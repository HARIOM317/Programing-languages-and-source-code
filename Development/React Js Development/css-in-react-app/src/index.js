import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const heading = {
    color: 'red',
    textAlign: 'center',
    textTransform: 'capitalize',
    fontWeight: 'bold',
    fontFamily: 'Josefin Sans, sans-serif',
    margin: '20px',
    fontSize: '40px',
}

ReactDOM.render(
  <>
    {/* Inline CSS */}
    <h1 style={heading}>CSS in JSX</h1>

    {/* Inline CSS */}
    <p style={{color : 'green', textTransform: 'capitalize', fontSize: '20px', textAlign: 'center'}}>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odio vero id, nulla doloremque libero sapiente commodi, minus nihil suscipit iste porro, voluptatem repudiandae eligendi tempore rem ut delectus dignissimos minima.</p>

    {/* External CSS */}
    <div className="rounded-img">
      <img
        src="https://source.unsplash.com/600x400/?mobile"
        alt="Mobile Phone"
      />
    </div>
  </>,

  document.getElementById("root")
);