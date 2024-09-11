import React from 'react';
import './Result.css';

const QuizResult = ({ quizData }) => {
  return (
    <div className="container">
      <h1 className="quiz-title">Quiz Result</h1>
      <div className="result-container">
        {/* Display quiz results here */}
        <pre>{JSON.stringify(quizData, null, 2)}</pre>
        <a href="/">Back to Quiz Generator</a>
      </div>
    </div>
  );
};

export default QuizResult;
