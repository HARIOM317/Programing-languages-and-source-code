import Image from "next/image";
import styles from "./page.module.css";
import LearnLink from "@/components/LearnLink";
import LearnUseRouter from "@/components/LearnUseRouter";

export default function Home() {
  return (
    <>
      <main className={styles.main}>
        <h1>Hariom Singh Rajput</h1>
        <LearnLink />
        <LearnUseRouter />
      </main>
    </>
  );
}
 