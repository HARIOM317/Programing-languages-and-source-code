import Link from "next/link";

export default function F1() {
  return (
    <>
      <div className="demo">
        <h1>F1 Page</h1>
        <div>
          <Link href={"/f1/f2"}>F2</Link>
        </div>
      </div>
    </>
  );
}
