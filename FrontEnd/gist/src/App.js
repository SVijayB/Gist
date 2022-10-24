import './App.css';
import HomePage from './Pages/HomePage';
import {BrowserRouter as Router,Routes, Route } from "react-router-dom";
import ApiPage from './Pages/ApiPage';


function App() {
  return (
      <Router> 
        <div className="App">
          
            <Routes>
                <Route path="/"  element={<HomePage/>} exact  />
                <Route path="/api" element={<ApiPage/>} exact />
            </Routes>
          
        </div>
      </Router>
  );
}

export default App;
