import React, { useState } from "react";
import "./index.css";

const App = () => {
  let currTime = new Date().toLocaleTimeString();

  const [time, setTime] = useState(currTime);

  setInterval(() => {
    currTime = new Date().toLocaleTimeString();
    setTime(currTime);
  }, 1000);

  return (
    <>
      <div>
        <h1>{time}</h1>
      </div>
    </>
  );
};

export default App;
