import React from "react";
import "./index.css";
import SlotMachine from "./SlotMachine";

const App = () => {
  return (
    <>
      <h1 className="heading-style">
        {" "}
        🎰 Welcome to{" "}
        <span style={{ fontWeight: "bold", backgroundColor: "#fff" }}>
          {" "}
          Slot Machine Game{" "}
        </span>{" "}
        🎰{" "}
      </h1>

      <div className="slot-machine">
        <SlotMachine x="😄" y="😄" z="😄" />
        <SlotMachine x="🔥" y="😄" z=" 🔔 " />
        <SlotMachine x="🔔" y="🔔" z="🔔" />
      </div>
    </>
  );
};

export default App;
