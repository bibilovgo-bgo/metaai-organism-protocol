"""FastAPI reference demo.

    uvicorn src.metaai_core.app:app --reload
    open http://127.0.0.1:8000

Shows the event bus, three demo agents, the decision ledger and the human gate
working together — on mock data, with no API keys.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .organism import Organism

app = FastAPI(title="METAai Organism Protocol — reference demo", version="0.1.0")
org = Organism()


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/events")
def events() -> list[dict]:
    return org.bus.recent()


@app.get("/decisions")
def decisions() -> list[dict]:
    return org.ledger.all()


@app.post("/tick")
def tick() -> dict:
    org.tick()
    return {"ok": True, "events": org.bus.recent(5)}


@app.post("/decisions/{decision_id}/approve")
def approve(decision_id: int) -> dict:
    return org.approve(decision_id)


@app.post("/decisions/{decision_id}/reject")
def reject(decision_id: int, wont_do: bool = False) -> dict:
    return org.reject(decision_id, wont_do=wont_do)


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return _DASHBOARD


_DASHBOARD = """<!doctype html><meta charset=utf-8>
<title>METAai Organism — reference demo</title>
<style>
  body{background:#0a0e16;color:#e8f5fc;font:14px/1.5 system-ui;margin:0;padding:24px}
  h1{font-size:18px;color:#2bd4ff} h2{font-size:13px;color:#8297a8;text-transform:uppercase;letter-spacing:1px}
  button{background:#10212e;color:#2bd4ff;border:1px solid #2bd4ff44;border-radius:6px;padding:6px 12px;cursor:pointer}
  .row{border-bottom:1px solid #ffffff14;padding:6px 0}
  .pending{color:#ffad3d} .approved{color:#36d99a} .rejected{color:#ff5364}
  .cols{display:grid;grid-template-columns:1fr 1fr;gap:24px}
  code{color:#8297a8}
</style>
<h1>METAai — Organism Protocol (reference demo)</h1>
<p><button onclick=tick()>▶ tick (sense → reason → propose)</button> &nbsp;<code>mock data, no keys</code></p>
<div class=cols>
  <div><h2>Decisions (human gate)</h2><div id=decisions></div></div>
  <div><h2>Event bus</h2><div id=events></div></div>
</div>
<script>
async function refresh(){
  const d = await (await fetch('/decisions')).json();
  document.getElementById('decisions').innerHTML = d.slice().reverse().map(r=>
    `<div class=row><b>#${r.id}</b> ${r.title} <span class=${r.status}>[${r.status}]</span>
     <br><code>conf ${r.confidence} — ${r.rationale}</code>
     ${r.status==='pending'?`<br><button onclick="act(${r.id},'approve')">✓ approve</button>
       <button onclick="act(${r.id},'reject')">✕ reject</button>`:''}</div>`).join('') || '<code>none yet — click tick</code>';
  const e = await (await fetch('/events')).json();
  document.getElementById('events').innerHTML = e.map(x=>
    `<div class=row><code>${x.ts.slice(11,19)}</code> <b>${x.type}</b> <code>[${x.source}]</code></div>`).join('') || '<code>none yet</code>';
}
async function tick(){ await fetch('/tick',{method:'POST'}); refresh(); }
async function act(id,a){ await fetch(`/decisions/${id}/${a}`,{method:'POST'}); refresh(); }
refresh();
</script>
"""
