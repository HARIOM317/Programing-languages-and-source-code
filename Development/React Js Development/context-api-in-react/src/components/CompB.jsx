import React, {useContext} from "react";
import CompC from "./CompC";
import { FirstName, LastName } from "../App";

// Using useState Hooks
const CompB = () => {
    // return <CompC />;

  const fName = useContext(FirstName);
  const lName = useContext(LastName);
  return (
    <h1>
      I am {fName} {lName}
    </h1>
  );
};

export default CompB;
