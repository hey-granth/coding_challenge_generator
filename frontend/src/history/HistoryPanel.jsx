import "react";
import {useState, useEffect} from "react";
import {MCQChallenge} from "../challenge/MCQChallenge.jsx";

export function HistoryPanel() {
    const [history, setHistory] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchHistory()
    }, [])

    const fetchHistory = async () => {
        setIsLoading(false);
    }

    if (isLoading) {
        return <div className="loading">Loading History...</div>
    }

    if (error) {
        return <div className="error-message">
            <p>{error}</p>
            <button onClick={fetchHistory}>Retry</button>
        </div>;
    }
    return <div className="history-panel">
        <h2>Challenge History</h2>
        {history.length === 0 ? (
            <p>No challenges generated yet.</p>
        ) : (
            <div className="history-list">
                {history.map((challenge) => {
                    return <MCQChallenge key={challenge.id} challenge={challenge} showExplanation/>
                })}
            </div>
        )}
    </div>
}