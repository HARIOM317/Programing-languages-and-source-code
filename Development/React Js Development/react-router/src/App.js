import React from "react";
import HomePage from "./pages/HomePage";
import { Routes, Route } from "react-router-dom";
import AboutPage from "./pages/AboutPage";
import ServicePage from "./pages/ServicePage";
import ContactPage from "./pages/ContactPage";
import ErrorPage from "./pages/ErrorPage";

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" Component={HomePage} />
        <Route path="/about" Component={AboutPage} />
        <Route path="/service" Component={ServicePage} />
        <Route path="/contact" Component={ContactPage} />
        <Route path="*" Component={ErrorPage} />
      </Routes>
    </>
  );
};

export default App;
