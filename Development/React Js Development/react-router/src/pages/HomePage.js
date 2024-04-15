import React from "react";
import Navbar from "../components/Navbar";

const HomePage = () => {
  return (
    <>
      <Navbar />
      <div className="container">
        <h1 className="d-flex justify-content-center align-items-end fw-bold fs-1 m-5 text-primary">This is Home Page</h1>
      </div>
    </>
  );
};

export default HomePage;
