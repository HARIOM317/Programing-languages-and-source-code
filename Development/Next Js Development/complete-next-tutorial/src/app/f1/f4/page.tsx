import Link from "next/link";

export default function F4() {
  return (
    <div className="demo">
      <h1>F4 Page</h1>
      <div>
        <Link href={"/f1/f3"}>F3</Link>
        <hr />
        <Link href={"/about"}>About</Link>
      </div>
    </div>
  );
}
