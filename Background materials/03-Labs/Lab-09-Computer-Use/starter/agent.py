"""
Lab 9: Computer Use Agent
Starter code for building a computer use agent with governance.
"""

import os
import yaml
import uuid
import logging
from datetime import datetime
from typing import Dict, Any, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


class GovernanceLayer:
    """Governance layer for controlling agent actions."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.action_count = 0
        self.last_reset = datetime.now()
        self.max_actions_per_minute = config.get('governance', {}).get('max_actions_per_minute', 10)

        # Load allowed actions
        self.allowed_targets = self._load_allowed_targets()
        self.blocked_patterns = ['DELETE', 'DROP', 'sudo', 'rm -rf', 'admin']

    def _load_allowed_targets(self) -> Dict[str, Any]:
        """Load allowed click targets from configuration."""
        return {
            'user_management_menu': {'x': (10, 150), 'y': (100, 130)},
            'search_box': {'x': (200, 500), 'y': (150, 180)},
            'reset_password_button': {'x': (400, 550), 'y': (300, 330)},
            'confirm_button': {'x': (300, 400), 'y': (400, 430)},
            'cancel_button': {'x': (200, 300), 'y': (400, 430)},
        }

    def is_allowed(self, action: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Check if action is allowed by governance rules.

        Returns:
            Tuple of (is_allowed, reason)
        """
        action_type = action.get('type')

        # Check 1: Action type allowed?
        allowed_types = ['click', 'type', 'key', 'scroll', 'wait', 'screenshot']
        if action_type not in allowed_types:
            return False, f"Action type '{action_type}' not allowed"

        # Check 2: Rate limit
        if not self._check_rate_limit():
            return False, "Rate limit exceeded"

        # Check 3: Target validation for clicks
        if action_type == 'click':
            if not self._check_click_target(action):
                return False, "Click target not in allowed regions"

        # Check 4: Content validation for typing
        if action_type == 'type':
            if not self._check_type_content(action):
                return False, "Type content contains blocked patterns"

        return True, "Action allowed"

    def _check_rate_limit(self) -> bool:
        """Check if we're within rate limits."""
        now = datetime.now()

        # Reset counter every minute
        if (now - self.last_reset).seconds >= 60:
            self.action_count = 0
            self.last_reset = now

        self.action_count += 1
        return self.action_count <= self.max_actions_per_minute

    def _check_click_target(self, action: Dict[str, Any]) -> bool:
        """Validate click target is in allowed regions."""
        target = action.get('target')
        if target and target in self.allowed_targets:
            return True

        # Check coordinates if provided
        x = action.get('x')
        y = action.get('y')
        if x is not None and y is not None:
            # TODO: Implement coordinate boundary checking
            # For now, allow named targets only
            pass

        return target in self.allowed_targets

    def _check_type_content(self, action: Dict[str, Any]) -> bool:
        """Check typed content for blocked patterns."""
        text = action.get('text', '').upper()
        for pattern in self.blocked_patterns:
            if pattern.upper() in text:
                return False
        return True


class CircuitBreaker:
    """Circuit breaker to prevent runaway failures."""

    def __init__(self, threshold: int = 3, reset_time: int = 300):
        self.threshold = threshold
        self.reset_time = reset_time
        self.failures = 0
        self.last_failure: Optional[datetime] = None
        self.state = "closed"  # closed, open, half-open

    def record_success(self):
        """Record successful action."""
        if self.state == "half-open":
            self.state = "closed"
            self.failures = 0

    def record_failure(self):
        """Record failed action."""
        self.failures += 1
        self.last_failure = datetime.now()

        if self.failures >= self.threshold:
            self.state = "open"
            logger.error(f"Circuit breaker OPEN after {self.failures} failures")

    def can_proceed(self) -> bool:
        """Check if we can proceed with an action."""
        if self.state == "closed":
            return True

        if self.state == "open":
            if self.last_failure and (datetime.now() - self.last_failure).seconds > self.reset_time:
                self.state = "half-open"
                logger.info("Circuit breaker half-open, allowing test request")
                return True
            return False

        return True  # half-open allows one test


class ComputerUseAgent:
    """
    Computer Use Agent with governance.

    This agent can control a computer interface while respecting
    governance rules and safety constraints.
    """

    def __init__(self, config_path: str = "config.yaml"):
        self.config = self._load_config(config_path)
        self.governance = GovernanceLayer(self.config)
        self.circuit_breaker = CircuitBreaker()
        self.action_log = []

    def _load_config(self, path: str) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if os.path.exists(path):
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        return {'test_mode': True}

    def process_ticket(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process an IT support ticket.

        Args:
            ticket: Dictionary containing ticket details

        Returns:
            Result of processing the ticket
        """
        ticket_type = ticket.get('type')
        logger.info(f"Processing ticket: {ticket_type}")

        if ticket_type == 'password_reset':
            return self.password_reset(ticket.get('user_email'))
        elif ticket_type == 'software_install':
            return self.software_install(ticket.get('software_name'))
        else:
            return {'status': 'error', 'message': f'Unknown ticket type: {ticket_type}'}

    def execute_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single action with governance checks.

        Args:
            action: The action to execute

        Returns:
            Result of the action
        """
        # Check circuit breaker
        if not self.circuit_breaker.can_proceed():
            return {'status': 'blocked', 'reason': 'circuit_breaker_open'}

        # Check governance
        is_allowed, reason = self.governance.is_allowed(action)
        if not is_allowed:
            logger.warning(f"Action blocked: {reason}")
            return {'status': 'blocked', 'reason': reason}

        # Execute action (in test mode, just log)
        if self.config.get('test_mode', True):
            result = self._simulate_action(action)
        else:
            result = self._do_action(action)

        # Log action
        self.action_log.append({
            'action': action,
            'result': result,
            'timestamp': datetime.now().isoformat()
        })

        # Update circuit breaker
        if result.get('status') == 'success':
            self.circuit_breaker.record_success()
        else:
            self.circuit_breaker.record_failure()

        return result

    def _simulate_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate action execution for testing."""
        logger.info(f"[SIMULATED] Executing: {action}")
        return {'status': 'success', 'simulated': True}

    def _do_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Actually execute the action.

        TODO: Implement real computer control here.
        This would integrate with Claude Computer Use API or OpenClaw.
        """
        raise NotImplementedError("Real execution not implemented - use test_mode: true")

    def password_reset(self, user_email: str) -> Dict[str, Any]:
        """
        Reset password for a user.

        Args:
            user_email: Email of user to reset password for

        Returns:
            Result including temporary password
        """
        logger.info(f"Starting password reset for {user_email}")

        # Step 1: Navigate to user management
        result = self.execute_action({'type': 'click', 'target': 'user_management_menu'})
        if result.get('status') != 'success':
            return {'status': 'error', 'step': 'navigation', 'details': result}

        result = self.execute_action({'type': 'wait', 'seconds': 1})

        # Step 2: Search for user
        result = self.execute_action({'type': 'click', 'target': 'search_box'})
        if result.get('status') != 'success':
            return {'status': 'error', 'step': 'search_box', 'details': result}

        result = self.execute_action({'type': 'type', 'text': user_email})
        if result.get('status') != 'success':
            return {'status': 'error', 'step': 'type_email', 'details': result}

        result = self.execute_action({'type': 'key', 'key': 'Enter'})
        result = self.execute_action({'type': 'wait', 'seconds': 2})

        # Step 3: Click reset password
        # TODO: Add verification that user was found before proceeding
        result = self.execute_action({'type': 'click', 'target': 'reset_password_button'})
        if result.get('status') != 'success':
            return {'status': 'error', 'step': 'reset_button', 'details': result}

        # Step 4: Generate temporary password
        temp_password = self._generate_temp_password()

        # Step 5: Confirm
        result = self.execute_action({'type': 'click', 'target': 'confirm_button'})
        if result.get('status') != 'success':
            return {'status': 'error', 'step': 'confirm', 'details': result}

        logger.info(f"Password reset successful for {user_email}")
        return {
            'status': 'success',
            'user_email': user_email,
            'temp_password': temp_password,
            'actions_taken': len(self.action_log)
        }

    def _generate_temp_password(self) -> str:
        """Generate a temporary password."""
        import secrets
        import string
        alphabet = string.ascii_letters + string.digits + "!@#$%"
        return ''.join(secrets.choice(alphabet) for _ in range(16))

    def software_install(self, software_name: str) -> Dict[str, Any]:
        """
        Install software for a user.

        TODO: Implement software installation flow.
        """
        logger.info(f"Software install requested: {software_name}")
        return {'status': 'not_implemented', 'message': 'Software install not yet implemented'}

    def get_action_log(self) -> list:
        """Return the action log."""
        return self.action_log


def main():
    """Main entry point for testing."""
    import argparse

    parser = argparse.ArgumentParser(description='Computer Use Agent')
    parser.add_argument('--action', type=str, help='Action to perform')
    parser.add_argument('--user', type=str, help='User email for password reset')
    parser.add_argument('--test', action='store_true', help='Run in test mode')
    parser.add_argument('--test-suite', type=str, help='Run test suite from YAML file')

    args = parser.parse_args()

    # Initialize agent
    agent = ComputerUseAgent()

    if args.test:
        # Run basic test
        logger.info("Running basic test...")
        result = agent.password_reset("test@example.com")
        print(f"Result: {result}")

    elif args.action == 'password_reset' and args.user:
        result = agent.password_reset(args.user)
        print(f"Result: {result}")

    elif args.test_suite:
        # Load and run test suite
        with open(args.test_suite, 'r') as f:
            tests = yaml.safe_load(f)

        for test in tests.get('test_scenarios', []):
            logger.info(f"Running test: {test['name']}")
            # TODO: Implement test execution
            print(f"  {test['name']}: TODO")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
