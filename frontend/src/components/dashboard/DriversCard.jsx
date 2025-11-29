import React from "react";

export default function DriversCard({ surge }) {
  if (!surge) return <div className="p-6 bg-white rounded-xl shadow">Loading drivers…</div>;
  const text = surge.llm_explanation || "";
  // try extract "AQI: 42%, Festival: 31%" like parts
  const drivers = text.match(/([A-Za-z ]+:\s*\d+%)/g) || [];

  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-3">Top Drivers</h3>
      <ul className="space-y-2">
        {drivers.length ? drivers.map((d, i) => (
          <li key={i} className="text-sm bg-muted p-2 rounded">{d}</li>
        )) : <li className="text-sm text-muted-foreground">Drivers not parsed — see explanation card.</li>}
      </ul>
      <div className="mt-3 text-xs text-muted-foreground">
        {(!drivers.length) && (surge.llm_explanation?.slice(0, 180) ?? "")}
      </div>
    </div>
  );
}
