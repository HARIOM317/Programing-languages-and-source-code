import React from 'react';
import ReactDOM from 'react-dom';

const fname = "Hariom";
const mname = "Singh";
const lname = "Rajput";

const dateTime = new Date();

const date = dateTime.toLocaleDateString();
const time = dateTime.toLocaleTimeString();


ReactDOM.render(
  <>
  <h1>Hello, My name is {`${fname} ${mname} ${lname}`}</h1>
  <p>Today's date is: {date}</p>
  <p>Current Time is: {time}</p>

  </>,
  document.getElementById('root')
)