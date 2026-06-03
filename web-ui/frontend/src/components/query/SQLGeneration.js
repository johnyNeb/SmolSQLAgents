import React from 'react';

const SQLGeneration = ({ sqlValidation, generatedSql, copySqlToClipboard }) => {
  if (!sqlValidation) return null;

  const isValid = sqlValidation.is_valid || sqlValidation.query_execution?.success;
  const isDiscovery = sqlValidation.is_discovery;

  return (
    <div className="card mb-3">
      <div className="card-header bg-white d-flex justify-content-between align-items-center">
        <h5 className="mb-0">
          <i className={`bi ${isDiscovery ? 'bi-chat-text' : 'bi-code-slash'} me-2`}></i>
          {isDiscovery ? 'Discovery Answer' : 'Generated SQL'}
        </h5>
        <div>
          {!isDiscovery && (
            <button
              className="btn btn-sm btn-outline-secondary me-2"
              onClick={copySqlToClipboard}
            >
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