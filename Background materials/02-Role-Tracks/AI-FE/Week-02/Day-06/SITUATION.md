# Day 6: Streaming Responses

## AI-FE Track - Week 2, Day 6

### The Situation: "Why Does It Take So Long?"

Users see a spinner for 30 seconds, then BOOM - wall of text.
Meanwhile, the AI is generating tokens the whole time.

**Challenge:** Implement streaming UI that shows text as it arrives.

### Technical Approach
- Server-Sent Events (SSE) or WebSocket
- Incremental DOM updates
- Smooth text appearance (typing effect optional)
- Handle stream interruption

### Deliverables
1. Streaming chat component
2. SSE/WebSocket integration
3. Graceful stream error handling
