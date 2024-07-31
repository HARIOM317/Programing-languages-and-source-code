import React from "react";

const Header = () => {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "column",
        padding: "1rem",
        borderBottom: "1.5px solid gray",
        background: "#262626",
      }}
    >
      <p>This is Header</p>
    </div>
  );
};

export default Header;
