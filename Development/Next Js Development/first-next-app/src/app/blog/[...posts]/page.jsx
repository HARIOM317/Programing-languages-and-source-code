import React from "react";

const Posts = ({ params }) => {
  console.log(params);
  return <div>Post Item - {params.posts}</div>;
};

export default Posts;
