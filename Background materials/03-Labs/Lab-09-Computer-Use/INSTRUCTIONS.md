# Lab 9: Computer Use Workshop - Detailed Instructions

## Pre-Lab Setup (15 minutes before lab)

### 1. Environment Setup

```bash
# Clone the starter code (if not already done)
cd /path/to/ai-academy/03-Labs/Lab-09-Computer-Use

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r starter/requirements.txt
```

### 2. API Configuration

Create `starter/config.yaml`:

```yaml
# Claude Computer Use API
anthropic:
  api_key: ${ANTHROPIC_API_KEY}
  model: claude-3-5-sonnet-20241022

# Governance settings
governance:
  max_actions_per_minute: 10
  max_tickets_per_hour: 50
  require_approval_for:
    - delete
    - admin
    - permission_change

# Logging
logging:
  level: DEBUG
  file: agent_actions.log

# Test mode
test_mode: true  # ALWAYS true until production approved
```

### 3. Test Environment

The lab uses a simulated IT admin interface. Start it:

```bash
python starter/test_environment.py
```

This opens a local web interface that simulates an IT admin portal.

---

## Phase 1: Understanding Computer Use

### Step 1.1: Read the Conceptual Overview

Computer use agents work in a loop:

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPUTER USE LOOP                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│   │ Capture  │────▶│ Analyze  │────▶│ Decide   │              │
│   │Screenshot│     │  Screen  │     │  Action  │              │
│   └──────────┘     └──────────┘     └──────────┘              │
│        ▲                                  │                    │
│        │                                  ▼                    │
│        │           ┌──────────┐     ┌──────────┐              │
│        └───────────│  Wait    │◀────│ Execute  │              │
│                    │  Result  │     │  Action  │              │
│                    └──────────┘     └──────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Step 1.2: Explore the Demo

1. Open the Claude Computer Use demo
2. Try these tasks:
   - "Open a browser and search for 'AI governance'"
   - "Take a screenshot and describe what you see"
   - "Click on the first search result"

3. Document your observations:
   - How does the agent decide where to click?
   - What happens when it makes a mistake?
   - How fast/slow is the loop?

### Step 1.3: Understand Action Primitives

The agent can execute these basic actions:

| Action | Parameters | Example |
|--------|------------|---------|
| `click` | x, y coordinates | `click(150, 300)` |
| `type` | text string | `type("jsmith@company.com")` |
| `key` | key name | `key("Enter")` |
| `scroll` | direction, amount | `scroll("down", 3)` |
| `screenshot` | none | `screenshot()` |
| `wait` | seconds | `wait(2)` |

---

## Phase 2: Building Your First Agent

### Step 2.1: Review Starter Code

Open `starter/agent.py` and understand the structure:

```python
class ComputerUseAgent:
    def __init__(self, config):
        self.config = config
        self.governance = GovernanceLayer(config)
        self.action_log = []

    def process_ticket(self, ticket):
        """Main entry point for processing a ticket."""
        # 1. Validate ticket
        # 2. Plan actions
        # 3. Execute with governance checks
        # 4. Verify result
        pass

    def execute_action(self, action):
        """Execute a single action with governance."""
        # Check if action is allowed
        if not self.governance.is_allowed(action):
            return {"status": "blocked", "reason": "governance"}

        # Execute action
        result = self._do_action(action)

        # Log action
        self.action_log.append({
            "action": action,
            "result": result,
            "timestamp": datetime.now()
        })

        return result
```

### Step 2.2: Implement Password Reset

Complete the `password_reset` method:

```python
def password_reset(self, user_email):
    """
    Reset password for a user.

    Steps:
    1. Navigate to user management
    2. Search for user
    3. Click reset password
    4. Generate temp password
    5. Confirm action
    """

    # Step 1: Navigate
    self.execute_action({"type": "click", "target": "user_management_menu"})
    self.execute_action({"type": "wait", "seconds": 1})

    # Step 2: Search
    self.execute_action({"type": "click", "target": "search_box"})
    self.execute_action({"type": "type", "text": user_email})
    self.execute_action({"type": "key", "key": "Enter"})
    self.execute_action({"type": "wait", "seconds": 2})

    # Step 3: Find and click reset
    # YOUR CODE HERE: Verify user is found before proceeding

    # Step 4: Generate password
    # YOUR CODE HERE: Generate secure temp password

    # Step 5: Confirm
    # YOUR CODE HERE: Verify password was reset successfully

    return {"status": "success", "temp_password": "..."}
```

### Step 2.3: Test Your Implementation

```bash
python agent.py --action password_reset --user jsmith@test.com
```

Expected output:
```
[INFO] Starting password reset for jsmith@test.com
[INFO] Navigating to user management...
[INFO] Searching for user...
[INFO] User found: John Smith (jsmith@test.com)
[INFO] Clicking reset password...
[INFO] Generating temporary password...
[INFO] Password reset successful
[INFO] Temporary password: Temp$ecure123!
```

---

## Phase 3: Implementing Governance

### Step 3.1: Action Whitelist

Edit `starter/governance.py`:

```python
class GovernanceLayer:
    def __init__(self, config):
        self.config = config
        self.action_count = 0
        self.last_reset = datetime.now()

    def is_allowed(self, action):
        """Check if action is allowed by governance rules."""

        # Check 1: Action type allowed?
        if not self._check_action_type(action):
            return False, "Action type not in whitelist"

        # Check 2: Target allowed?
        if not self._check_target(action):
            return False, "Target not in allowed list"

        # Check 3: Rate limit OK?
        if not self._check_rate_limit():
            return False, "Rate limit exceeded"

        # Check 4: Context valid?
        if not self._check_context(action):
            return False, "Invalid context for action"

        return True, "Action allowed"

    def _check_action_type(self, action):
        allowed_types = ["click", "type", "key", "scroll", "wait", "screenshot"]
        return action.get("type") in allowed_types

    def _check_target(self, action):
        # YOUR CODE HERE: Implement target whitelist checking
        pass

    def _check_rate_limit(self):
        # YOUR CODE HERE: Implement rate limiting
        pass

    def _check_context(self, action):
        # YOUR CODE HERE: Verify we're in expected application state
        pass
```

### Step 3.2: Human Approval Workflow

Implement approval for sensitive actions:

```python
class ApprovalWorkflow:
    def __init__(self):
        self.pending_approvals = {}

    def request_approval(self, action, context):
        """Request human approval for an action."""
        approval_id = str(uuid.uuid4())

        self.pending_approvals[approval_id] = {
            "action": action,
            "context": context,
            "requested_at": datetime.now(),
            "status": "pending"
        }

        # Notify human (your implementation)
        self._notify_human(approval_id, action, context)

        # Wait for response (with timeout)
        return self._wait_for_response(approval_id, timeout=300)

    def _notify_human(self, approval_id, action, context):
        """Send notification to human operator."""
        # YOUR CODE HERE: Slack, Teams, email, dashboard, etc.
        pass

    def _wait_for_response(self, approval_id, timeout):
        """Wait for human response with timeout."""
        # YOUR CODE HERE: Implement waiting with timeout
        pass
```

### Step 3.3: Circuit Breaker

Implement automatic stop on errors:

```python
class CircuitBreaker:
    def __init__(self, threshold=3, reset_time=300):
        self.threshold = threshold
        self.reset_time = reset_time
        self.failures = 0
        self.last_failure = None
        self.state = "closed"  # closed, open, half-open

    def record_failure(self):
        self.failures += 1
        self.last_failure = datetime.now()

        if self.failures >= self.threshold:
            self.state = "open"
            self._alert_operators()

    def can_proceed(self):
        if self.state == "closed":
            return True

        if self.state == "open":
            # Check if reset time has passed
            if (datetime.now() - self.last_failure).seconds > self.reset_time:
                self.state = "half-open"
                return True
            return False

        if self.state == "half-open":
            return True  # Allow one test request

    def _alert_operators(self):
        """Alert operators that circuit breaker tripped."""
        # YOUR CODE HERE
        pass
```

---

## Phase 4: Testing

### Step 4.1: Unit Tests

Run the test suite:

```bash
pytest starter/tests/ -v
```

### Step 4.2: Integration Tests

Run against test environment:

```bash
python agent.py --test-suite data/test_scenarios.yaml --verbose
```

### Step 4.3: Adversarial Testing

Try to bypass your governance:

```python
# Test cases to try
adversarial_tests = [
    # Try to access blocked area
    {"action": "click", "x": 550, "y": 325},  # Near delete button

    # Try injection in type
    {"action": "type", "text": "'; DROP TABLE users; --"},

    # Try to exceed rate limit
    [{"action": "click", "x": 100, "y": 100}] * 100,

    # Try with invalid context
    {"action": "click", "target": "reset_password", "context": "home_page"},
]
```

---

## Phase 5: Production Preparation

### Step 5.1: Monitoring Setup

Create monitoring configuration:

```yaml
# monitoring.yaml
metrics:
  - name: actions_per_minute
    type: gauge
    alert_threshold: 15

  - name: errors_per_hour
    type: counter
    alert_threshold: 5

  - name: human_approvals_pending
    type: gauge
    alert_threshold: 10

  - name: circuit_breaker_state
    type: status
    alert_on: ["open"]

dashboards:
  - name: Agent Activity
    panels:
      - type: timeline
        metric: actions_per_minute
      - type: status
        metric: circuit_breaker_state
      - type: log
        filter: level=ERROR
```

### Step 5.2: Incident Response

Document your incident response plan in `INCIDENT_RESPONSE.md`.

---

## Submission Checklist

- [ ] `agent.py` with working password reset
- [ ] `governance.py` with all checks implemented
- [ ] All test scenarios passing
- [ ] Adversarial tests documented
- [ ] Monitoring configuration
- [ ] Incident response plan

---

## Common Issues

| Issue | Solution |
|-------|----------|
| API rate limiting | Implement exponential backoff |
| Screenshot too slow | Reduce resolution, increase interval |
| Actions miss target | Increase wait time, verify element loaded |
| Governance too strict | Adjust thresholds based on testing |

---

*"The best computer use agent is one that knows when NOT to act."*
