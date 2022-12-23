import './App.css';
import HomePage from './Pages/HomePage';
import {BrowserRouter as Router,Routes, Route } from "react-router-dom";
import ApiPage from './Pages/ApiPage';
import Gist from './Pages/Gist';
import Gmail from './Pages/Gmail'
import ScrollToTop from './Components/ScrollToTop'

function App() {
  return (
      <Router> 
       <ScrollToTop />
        <div className="App">
          
            <Routes>
                <Route path="/"  element={<HomePage/>} exact  />
                <Route path="/api" element={<ApiPage/>} exact />
                <Route path="/gist" element={<Gist/>} exact />
                <Route path="/gmail" element={<Gmail/>} exact />
            </Routes>
          
        </div>
      </Router>
  );
}

export default App;
