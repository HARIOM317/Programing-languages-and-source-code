import { Inter } from "next/font/google";
import "./globals.css";
import { Metadata } from "next";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    absolute: "Next.js Tutorial | GitNexa",
    default: "Next Js Tutorial",
    template: "%s | GitNexa",
  },
  description: "Let's learn next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  );
}
