import React from "react";

export default function AgentsPanel({ agents, onRun }) {
  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold">AI Agents</h3>
        <button onClick={onRun} className="px-3 py-2 bg-primary text-white rounded">Run</button>
      </div>

      <div className="mt-4 text-sm">
        {!agents && <div className="text-muted-foreground">No agent outputs yet. Click Run.</div>}
        {agents && (
          <div className="space-y-3 text-xs">
            <div><strong>Surge:</strong><div className="mt-1">{agents.surge_explainer}</div></div>
            <div><strong>Staffing:</strong><div className="mt-1">{agents.resource_planner}</div></div>
            <div><strong>Procurement:</strong><div className="mt-1">{agents.procurement}</div></div>
            <div><strong>Deflection:</strong><div className="mt-1">{agents.deflection}</div></div>
          </div>
        )}
      </div>
    </div>
  );
}
