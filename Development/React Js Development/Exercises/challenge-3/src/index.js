import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

let currDate = new Date();
currDate = currDate.getHours();
let greet;

const cssStyle = { };


if(currDate >= 1 && currDate < 12){
  greet = "Good Morning";
  cssStyle.color = 'green';
} else if(currDate >= 12 && currDate < 17){
  greet = "Good Afternoon";
  cssStyle.color = "orange";
} else {
  greet = "Good Evening";
  cssStyle.color = "aqua";
}


ReactDOM.render(
  <>
    <div>
      <h1 style={{color: 'white'}}>
        Hello Sir, <span style={cssStyle}>{greet}</span>
      </h1>
    </div>
  </>,

  document.getElementById("root")
);