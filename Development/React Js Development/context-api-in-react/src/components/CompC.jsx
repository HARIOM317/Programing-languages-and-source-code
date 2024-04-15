import React from "react";
import { FirstName, LastName } from "../App";

// Now we are directly passing the data only CompC which is at the end of the hierarchy without passing CompA and CompB using context api. This is very lengthy way to achieve this. We have a better way or solution to do same thing.
// We can simplify this Consumer process using useState hooks (Check CompB.jsx)

// Using Context API
const CompC = () => {
  return (
    <>
      {/* Consumer - It requires a function */}

      {/* Consumer 1 */}
      <FirstName.Consumer>
        {(fName) => {
          return (
            // Consumer 2
            <LastName.Consumer>
              {(lName) => {
                return (
                  <h2>
                    My name is {fName} {lName}
                  </h2>
                );
              }}
            </LastName.Consumer>
          );
        }}
      </FirstName.Consumer>

      <h1>Component C</h1>
    </>
  );
};

export default CompC;
