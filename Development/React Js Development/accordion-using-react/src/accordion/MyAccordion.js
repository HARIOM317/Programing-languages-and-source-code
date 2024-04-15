import React, { useState } from "react";

const MyAccordion = ({question, answer}) => {
    const [show, setShow] = useState(false);
  return (
    <>
      <div className="main-heading">
        <p onClick={() => setShow(!show)}>{show ? "➖" : "➕"}</p>
        <h3>{question}</h3>
      </div>
      {/* If show is true then show the answer */}
      {show && <p className="answer">{answer}</p>}
    </>
  );
};

export default MyAccordion;
