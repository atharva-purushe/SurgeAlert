import React, { useState } from "react";

export default function RouterChat({ askRouter }) {
  const [msg, setMsg] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!msg) return;
    setLoading(true);
    try {
      const r = await askRouter(msg);
      setReply(r.reply || JSON.stringify(r));
    } catch (e) {
      setReply("Error: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow">
      <h3 className="font-semibold mb-2">Patient Router</h3>
      <textarea value={msg} onChange={(e) => setMsg(e.target.value)}
        className="w-full p-2 border rounded-lg bg-muted" rows={3} placeholder="e.g., chest pain, breathless"/>
      <div className="flex gap-2 mt-2">
        <button onClick={send} className="px-3 py-2 bg-secondary text-white rounded">Ask AI</button>
        <button onClick={() => { setMsg(""); setReply(""); }} className="px-3 py-2 border rounded">Clear</button>
      </div>
      {loading && <div className="mt-2 text-sm text-muted-foreground">Thinking…</div>}
      {reply && <div className="mt-3 p-2 bg-muted rounded">{reply}</div>}
    </div>
  );
}
