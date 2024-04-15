// JSX - Java Script Extension (XML)
import React from "react";
import ReactDOM from "react-dom";

// First Way to render HTML elements (Recommended - By using JSX)
ReactDOM.render(<h1>Hariom Singh Rajput</h1>, document.getElementById("root"));

// Second way - Actual code of render on browser (It is done by babel)

// ReactDOM.render(
//   React.createElement("h1", null, "Hariom Singh Rajput"),
//   document.getElementById("root")
// );

// Third way - Without JSX
var h1 = document.createElement("h1");
h1.innerHTML = "Hariom Singh Rajput";
document.getElementById("root").appendChild(h1);
