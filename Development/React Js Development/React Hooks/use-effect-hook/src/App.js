import React, { useState, useEffect } from "react";

const App = () => {
  const [num, setNum] = useState(0);
  const [num2, setNum2] = useState(0);
  const [count, setCount] = useState(0);

  // It will call automatically every time when render method is called

  // It will call every time when the value of count will be update.

  // If I pass an empty array [] in useEffect instant of count then it will call only first time during render method calling 
  useEffect(() => {
    document.title = `You clicked ${count} times`;
    alert(`You clicked ${count} times`);
  }, [count]);

  return (
    <>
      <div className="container">
        {/* button 1 */}
        <button
          onClick={() => {
            setNum(num + 1);
            setCount(count + 1);
          }}
        >
          Click Me - {num}
        </button>

        {/* button 2 */}
        <button
          onClick={() => {
            setNum2(num2 + 1);
            setCount(count + 1);
          }}
        >
          Click Me - {num2}
        </button>
      </div>
    </>
  );
};

export default App;
