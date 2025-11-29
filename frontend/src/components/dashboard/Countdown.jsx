import React from "react";

export default function Countdown({ surge }) {
  if (!surge) return <div className="p-6 bg-white rounded-xl shadow">Loading countdown…</div>;

  const text = surge.llm_explanation || "";
  const match = text.match(/(\d+\s?(hours|hour|days|day|minutes|minute))/gi);
  const time = match ? match.join(", ") : "Estimate not available";

  return (
    <div className="p-6 bg-white rounded-xl shadow text-center">
      <h3 className="font-semibold mb-2">Time to Peak</h3>
      <div className="text-2xl font-bold text-primary">{time}</div>
    </div>
  );
}
