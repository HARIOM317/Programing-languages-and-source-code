import React from "react";
import Card from "./components/Card";
import SData from "./components/SData";
import "./index.css";

// function to return card using Card component
const netflixCard = (value) => {
  return (
    <Card
      imgSrc={value.imgSrc}
      category={value.category}
      title={value.title}
      link={value.link}
    />
  );
};

const App = () => {
  return (
    <>
      <h1 className="heading-style">List of top 5 Netflix Series in 2023</h1>

      {/* Mapping all data from SData component using netflixCard function */}
      {SData.map(netflixCard)}
    </>
  );
};

export default App;
