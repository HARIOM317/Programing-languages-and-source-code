import React from "react";
import { add, sub, pro, div } from "./Calc";

function App() {
  let a = 20;
  let  b = 3;

  return (
    <>
      <ul>
        <li>{`The Sum of ${a} and ${b} is : ${add(a, b)}`}</li>
        <li>{`The Subtraction of ${a} and ${b} is : ${sub(a, b)}`}</li>
        <li>{`The Product of ${a} and ${b} is : ${pro(a, b)}`}</li>
        <li>{`The Division of ${a} and ${b} is : ${div(a, b)}`}</li>
      </ul>
    </>
  );
}

export default App;
