import { useState, useRef, useEffect } from 'react';

function App() {
  const [messages, setMessages] = useState([
    { role: 'socrates', content: 'Greetings, seeker of truth. What is on your mind today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const scrollRef = useRef(null);

  // --- API CONFIGURATION ---
  // If VITE_API_URL is set in Vercel, it uses that. Otherwise, it defaults to localhost.
  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async (e) => {
    if (e) e.preventDefault();
    if (!input.trim() || isLoading) return;

    const messageText = input;
    setInput('');
    setIsLoading(true);

    setMessages((prev) => [...(prev || []), { role: 'user', content: messageText }]);

    try {
      // --- DYNAMIC FETCH CALL ---
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: messageText }),
      });

      if (!response.ok) throw new Error(`Server Error: ${response.status}`);

      const data = await response.json();
      
      // Extraction logic to prevent [object Object]
      let rawValue = data.reply || data.socrates_response || data.response || data;
      if (typeof rawValue === 'object' && rawValue !== null) {
          rawValue = rawValue.content || rawValue.text || JSON.stringify(rawValue);
      }

      setMessages((prev) => [
        ...prev, 
        { role: 'socrates', content: String(rawValue) } 
      ]);

    } catch (error) {
      console.error("Critical UI Error:", error);
      setMessages((prev) => [
        ...prev, 
        { role: 'socrates', content: 'The connection to the Agora was lost. Please check your backend.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-slate-50 font-sans antialiased text-slate-900">
      <header className="py-6 bg-white border-b border-slate-200 text-center shadow-sm">
        <h1 className="text-2xl font-serif font-bold text-slate-800 tracking-tight">Project Socrates</h1>
        <p className="text-xs uppercase tracking-widest text-slate-400 mt-1">Intellectual AI Assistant</p>
      </header>

      <main className="flex-1 overflow-y-auto p-4 md:p-8">
        <div className="max-w-3xl mx-auto space-y-6">
          {(messages || []).map((msg, index) => (
            <div key={index} className={`flex ${msg?.role === 'user' ? 'justify-end' : 'justify-start'} mb-6`}>
              <div className={`max-w-[85%] px-5 py-3 rounded-2xl shadow-sm ${
                msg?.role === 'user' 
                ? 'bg-amber-600 text-white rounded-tr-none' 
                : 'bg-white border border-slate-200 text-slate-800 rounded-tl-none'
              }`}>
                <p className="leading-relaxed">{msg?.content || "..."}</p>
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div className="flex justify-start animate-pulse">
              <div className="bg-slate-200 h-10 w-24 rounded-2xl rounded-tl-none"></div>
            </div>
          )}
          <div ref={scrollRef} />
        </div>
      </main>

      <footer className="p-4 bg-white border-t border-slate-200">
        <form onSubmit={handleSendMessage} className="max-w-3xl mx-auto flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question..."
            className="flex-1 bg-slate-100 border-none rounded-full px-6 py-3 focus:ring-2 focus:ring-amber-500 transition-all outline-none"
            disabled={isLoading}
          />
          <button 
            type="submit" 
            disabled={isLoading}
            className="bg-slate-900 text-white px-6 py-3 rounded-full hover:bg-slate-800 transition-colors disabled:opacity-50"
          >
            {isLoading ? 'Thinking...' : 'Send'}
          </button>
        </form>
      </footer>
    </div>
  );
}

export default App;