from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Cyber Threat Demo API", version="1.0.0")

class Flow(BaseModel):
    duration: float = Field(0, ge=0)
    total_fwd_packets: float = Field(0, ge=0)
    total_backward_packets: float = Field(0, ge=0)
    total_length_fwd_packets: float = Field(0, ge=0)
    total_length_bwd_packets: float = Field(0, ge=0)
    flow_bytes_per_second: float = Field(0, ge=0)
    flow_packets_per_second: float = Field(0, ge=0)
    syn_flag_count: float = Field(0, ge=0)
    rst_flag_count: float = Field(0, ge=0)
    packet_length_mean: float = Field(0, ge=0)

def score(f: Flow):
    s, reasons = 0.0, []
    if f.syn_flag_count > 20: s += .25; reasons.append("high SYN activity")
    if f.rst_flag_count > 10: s += .15; reasons.append("high RST activity")
    if f.flow_packets_per_second > 1000: s += .25; reasons.append("very high packet rate")
    if f.flow_bytes_per_second > 1e7: s += .15; reasons.append("very high byte rate")
    if f.total_backward_packets > max(1, f.total_fwd_packets * 5): s += .10; reasons.append("strongly asymmetric flow")
    if f.packet_length_mean < 40 and f.flow_packets_per_second > 500: s += .10; reasons.append("small packets at high rate")
    s = min(s, 1.0)
    label = "HIGH_RISK" if s >= .55 else "MEDIUM_RISK" if s >= .25 else "LOW_RISK"
    return label, round(s, 3), reasons

@app.get("/health")
def health():
    return {"status": "ok", "model_mode": "explainable-demo"}

@app.post("/predict")
def predict(flow: Flow):
    label, risk, reasons = score(flow)
    return {"prediction": label, "risk_score": risk, "reasons": reasons,
            "note": "Fallback screening mode. Use trained artifacts for research-model inference."}
