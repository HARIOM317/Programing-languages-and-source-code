import React from "react";
import Link from "next/link";

const ProductList = () => {
  return (
    <div className="demo">
      <Link href={"/"}>Home</Link>
      <h1>Product List</h1>
      <h2>
        <Link href={"products/product1"} replace>Product 1</Link>
      </h2>
      <h2>
        <Link href={"products/product2"}>Product 2</Link>
      </h2>
      <h2>
        <Link href={"products/product3"}>Product 3</Link>
      </h2>
    </div>
  );
};

export default ProductList;
