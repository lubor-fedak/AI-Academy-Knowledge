# Lab 08: Instructions

## Phase 1: Design System Components (25 min)

### Step 1.1: Chat Bubble Component

Design chat bubbles that convey:
- Who sent the message (user vs. AI)
- Message content
- Timestamp
- Status (sending, sent, error)

```jsx
// ChatBubble.jsx
const ChatBubble = ({ message, sender, timestamp, status }) => {
  const isUser = sender === 'user';
  
  return (
    <div className={`bubble ${isUser ? 'user' : 'ai'}`}>
      {!isUser && <Avatar src="/ai-avatar.svg" alt="AI Assistant" />}
      <div className="content">
        <p>{message}</p>
        <span className="timestamp">{timestamp}</span>
        {status === 'sending' && <Spinner size="small" />}
        {status === 'error' && <ErrorIcon />}
      </div>
    </div>
  );
};
```

### Step 1.2: Confidence Indicator

When AI isn't certain, show it:

```jsx
const ConfidenceIndicator = ({ level }) => {
  const labels = {
    high: { text: "High confidence", color: "green", icon: "✓" },
    medium: { text: "Moderate confidence", color: "yellow", icon: "?" },
    low: { text: "Low confidence - verify", color: "red", icon: "⚠" }
  };
  
  const config = labels[level];
  
  return (
    <div className="confidence" style={{ color: config.color }}>
      <span>{config.icon}</span>
      <span>{config.text}</span>
    </div>
  );
};
```

### Step 1.3: Source Citation Component

For RAG systems, show where information comes from:

```jsx
const SourceCitation = ({ sources }) => {
  return (
    <div className="sources">
      <span className="label">Sources:</span>
      <ul>
        {sources.map((source, i) => (
          <li key={i}>
            <a href={source.url}>{source.title}</a>
            <span className="relevance">({source.relevance}% relevant)</span>
          </li>
        ))}
      </ul>
    </div>
  );
};
```

### Step 1.4: Loading States

Design informative loading experiences:

- **Skeleton loader:** Shape of expected content
- **Progress indicator:** "Thinking...", "Searching documents..."
- **Typing indicator:** Animated dots showing AI is "typing"

```jsx
const ThinkingIndicator = ({ stage }) => {
  const stages = [
    "Understanding your question...",
    "Searching relevant documents...",
    "Generating response..."
  ];
  
  return (
    <div className="thinking">
      <div className="dots">
        <span></span><span></span><span></span>
      </div>
      <span className="stage">{stages[stage]}</span>
    </div>
  );
};
```

---

## Phase 2: Streaming Implementation (25 min)

### Step 2.1: Server-Sent Events (SSE)

Backend sends chunks as they're generated:

```python
# FastAPI backend
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    async def generate():
        # Call your AI with streaming
        for chunk in ai_stream(request.message):
            yield f"data: {json.dumps({'text': chunk})}\n\n"
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
```

### Step 2.2: Frontend SSE Consumer

```jsx
const useStreamingChat = () => {
  const [message, setMessage] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  
  const sendMessage = async (userInput) => {
    setIsStreaming(true);
    setMessage('');
    
    const response = await fetch('/chat/stream', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userInput })
    });
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      
      const text = decoder.decode(value);
      const lines = text.split('\n');
      
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6);
          if (data === '[DONE]') {
            setIsStreaming(false);
          } else {
            const { text: chunk } = JSON.parse(data);
            setMessage(prev => prev + chunk);
          }
        }
      }
    }
  };
  
  return { message, isStreaming, sendMessage };
};
```

### Step 2.3: Smooth Rendering

Don't just append text - animate it:

```css
.streaming-text {
  animation: fadeIn 0.1s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0.5; }
  to { opacity: 1; }
}
```

---

## Phase 3: Accessibility (20 min)

### Step 3.1: WCAG 2.2 Checklist for Chat

- [ ] **Color contrast:** 4.5:1 minimum for text
- [ ] **Focus indicators:** Visible focus on all interactive elements
- [ ] **Keyboard navigation:** Tab through all controls
- [ ] **Screen reader:** ARIA labels on non-text elements
- [ ] **Motion:** Respect prefers-reduced-motion
- [ ] **Text size:** Works at 200% zoom

### Step 3.2: ARIA Labels

```jsx
<button 
  aria-label="Send message" 
  aria-disabled={isLoading}
>
  <SendIcon aria-hidden="true" />
</button>

<div 
  role="log" 
  aria-label="Chat conversation"
  aria-live="polite"
>
  {messages.map(m => <ChatBubble key={m.id} {...m} />)}
</div>
```

### Step 3.3: Focus Management

When new messages arrive, manage focus appropriately:

```jsx
const chatEndRef = useRef(null);

useEffect(() => {
  // Scroll to new message
  chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  
  // Announce to screen readers
  announcer.announce('New message from AI assistant');
}, [messages]);
```

### Step 3.4: Keyboard Shortcuts

```jsx
useEffect(() => {
  const handleKeydown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
    if (e.key === 'Escape') {
      handleCancel();
    }
  };
  
  document.addEventListener('keydown', handleKeydown);
  return () => document.removeEventListener('keydown', handleKeydown);
}, []);
```

---

## Phase 4: User Testing (20 min)

### Step 4.1: Prepare Test Script

```markdown
## User Testing Script

### Introduction (1 min)
"I'm going to show you an AI assistant interface. Please think aloud as you use it."

### Tasks (10 min)
1. Ask the assistant about vacation policy
2. Try to send a message while it's still responding
3. Find where a piece of information came from
4. Try using only keyboard (no mouse)

### Questions (5 min)
- What was confusing?
- What did you like?
- What would you change?
```

### Step 4.2: Conduct Tests

Test with 3-5 users:
- At least 1 screen reader user (or simulate)
- Mix of technical and non-technical users
- Note usability issues

### Step 4.3: Document Findings

| Issue | Severity | Users Affected | Fix |
|-------|----------|----------------|-----|
| Can't tell when AI is thinking | High | 3/5 | Add thinking indicator |
| Sources not obvious | Medium | 2/5 | Make sources more prominent |

---

## Extension Challenges

1. **Dark mode:** Add theme toggle
2. **Voice input:** Add speech-to-text
3. **Multi-modal:** Support image inputs
4. **Conversation history:** Add chat history
5. **Mobile gestures:** Swipe to dismiss, etc.

---

## Submission

Upload to SharePoint `/07-Submissions/Labs/Lab-08/`:
- Component code (`components/`)
- Working prototype (link or exported)
- `accessibility_report.md`
- `user_testing_findings.md`
- `REFLECTION.md`
