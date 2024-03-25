import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import CoursePage from "./CoursePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/CoursePage" element={<CoursePage />} />
      </Routes>
    </Router>
  );
}

export default App;
