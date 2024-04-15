import React from "react";

const SlotMachine = (props) => {
  let {x, y, z} = props;

  if (x === y && x === z) {
    return (
      <>
        <div>
          <h1 className="slot-inner">{`${x} ${y} ${z}`}</h1>
          <h2 className="slot-outer">This is Matching</h2>
          <hr />
        </div>
      </>
    );
  } else {
    return (
      <>
        <div>
          <h1 className="slot-inner">{`${x} ${y} ${z}`}</h1>
          <h2 className="slot-outer">This is not Matching</h2>
          <hr />
        </div>
      </>
    );
  }
};

export default SlotMachine;
