import React from "react";
import "./index.css";
import { useState } from "react";

const App = () => {
  const [name, setName] = useState();
  const [myName, showName] = useState();

  const inputEvent = (event) => {
    setName(event.target.value);
  };

  const inputSubmit = () => {
    showName(name);
  };

  return (
    <>
      <div>
        <h1>Hello 🖐️ {myName}</h1>
        <input
          type="text"
          placeholder="Enter Your Name"
          onChange={inputEvent}
          value={name}
        />
        <button onClick={inputSubmit}>Submit</button>
      </div>
    </>
  );
};

export default App;
