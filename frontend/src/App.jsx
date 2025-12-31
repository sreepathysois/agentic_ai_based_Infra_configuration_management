import { useState } from "react";
import { api } from "./api";

export default function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runQuery = async () => {
    setLoading(true);
    const res = await api.post("/run", { query });
    setResult(res.data);
    setLoading(false);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>🧠 Infra AI Agent</h2>

      <textarea
        rows="3"
        style={{ width: "100%" }}
        placeholder="Install nginx on all ubuntu web servers"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={runQuery} disabled={loading}>
        {loading ? "Running..." : "Run"}
      </button>

      {result && (
        <>
          <h3>Intent</h3>
          <pre>{result.intent}</pre>

          <h3>Plan</h3>
          <pre>{JSON.stringify(result.plan, null, 2)}</pre>

          <h3>Playbook</h3>
          <pre>{result.playbook_yaml}</pre>

          <h3>Dry Run</h3>
          <pre>{result.dry_run_output}</pre>

          <h3>Execution</h3>
          <pre>{result.execution_output}</pre>

          <h3>Status</h3>
          <b>{result.status}</b>
        </>
      )}
    </div>
  );
}

