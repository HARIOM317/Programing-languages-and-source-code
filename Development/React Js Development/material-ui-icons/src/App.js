import React, { useState } from "react";
import "./index.css";

// Material Ui Components
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import RestartAltIcon from "@mui/icons-material/RestartAlt";
import Button from "@mui/material/Button";

const App = () => {
  // Hook
  let [count, setCount] = useState(0);

  const IncrementNum = () => {
    setCount(count + 1);
  };

  const DecrementNum = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert("Min Limit Reached!");
      setCount(0);
    }
  };

  const Reset = () => {
    setCount(0);
  };

  return (
    <>
      <div>
        <h1>{count}</h1>
        <div className="btn">
          {/* Using Material UI Button */}
          <Button
            onClick={IncrementNum}
            variant="contained"
            style={{ margin: "10px" }}
          >
            <AddIcon />
          </Button>
          <Button
            onClick={DecrementNum}
            variant="contained"
            style={{ margin: "10px" }}
          >
            <RemoveIcon />
          </Button>
          <Button
            onClick={Reset}
            variant="contained"
            style={{ margin: "10px" }}
          >
            <RestartAltIcon />
          </Button>
        </div>
      </div>
    </>
  );
};

export default App;
