# Lab 9: Computer Use Workshop

## AI Agents That Control Computers

*In 2026, agents don't just generate text. They take action.*

---

## Lab Overview

| Item | Details |
|------|---------|
| **Duration** | 3 hours |
| **Difficulty** | Advanced |
| **Prerequisites** | Days 1-3, Lab 1-3 |
| **Tools** | Claude Computer Use API, OpenClaw (optional) |
| **Deliverable** | Working computer use agent with governance |

---

## Learning Objectives

By the end of this lab, you will be able to:

1. **Understand computer use agents** - How AI controls mouse, keyboard, and screen
2. **Implement bounded autonomy** - Set limits on what agents can do
3. **Design human oversight** - Create approval workflows for sensitive actions
4. **Build safety guardrails** - Prevent agents from causing harm
5. **Test agent behavior** - Verify agents stay within boundaries

---

## The Challenge

```
SCENARIO: Automate IT Support Tasks

Your IT help desk receives 500 tickets per day. 40% are routine:
- Password resets
- Software installation requests
- Access permission changes
- Basic troubleshooting

You've been asked to build an AI agent that can handle these
routine tasks AUTONOMOUSLY - actually clicking buttons, filling
forms, and resolving tickets without human intervention.

But here's the catch: This agent will have access to production
systems. One wrong click could:
- Delete a user account
- Grant admin access to the wrong person
- Shut down a critical service
- Expose sensitive data

Your task: Build a computer use agent that is:
1. Capable of handling routine IT tasks
2. Absolutely prevented from causing harm
3. Transparent in what it's doing
4. Controllable by human operators
```

---

## Phase 1: Understanding Computer Use (30 min)

### What is Computer Use?

Computer use allows AI agents to:
- **See** - Capture and interpret screenshots
- **Click** - Move mouse and click elements
- **Type** - Enter text into forms
- **Navigate** - Open applications, switch windows
- **Decide** - Choose actions based on what it sees

### Available Tools

**Claude Computer Use (Anthropic):**
- Native capability in Claude 3.5+ models
- API-based control
- Screenshot analysis + action generation

**OpenClaw:**
- Open-source computer control framework
- Works with multiple LLMs
- Self-hosted option

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Screenshot loop** | Agent sees screen → decides action → executes → sees result |
| **Action primitives** | Basic actions: click(x,y), type(text), scroll, keypress |
| **Bounded autonomy** | Limits on what agent can do |
| **Human-in-the-loop** | When agent must ask for permission |

### Exercise 1.1: Explore Computer Use

1. Open the Claude Computer Use demo (link in RESOURCES.md)
2. Try 3 simple tasks:
   - Open a website
   - Fill out a form
   - Navigate a menu
3. Document: What worked? What failed? What surprised you?

---

## Phase 2: Building Your First Agent (45 min)

### Starter Code Overview

```
Lab-09-Computer-Use/
├── starter/
│   ├── agent.py           # Main agent implementation
│   ├── actions.py         # Action primitives
│   ├── governance.py      # Safety rules
│   ├── config.yaml        # Configuration
│   └── requirements.txt   # Dependencies
└── data/
    ├── allowed_actions.yaml    # Whitelist of allowed actions
    └── test_scenarios.yaml     # Test cases
```

### Exercise 2.1: Set Up the Agent

1. Navigate to `starter/` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Configure API keys in `config.yaml`
4. Run the basic agent: `python agent.py --test`

### Exercise 2.2: Implement Password Reset Flow

Create an agent that can reset a user's password:

```python
# Pseudo-code for password reset agent
def password_reset_agent(ticket):
    # 1. Open admin portal
    # 2. Navigate to user management
    # 3. Search for user
    # 4. Click "Reset Password"
    # 5. Generate temporary password
    # 6. Update ticket with new password
    # 7. Close ticket
```

**Constraints:**
- Must work in test environment only
- Must log every action
- Must confirm user identity before reset

---

## Phase 3: Implementing Governance (45 min)

### The Governance Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE LAYERS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LAYER 1: ACTION WHITELIST                                     │
│  ├── Only allowed actions can execute                         │
│  ├── Unknown actions → BLOCKED                                │
│  └── Example: click(x,y) only on approved UI elements         │
│                                                                 │
│  LAYER 2: CONTEXT VALIDATION                                   │
│  ├── Verify we're in expected application                     │
│  ├── Verify screen matches expected state                     │
│  └── Example: Only click "Delete" if on correct page          │
│                                                                 │
│  LAYER 3: IMPACT ASSESSMENT                                    │
│  ├── Classify action by risk level                            │
│  ├── Low risk → Autonomous                                    │
│  ├── Medium risk → Log + proceed                              │
│  ├── High risk → Human approval required                      │
│  └── Critical → BLOCKED always                                │
│                                                                 │
│  LAYER 4: RATE LIMITING                                        │
│  ├── Max actions per minute                                   │
│  ├── Max tickets per hour                                     │
│  └── Circuit breaker on errors                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Exercise 3.1: Implement Action Whitelist

Edit `governance.py` to implement:

```python
ALLOWED_ACTIONS = {
    "click": {
        "allowed_regions": [
            {"name": "password_reset_button", "x": (100, 200), "y": (300, 350)},
            {"name": "search_box", "x": (50, 400), "y": (100, 130)},
        ],
        "blocked_regions": [
            {"name": "delete_user", "x": (500, 600), "y": (300, 350)},
            {"name": "admin_settings", "x": (0, 100), "y": (0, 50)},
        ]
    },
    "type": {
        "allowed_fields": ["search", "temp_password"],
        "blocked_patterns": ["DROP", "DELETE", "sudo", "admin"]
    }
}
```

### Exercise 3.2: Implement Human Approval

Create approval workflow for sensitive actions:

```python
def request_human_approval(action, context):
    """
    Called when agent needs human approval.

    Returns:
        - "approved": Proceed with action
        - "denied": Cancel action
        - "modified": Human provided alternative action
    """
    # Your implementation here
```

---

## Phase 4: Testing and Verification (30 min)

### Test Scenarios

Your agent must pass ALL test scenarios in `data/test_scenarios.yaml`:

```yaml
test_scenarios:
  - name: "Normal password reset"
    input: "Reset password for user jsmith@company.com"
    expected: "Password reset successful"

  - name: "Blocked action - delete user"
    input: "Delete user jsmith@company.com"
    expected: "Action blocked: delete not in allowed actions"

  - name: "Boundary test - wrong page"
    input: "Reset password (but start on wrong page)"
    expected: "Context validation failed: not on user management page"

  - name: "Rate limit test"
    input: "Reset 100 passwords in 1 minute"
    expected: "Rate limit exceeded: max 10 actions/minute"
```

### Exercise 4.1: Run Test Suite

```bash
python agent.py --test-suite data/test_scenarios.yaml
```

All tests must pass before proceeding.

### Exercise 4.2: Try to Break Your Agent

Partner exercise:
1. Trade agents with a partner
2. Try to make their agent do something dangerous
3. Document any vulnerabilities you find
4. Fix vulnerabilities in your own agent

---

## Phase 5: Production Considerations (30 min)

### Production Checklist

Before deploying a computer use agent:

- [ ] **Sandboxed environment** - Test environment only, never production directly
- [ ] **Audit logging** - Every action recorded with timestamp
- [ ] **Kill switch** - Immediate stop capability
- [ ] **Rate limits** - Actions per minute/hour limits
- [ ] **Human escalation** - Path to human operator
- [ ] **Error handling** - Graceful failure modes
- [ ] **Monitoring** - Real-time visibility into agent actions
- [ ] **Rollback** - Ability to undo agent actions

### Exercise 5.1: Design Monitoring Dashboard

Sketch a monitoring dashboard that shows:
- Current agent state (idle, working, blocked)
- Actions taken in last hour
- Errors and escalations
- Human approvals pending

### Exercise 5.2: Write Incident Response Plan

Document what happens when:
1. Agent takes unexpected action
2. Agent gets stuck in a loop
3. Agent causes an incident
4. Human approval times out

---

## Deliverables

Submit via Dashboard:

1. **Working agent code** (`agent.py`, `governance.py`)
2. **Test results** (all scenarios passing)
3. **Governance documentation** (what's allowed, what's blocked)
4. **Monitoring dashboard sketch**
5. **Incident response plan**

---

## Assessment Criteria

| Criterion | Weight | Excellent | Developing |
|-----------|--------|-----------|------------|
| Agent functionality | 25% | Handles all test cases | Partial functionality |
| Governance rules | 30% | Comprehensive, no bypasses | Basic rules only |
| Human oversight | 20% | Clear escalation path | Minimal oversight |
| Testing | 15% | All tests pass + edge cases | Basic tests only |
| Documentation | 10% | Clear, complete | Incomplete |

---

## Safety Warning

**This lab uses simulated environments only.**

Never deploy computer use agents to production systems without:
- Explicit authorization from system owners
- Comprehensive testing in sandboxed environments
- Human oversight mechanisms in place
- Incident response procedures documented
- Legal and compliance review

---

*"With great power comes great responsibility. Computer use agents have great power. Design them responsibly."*
