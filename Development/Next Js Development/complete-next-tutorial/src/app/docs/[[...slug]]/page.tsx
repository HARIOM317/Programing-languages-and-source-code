import React from "react";

const Docs = ({ params }: { params: { slug: string[] } }) => {
  if (params.slug?.length === 2) {
    return (
      <div className="demo">
        <h2>
          Viewing docs for feature {params.slug[0]} and Concept {params.slug[1]}
        </h2>
      </div>
    );
  } else if (params.slug?.length === 1) {
    return (
      <div className="demo">
        <h2>Viewing docs for feature {params.slug[0]}</h2>
      </div>
    );
  }
  return (
    <div className="demo">
      <h1>Docs Home Page</h1>
    </div>
  );
};

export default Docs;
