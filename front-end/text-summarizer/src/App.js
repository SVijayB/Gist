import './App.css';
import { FileUpload } from './FileUpload';
import { useState } from 'react';

function App() {

  const [fileData, setFileData] = useState({
    fileName: '',
    fileType: ''
  });

  const [inputType, setInputType] = useState('1');

  return (
    <div className="App">

      <select onChange={(e) => setInputType(e.target.value)}>
        <option value="1">Text</option>
        <option value="2">Image</option>
        <option value="3">PDF</option>
        <option value="4">Doc</option>
      </select>


      <label htmlFor="url">URL</label>
      <input type="text" id='url' name='url' />

      <label>Image</label>
      <FileUpload />

      {/* <button onClick={() => {
        if (inputType === '1') {
          axios.get(`http://127.0.0.1:5000/api/summarize?type={1,2,3,4}&link=OBJECT_LOCATION */}

    </div>
  );
}

export default App;
