import React from "react";
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

export default function CapacityGraph({ capacity }) {
  if (!capacity) return <div className="p-6 bg-white rounded-xl shadow">Loading capacity…</div>;

  const data = [
    { name: "Current", beds: capacity.current_load?.beds ?? 0, icu: capacity.current_load?.icu ?? 0 },
    { name: "Predicted", beds: capacity.predicted_load?.beds ?? 0, icu: capacity.predicted_load?.icu ?? 0 },
  ];

  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-3">Capacity (Beds / ICU)</h3>
      <div style={{ width: "100%", height: 240 }}>
        <ResponsiveContainer>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="beds" stroke="#06b6d4" strokeWidth={3} />
            <Line type="monotone" dataKey="icu" stroke="#f97316" strokeWidth={3} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
