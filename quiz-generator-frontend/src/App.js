// App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import QuizResult from './QuizResult.js';

const Home = () => {
  // State variables for form inputs
  const [quizType, setQuizType] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [textInput, setTextInput] = useState('');
  const [numQuestions, setNumQuestions] = useState(0); // New state for the number of questions
  const navigate = useNavigate();

  // Function to handle quiz generation
  const generateQuiz = async () => {
    try {
      // Validate that numQuestions is a positive integer
      if (!Number.isInteger(numQuestions) || numQuestions <= 0) {
        console.error('Please enter a valid number of questions.');
        return;
      }

      // Make a POST request to your backend endpoint with the quiz data
      const response = await axios.post('http://localhost:5000/generate', {
        quizType,
        difficulty,
        textInput,
        numQuestions, // Include the number of questions in the request
      });

      // Log the response from the backend (for testing purposes)
      console.log('Backend response:', response.data);

      // After a successful POST request, navigate to the /quiz-results route
      navigate('/quiz-results');
    } catch (error) {
      // Log any errors that occur during the API request
      console.error('Error making API request:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="quiz-title">Quiz Generator</h1>
      <form className="form">
        <div className="form-row">
          <div className="form-group">
            <label>Quiz Type</label>
            <select
              value={quizType}
              onChange={(e) => setQuizType(e.target.value)}
            >
              <option value="">Select Quiz Type</option>
              <option value="open-ended">Open Ended</option>
              <option value="multiple-choice">Multiple Choice</option>
              <option value="matching">Matching</option>
              <option value="true-false">True/False</option>
              {/* Add more quiz types as needed */}
            </select>
          </div>

          <div className="form-group">
            <label>Difficulty</label>
            <select
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
            >
              <option value="">Select Difficulty</option>
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>

          <div className="form-group">
            <label>Number of Questions</label>
            <input
              type="number"
              placeholder="Enter number of questions"
              value={numQuestions}
              onChange={(e) => setNumQuestions(parseInt(e.target.value, 10))}
            />
          </div>
        </div>

        <div className="form-group">
          <label>Text Input</label>
          <input
            type="text"
            placeholder="Enter text input"
            value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
          />
        </div>

        {/* Use a button to trigger the form submission */}
        <button type="button" onClick={generateQuiz}>
          Generate
        </button>
      </form>
    </div>
  );
};

// Main App component with routing
const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quiz-results" element={<QuizResult />} />
      </Routes>
    </Router>
  );
};

export default App;
