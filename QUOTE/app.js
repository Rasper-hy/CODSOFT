import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState('');
  const [favorites, setFavorites] = useState([]);

  const fetchQuote = async () => {
    const res = await fetch('https://api.quotable.io/random');
    const data = await res.json();
    setQuote(data.content);
  };

  useEffect(() => {
    fetchQuote();
  }, []);

  const saveFavorite = () => {
    if (!favorites.includes(quote)) {
      setFavorites([...favorites, quote]);
    }
  };

  const shareQuote = () => {
    if (navigator.share) {
      navigator.share({ text: quote });
    } else {
      navigator.clipboard.writeText(quote);
      alert('Quote copied!');
    }
  };

  return (
    <div className="container">
      <h1>🌟 Quote of the Day</h1>
      <p className="quote">"{quote}"</p>
      <div className="buttons">
        <button onClick={fetchQuote}>🔄 New Quote</button>
        <button onClick={shareQuote}>📤 Share</button>
        <button onClick={saveFavorite}>❤️ Save</button>
      </div>
      <h3>⭐ Favorites</h3>
      <ul>
        {favorites.map((q, i) => <li key={i}>{q}</li>)}
      </ul>
    </div>
  );
}

export default App;