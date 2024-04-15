import React from 'react';
import ReactDOM from 'react-dom';

// render() - to show something on web page
// render() - It has 3 parameters (1. What to show, 2. Where to show, 3. Callback function)
ReactDOM.render(
  <h1>Hello World!</h1>, //What to Show?
  document.getElementById('root'), //Where To Show?
  () => console.log("Component Rendered") //Callback Function
)