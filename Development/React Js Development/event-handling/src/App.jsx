import React from "react";
import "./index.css";
import { useState } from "react";

const App = () => {
  // Hooks using array destructuring
  const [bg, setBg] = useState("#eec9aa");
  const [data, setData] = useState();
  const [color, setColor] = useState();
  const [text, setText] = useState();

  const updateScreen = () => {
    setBg("#8e44ad");
    setColor("white");

    if (data == "Yum 😋") {
      setData("Wow 🫨");
    } else {
      setData("Yum 😋");
    }
  };

  const backBg = () => {
    setBg("#eec9aa");
    setColor("brown");
  };

  const setScreenText = () => {
    setText("👧 Chhodo mujhe jano do");
  };

  const removeScreenText = () => {
    setText("");
  };

  return (
    <>
      <div style={{ backgroundColor: bg }}>
        <h1 style={{ backgroundColor: bg, color: color }}>{data}</h1>
        {/* onClick event, onDoubleClick event etc. */}
        <button
          onClick={updateScreen}
          onDoubleClick={backBg}
          onMouseEnter={setScreenText}
          onMouseLeave={removeScreenText}
        >
          Click Me
        </button>
        <h2 style={{ backgroundColor: bg, color: color }}>{text}</h2>
      </div>
    </>
  );
};

export default App;
