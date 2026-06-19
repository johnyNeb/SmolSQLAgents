import React, { useState, useEffect } from 'react';

const SQLGeneration = ({ sqlValidation, generatedSql, copySqlToClipboard, query }) => {
  const [feedback, setFeedback] = useState(null);
  const [feedbackSent, setFeedbackSent] = useState(false);

  // Reset feedback when a new query result comes in
  useEffect(() => {
    setFeedback(null);
    setFeedbackSent(false);
  }, [generatedSql]);

  if (!sqlValidation) return null;

  const isValid = sqlValidation.is_valid || sqlValidation.query_execution?.success;
  const isDiscovery = sqlValidation.is_discovery;

  const submitFeedback = async (correct) => {
    setFeedback(correct ? 'up' : 'down');
    try {
      await fetch('http://127.0.0.1:5000/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: query || '',
          generated_sql: generatedSql || '',
          correct
        })
      });
      setFeedbackSent(true);
    } catch (e) {
      console.error('Feedback failed:', e);
    }
  };

  return (
    <div className="card mb-3">
      <div className="card-header bg-white d-flex justify-content-between align-items-center">
        <h5 className="mb-0">
          <i className={`bi ${isDiscovery ? 'bi-chat-text' : 'bi-code-slash'} me-2`}></i>
          {isDiscovery ? 'Discovery Answer' : 'Generated SQL'}
        </h5>
        <div className="d-flex align-items-center gap-2">
          {!isDiscovery && (
            <button className="btn btn-sm btn-outline-secondary" onClick={copySqlToClipboard}>
              <i className="bi bi-clipboard me-1"></i>Copy
            </button>
          )}
          <span className={`badge ${isValid ? 'bg-success' : 'bg-danger'}`}>
            {isValid ? 'Valid' : 'Invalid'}
          </span>
        </div>
      </div>
      <div className="card-body">
        {isDiscovery ? (
          <div className="p-3 bg-light rounded">
            <p className="mb-0" style={{ lineHeight: '1.7' }}>
              {sqlValidation.answer}
            </p>
          </div>
        ) : (
          <pre className="bg-light p-3 rounded">
            <code>{generatedSql}</code>
          </pre>
        )}

        {isValid && (
          <div className="d-flex align-items-center gap-2 mt-3">
            <small className="text-muted">Was this helpful?</small>
            {feedbackSent ? (
              <small className="text-success">
                <i className="bi bi-check-circle me-1"></i>Thanks!
              </small>
            ) : (
              <>
                <button
                  className={`btn btn-sm ${feedback === 'up' ? 'btn-success' : 'btn-outline-success'}`}
                  onClick={() => submitFeedback(true)}
                >
                  <i className="bi bi-hand-thumbs-up"></i>
                </button>
                <button
                  className={`btn btn-sm ${feedback === 'down' ? 'btn-danger' : 'btn-outline-danger'}`}
                  onClick={() => submitFeedback(false)}
                >
                  <i className="bi bi-hand-thumbs-up"></i>
                </button>
              </>
            )}
          </div>
        )}

        {sqlValidation.errors && sqlValidation.errors.length > 0 && (
          <div className="mt-3">
            <h6>Validation Errors:</h6>
            <ul className="list-unstyled">
              {sqlValidation.errors.map((error, index) => (
                <li key={index} className="text-danger">
                  <i className="bi bi-exclamation-triangle me-1"></i>
                  {error}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default SQLGeneration;