import React, { useState } from "react";

export default function TextForm(props) {
  const convertToUppercase = () => {
    setText(text.toUpperCase());
  };
  
  const convertToLowercase = () => {
    setText(text.toLowerCase());
  };

  const clearText = () => {
    setText("");
  };

  const handleOnChange = (event) => {
    setText(event.target.value);
  };

  const [text, setText] = useState("Enter text here");

  return (
    <>
      <div className="container">
        <h1>{props.heading}</h1>
        <div className="mb-3">
          <textarea
            className="form-control"
            id="exampleFormControlTextarea1"
            rows="5"
            value={text}
            onChange={handleOnChange}
          ></textarea>
        </div>

        <button className="btn btn-primary" onClick={convertToUppercase}>
          Convert to Uppercase
        </button>

        <button className="btn btn-primary mx-4" onClick={convertToLowercase}>
          Convert to Lowercase
        </button>
        
        <button className="btn btn-primary" onClick={clearText}>
          Clear Text
        </button>
      </div>

      <div className="container my-3">
        <h1>Your Text Summary</h1>
        <p>
          Total Words = {text.length === 0 ? text.length : text.split(" ").length} and Total Characters ={" "}
          {text.length}
        </p>
        <p>{0.008 * text.split(" ").length} Minutes to read</p>

        <div className="my-3">
          <h3>Preview</h3>
          <p>{text}</p>
        </div>
      </div>
    </>
  );
}
