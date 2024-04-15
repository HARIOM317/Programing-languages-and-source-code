import React, {useState} from 'react';
import './index.css';

const App = () => {
  // Hook
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  const GetTime = () => {
    setTime(new Date().toLocaleTimeString());
  }
  
  const GetDate = () => {
    setTime(new Date().toLocaleDateString());
  }

  return (
    <>
    <div>
      <h1>{time}</h1>
      <button onClick={GetTime}>Get Time</button>
      <button onClick={GetDate}>Get Date</button>
    </div>
    </>
  );
}

export default App;