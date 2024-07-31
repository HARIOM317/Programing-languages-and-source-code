import React from "react";
import { Metadata } from "next";

type Props = {
  params: {
    productId: string;
  };
};

// for dynamic metadata heading & description for SEO of dynamic pages
export const generateMetadata = async ({
  params,
}: Props): Promise<Metadata> => {
  const title = await new Promise((resolve) => {
    setTimeout(() => {
      resolve(`${params.productId}`);
    }, 100);
  });
  return {
    title: `Product ${title}`,
    description: `This is description for ${params.productId}`,
  };
};

const ProductDetail = ({ params }: Props) => {
  return (
    <div className="demo">
      <h2>This is Detail about Product {params.productId}</h2>
    </div>
  );
};

export default ProductDetail;
