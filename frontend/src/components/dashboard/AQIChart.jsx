import React from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

export default function AQIChart({ data = [] }) {
  const formatted = data
    .slice(0, 120)
    .map((d) => ({
      time: new Date(d.created_at).toLocaleTimeString(),
      aqi: d.aqi ?? 0,
    }))
    .reverse();

  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-3">AQI (recent)</h3>
      <div style={{ width: "100%", height: 200 }}>
        <ResponsiveContainer>
          <LineChart data={formatted}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" minTickGap={20} />
            <YAxis domain={[0, "dataMax + 20"]} />
            <Tooltip />
            <Line type="monotone" dataKey="aqi" stroke="#6366f1" strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
