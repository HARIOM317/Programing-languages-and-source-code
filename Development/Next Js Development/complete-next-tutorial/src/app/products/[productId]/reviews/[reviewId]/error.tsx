"use client";

export default function ErrorBoundary({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="demo">
      <h2 style={{ color: "gold" }}>{error.message}</h2>

      <button onClick={reset}>Try again</button>
    </div>
  );
}
