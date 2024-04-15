import React from "react";
import Navbar from "../components/Navbar";

const AboutPage = () => {
  return (
    <>
      <Navbar />
      <div className="container">
        <h1 className="d-flex justify-content-center align-items-end fw-bold fs-1 m-5 text-danger">
          This is About Page
        </h1>
      </div>
    </>
  );
};

export default AboutPage;
