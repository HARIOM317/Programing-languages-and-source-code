import React from "react";

const MyBlogs = ({ params }) => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        margin: "2rem",
        padding: "2rem",
      }}
    >
      <h1 style={{ margin: "2rem", padding: "2rem" }}>
        My Blog - {params.post}
      </h1>
      <p style={{ width: "50%" }}>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt quia
        qui magnam libero ut. Repellendus vero repellat beatae ratione nihil
        laborum, temporibus quae sint quasi iure laudantium accusamus minus
        animi.
      </p>
    </div>
  );
};

export default MyBlogs;
