from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 156.06,
    "uptime_pct": 98.813,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 120.06,
    "uptime_pct": 97.203,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 126.06,
    "uptime_pct": 97.544,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 129.52,
    "uptime_pct": 98.216,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 212.6,
    "uptime_pct": 98.346,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 208.87,
    "uptime_pct": 99.252,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 212.54,
    "uptime_pct": 98.133,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 134.56,
    "uptime_pct": 98.971,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 120.76,
    "uptime_pct": 97.196,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 189.1,
    "uptime_pct": 97.771,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 166.19,
    "uptime_pct": 97.585,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 218.52,
    "uptime_pct": 97.882,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 191.31,
    "uptime_pct": 97.606,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 146.56,
    "uptime_pct": 97.451,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 208.03,
    "uptime_pct": 99.455,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 124.22,
    "uptime_pct": 97.808,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 217.88,
    "uptime_pct": 98.972,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 185.66,
    "uptime_pct": 99.37,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 139.54,
    "uptime_pct": 97.314,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 107.46,
    "uptime_pct": 97.121,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 184.48,
    "uptime_pct": 99.155,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 219.02,
    "uptime_pct": 98.222,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 133.9,
    "uptime_pct": 98.69,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 194.99,
    "uptime_pct": 98.914,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 207.88,
    "uptime_pct": 99.135,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 215.87,
    "uptime_pct": 99.116,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 141.47,
    "uptime_pct": 97.196,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 165.23,
    "uptime_pct": 97.264,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 167.9,
    "uptime_pct": 97.675,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 156.45,
    "uptime_pct": 97.65,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 142.24,
    "uptime_pct": 98.802,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 213.72,
    "uptime_pct": 99.054,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 223.46,
    "uptime_pct": 98.84,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 226.66,
    "uptime_pct": 97.847,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 127.92,
    "uptime_pct": 97.883,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 121.1,
    "uptime_pct": 98.102,
    "timestamp": 20250312
  }
]
""")

async def calculate_latency(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]
        
        if not latencies:
            continue
            
        results.append({
            "region": region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime": round(float(np.mean(uptimes)), 3),
            "breaches": int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return Response(status_code=200, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*"
    })

app.post("/api/latency")(calculate_latency)
app.post("/")(calculate_latency)

handler = Mangum(app)