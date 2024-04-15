import React from "react";
import CompA from "./components/CompA";
import { createContext } from "react";

// Context
const FirstName = createContext();
const LastName = createContext(); 

const App = () => {
  return (
    <>
      {/* Provider */}
      <FirstName.Provider value={"Hariom"}>
        <LastName.Provider value={"Rajput"}>
          <CompA />
        </LastName.Provider>
      </FirstName.Provider>
    </>
  );
};

export default App;
export { FirstName, LastName };
