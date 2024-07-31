"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

const navLinks = [
  { name: "Register", href: "/register" },
  { name: "Login", href: "/login" },
];

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const [input, setInput] = useState("");

  return (
    <>
      <div style={{ marginTop: "1rem" }}>
        {navLinks.map((link) => {
          const isActive = pathname.startsWith(link.href);

          return (
            <Link
              href={link.href}
              key={link.name}
              className={isActive ? "font-bold mr-4 text-red-300" : "mr-4"}
            >
              {link.name}
            </Link>
          );
        })}
      </div>

      {/* Input Field */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter Email"
          style={{
            background: "#1c212f",
            padding: "10px",
            borderRadius: "8px",
          }}
        />
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexDirection: "column",
          marginTop: "1.5rem",
          width: "100%",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            flexDirection: "column",
            padding: "1rem",
            width: "50%",
            border: "1px solid gray",
            background: "#1c212f",
          }}
        >
          <h3>Create Account or Login</h3>
        </div>
      </div>

      {children}
    </>
  );
}
