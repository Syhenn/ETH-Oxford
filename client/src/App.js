import { useState, useEffect } from "react";
import "./styles/styles.css";
export default function CryptoTrends() {
  const [sentiments, setSentiments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setSentiments([
        { crypto: "Bitcoin", score: 1.2 },
        { crypto: "Ethereum", score: 0.8 },
        { crypto: "Avalanche", score: 0.5 },
      ]);
      setLoading(false);
    }, 2000);
  }, []);

  // Générer des particules
  const particles = new Array(30).fill(0).map((_, i) => ({
    id: i,
    top: Math.random() * 100 + "vh",
    left: Math.random() * 100 + "vw",
    animationDuration: Math.random() * 5 + 3 + "s",
  }));

  return (
    <div className="container">
      {particles.map((p) => (
        <div
          key={p.id}
          className="particle"
          style={{
            top: p.top,
            left: p.left,
            animationDuration: p.animationDuration,
          }}
        />
      ))}

      <h1 className="title">Crypto popularity 🚀</h1>

      {loading ? (
        <p className="loading">Chargement des tendances...</p>
      ) : (
        <div className="grid">
          {sentiments.map((crypto, index) => (
            <div key={index} className="card">
              <h2 className="crypto-name">{crypto.crypto}</h2>
              <p className="score">Score: {crypto.score}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
