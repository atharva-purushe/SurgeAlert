import React from "react";

export default function SurgeRadar({ surge }) {
  if (!surge) return <div className="p-6 bg-white rounded-xl shadow">Loading surge…</div>;

  const text = surge.llm_explanation || "";
  const level = (text.match(/Green|Yellow|Orange|Red|Black/i) || ["Unknown"])[0];
  const colors = {
    Green: "bg-green-400",
    Yellow: "bg-yellow-400",
    Orange: "bg-orange-500",
    Red: "bg-red-600",
    Black: "bg-slate-900 text-white",
    Unknown: "bg-gray-300",
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-3">Surge Level</h3>
      <div className="flex items-center gap-4">
        <div className={` px-4 w-28 h-28 rounded-full flex items-center justify-center ${colors[level]}`}>
          <span className="text-xl font-bold">{level}</span>
        </div>
        <div className="text-sm">
          <div><strong>Factor:</strong> {surge.numeric_prediction?.surge_factor ?? "—"}</div>
          <div className="mt-2 text-xs text-muted-foreground">{(surge.llm_explanation || "").slice(0, 220)}</div>
        </div>
      </div>
    </div>
  );
}
