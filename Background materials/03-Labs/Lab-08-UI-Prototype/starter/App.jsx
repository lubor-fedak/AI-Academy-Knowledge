/**
 * AI Academy Lab 08 - Chat Interface
 * Starter template (React)
 */

import React, { useState, useRef, useEffect } from 'react';
import './styles.css';

// ============================================
// Components
// ============================================

const ChatBubble = ({ message, sender, timestamp }) => {
  // TODO: Implement chat bubble
  return (
    <div className={`bubble ${sender}`}>
      <p>{message}</p>
      <span className="timestamp">{timestamp}</span>
    </div>
  );
};

const ThinkingIndicator = () => {
  // TODO: Implement thinking animation
  return (
    <div className="thinking">
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
    </div>
  );
};

const ConfidenceIndicator = ({ level }) => {
  // TODO: Implement confidence display
  return null;
};

const SourceCitation = ({ sources }) => {
  // TODO: Implement source display
  return null;
};

// ============================================
// Main App
// ============================================

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message
    const userMessage = {
      id: Date.now(),
      text: input,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    // TODO: Implement streaming response
    // For now, simulate a response
    setTimeout(() => {
      const aiMessage = {
        id: Date.now() + 1,
        text: 'This is a placeholder response. Implement streaming!',
        sender: 'ai',
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages(prev => [...prev, aiMessage]);
      setIsLoading(false);
    }, 1000);
  };

  return (
    <div className="chat-container">
      <header className="chat-header">
        <h1>AI Assistant</h1>
      </header>

      <main 
        className="chat-messages" 
        role="log" 
        aria-label="Chat conversation"
      >
        {messages.map(msg => (
          <ChatBubble key={msg.id} {...msg} />
        ))}
        {isLoading && <ThinkingIndicator />}
        <div ref={messagesEndRef} />
      </main>

      <form className="chat-input" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          aria-label="Message input"
          disabled={isLoading}
        />
        <button 
          type="submit" 
          aria-label="Send message"
          disabled={isLoading || !input.trim()}
        >
          Send
        </button>
      </form>
    </div>
  );
};

export default App;
