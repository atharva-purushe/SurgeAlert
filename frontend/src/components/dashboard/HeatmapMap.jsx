import React from "react";
import { MapContainer, TileLayer, CircleMarker, Tooltip } from "react-leaflet";

// simple color based on AQI
function aqiColor(aqi = 0) {
  if (aqi <= 50) return "#50f0e6";
  if (aqi <= 100) return "#50ccaa";
  if (aqi <= 150) return "#f0e641";
  if (aqi <= 200) return "#ff8b3d";
  if (aqi <= 300) return "#ff3e3e";
  return "#7e0023";
}

export default function HeatmapMap({ points = [] }) {
  const center = [19.076, 72.8777]; // Mumbai center

  // If points have lat/lng use them; otherwise scatter around Mumbai center
  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-3">Mumbai AQI Map</h3>
      <div style={{ width: "100%", height: 300 }}>
        <MapContainer center={center} zoom={11} style={{ width: "100%", height: "100%" }}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          {points.slice(0, 80).map((p, i) => {
            const lat = p.lat ?? (19.076 + (Math.random() - 0.5) * 0.04);
            const lng = p.lng ?? (72.8777 + (Math.random() - 0.5) * 0.04);
            const color = aqiColor(p.aqi ?? 200);
            const radius = Math.min(5, Math.max(4, (p.aqi ?? 200) / 20));
            return (
              <CircleMarker key={i} center={[lat, lng]} radius={radius} pathOptions={{ color, fillColor: color, fillOpacity: 0.45 }}>
                <Tooltip>
                  <div style={{ fontSize: 12 }}>
                    <strong>{p.hospital_name ?? `Hospital ${p.hospital_id ?? ""}`}</strong><br />
                    AQI: {p.aqi ?? "—"}<br />
                    {p.created_at ? new Date(p.created_at).toLocaleString() : ""}
                  </div>
                </Tooltip>
              </CircleMarker>
            );
          })}
        </MapContainer>
      </div>
    </div>
  );
}
