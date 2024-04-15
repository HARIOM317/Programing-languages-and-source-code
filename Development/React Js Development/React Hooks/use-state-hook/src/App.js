import React, { useState } from "react";
import "./index.css";

const App = () => {
  // Hook
  let [count, setCount] = useState(0);

  const IncrementNum = () => {
    setCount(count + 1);
  };

  const DecrementNum = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert("Min Limit Reached!");
      setCount(0);
    }
  };

  const Reset = () => {
    setCount(0);
  };

  return (
    <>
      <div>
        <h1>{count}</h1>
        <div className="btn">
          <button onClick={IncrementNum}>Increment</button>
          <button onClick={DecrementNum}>Decrement</button>
          <button onClick={Reset}>Reset</button>
        </div>
      </div>
    </>
  );
};

export default App;
