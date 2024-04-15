import React from 'react';
import ReactDOM from 'react-dom';

const randomImage = "https://source.unsplash.com/400x400/?computers";

ReactDOM.render(
  <>
    <h1>JSX Attributes</h1>
    <p>
      JSX allows us to use attributes with the HTML elements just like we do
      with normal HTML. But instead of the normal naming convention of HTML, JSX
      uses the camelCase convention for attributes (className, src, alt, contentEditable etc.)
    </p>

    <img
      src={randomImage}
      alt="Random Computer"
    />
  </>,

  document.getElementById('root')
);