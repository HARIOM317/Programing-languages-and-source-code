import React from "react";
import Navbar from "../components/Navbar";

const ErrorPage = () => {
  return (
    <>
      <Navbar />
      <div className="container">
        <h1 className="d-flex justify-content-center align-items-end fw-bold fs-1 m-5">
          Page Not Found
        </h1>
        <p className="text-center" >The page you are trying to access might have been removed or currently not available</p>
      </div>
    </>
  );
};

export default ErrorPage;
