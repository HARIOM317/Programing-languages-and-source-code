import React, { useState } from "react";
import { questions } from "../api";
import MyAccordion from "./MyAccordion";

const Accordion = () => {
    const [data, setData] = useState(questions);
  return (
    <>
      <section className="main-div">
        <h1>General Knowledge Questions</h1>
        {data.map((element) => {
          const { id } = element;
          return <MyAccordion key={id} {...element} />;
        })}
      </section>
    </>
  );
};

export default Accordion;
