"use client";

import React from "react";
import { useRouter } from "next/navigation";

const OrderProduct = () => {
  const router = useRouter();

  const handleClick = () => {
    setTimeout(() => {
      alert("Order Placed Successfully!");
      router.push("/"); // to push specific page on stack
      //   router.replace("/"); // to replace the history
      // router.back(); // to navigate on previous page
      //   router.forward(); // to navigate forward to the next page
    }, 1000);
  };

  return (
    <div className="demo">
      <h1>Order Product</h1>
      <button
        onClick={handleClick}
        style={{
          border: "1.5px solid white",
          borderRadius: "6px",
          padding: "8px 16px",
          background: "gray",
        }}
      >
        Place Order
      </button>
    </div>
  );
};

export default OrderProduct;
