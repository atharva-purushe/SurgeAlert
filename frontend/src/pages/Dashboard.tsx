import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { getSurgePrediction, getCapacity, runAgents, getSignals, askRouterBot } from "../lib/api";
import SurgeRadar from "../components/dashboard/SurgeRadar";
import Countdown from "../components/dashboard/Countdown";
import AQIChart from "../components/dashboard/AQIChart";
import HeatmapMap from "../components/dashboard/HeatmapMap";
import DriversCard from "../components/dashboard/DriversCard";
import CapacityGraph from "../components/dashboard/CapacityGraph";
import AgentsPanel from "../components/dashboard/AgentsPanel";
import RouterChat from "../components/dashboard/RouterChat";

export default function Dashboard() {
  const [surge, setSurge] = useState(null);
  const [capacity, setCapacity] = useState(null);
  const [signals, setSignals] = useState([]);
  const [agentsOut, setAgentsOut] = useState(null);
  const [loading, setLoading] = useState(true);

  // initial load
  useEffect(() => {
    const load = async () => {
      setLoading(true);
      try {
        const [s1, c1, sigs] = await Promise.all([
          getSurgePrediction(),
          getCapacity(),
          getSignals(200),
        ]);
        setSurge(s1);
        setCapacity(c1);
        // getSignals returns { data: [...] } or array depending on backend; handle both
        const rows = Array.isArray(sigs) ? sigs : (sigs?.data ?? []);
        setSignals(rows);
      } catch (err) {
        console.error("load error", err);
      } finally {
        setLoading(false);
      }
    };
    load();

    // poll every 20s for demo/live feel
    const id = setInterval(load, 20000);
    return () => clearInterval(id);
  }, []);

  const handleRunAgents = async () => {
    const out = await runAgents();
    setAgentsOut(out);
  };

  const handleAskRouter = async (msg) => {
    if (!msg) return { reply: "Please type symptoms." };
    const res = await askRouterBot(msg);
    return res;
  };

  return (
    <div className="min-h-screen bg-background text-foreground font-sans">
      <Navbar />
      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-3xl font-bold">SurgeShield — Dashboard</h1>
            <p className="text-sm text-muted-foreground">
              Live hospital surge intelligence — Mumbai demo
            </p>
          </div>
          <div className="text-sm text-muted-foreground">
            Last update: {signals[0] ? new Date(signals[0].created_at).toLocaleString() : "—"}
          </div>
        </div>

        {loading && (
          <div className="p-6 bg-white rounded-xl shadow text-center mb-6">Loading data…</div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* LEFT column */}
          <div className="space-y-6">
            <SurgeRadar surge={surge} />
            <Countdown surge={surge} />
            <AQIChart data={signals} />
            <DriversCard surge={surge} />
          </div>

          {/* CENTER column */}
          <div className="space-y-6">
            <CapacityGraph capacity={capacity} />
            <AgentsPanel agents={agentsOut} onRun={handleRunAgents} />
          </div>

          {/* RIGHT column */}
          <div className="space-y-6">
            <HeatmapMap points={signals} />
            <RouterChat askRouter={handleAskRouter} />
          </div>
        </div>
      </div>
    </div>
  );
}
