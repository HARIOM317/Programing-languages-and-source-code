import Link from "next/link";

export default function Home() {
  return (
    <div className="demo">
      <h1>Welcome Home!</h1>
      <Link href={"/blog"}>Blogs</Link>
      <Link href={"/products"}>Products</Link>
      <Link href={"/order-product"}>Order Product</Link>
    </div>
  );
}
