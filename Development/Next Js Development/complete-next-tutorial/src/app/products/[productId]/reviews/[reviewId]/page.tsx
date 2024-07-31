"use client";

import React from "react";
import { notFound } from "next/navigation";

function getRandomInt(count: number) {
  return Math.floor(Math.random() * count);
}

const ReviewDetail = ({
  params,
}: {
  params: { productId: string; reviewId: string };
}) => {
  const random = getRandomInt(2);

  if (random === 1 && parseInt(params.reviewId) <= 1) {
    throw new Error("Error loading review!");
  }

  if (parseInt(params.reviewId) > 1000) {
    notFound();
  }
  return (
    <div className="demo">
      <h2>
        Review {params.reviewId} for Product {params.productId}
      </h2>
    </div>
  );
};

export default ReviewDetail;
