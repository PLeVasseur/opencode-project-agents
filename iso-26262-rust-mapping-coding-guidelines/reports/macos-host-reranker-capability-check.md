# macOS Host Capability + Reranker Benchmark Commands

Run these commands on the macOS host to determine whether moving from the Ubuntu x86_64 VM to native macOS aarch64 is a good acceleration path.

## 1) Capability Snapshot

```bash
sw_vers
uname -m
sysctl -n machdep.cpu.brand_string
sysctl -n hw.physicalcpu
sysctl -n hw.logicalcpu
sysctl -n hw.memsize
```

## 2) Torch Backend Availability (run from repo root)

```bash
uv run python - <<'PY'
import platform, torch
print("platform:", platform.platform())
print("machine:", platform.machine())
print("torch:", torch.__version__)
print("cuda_available:", torch.cuda.is_available())
print("mps_built:", torch.backends.mps.is_built())
print("mps_available:", torch.backends.mps.is_available())
PY
```

## 3) Quick Reranker Benchmark (64 docs; CPU vs MPS if available)

```bash
uv run python - <<'PY'
import time, torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "BAAI/bge-reranker-v2-m3"
query = "How should Rust code handle defensive error paths safely?"
passage = (
    "Rust defensive error handling uses Result and Option, explicit propagation, "
    "bounded retries, and clear invariants. " * 80
)
pairs = [(query, passage) for _ in range(64)]

tok = AutoTokenizer.from_pretrained(model_id)
devices = ["cpu"] + (["mps"] if torch.backends.mps.is_available() else [])

for device in devices:
    print(f"\n=== device={device} ===")
    model = AutoModelForSequenceClassification.from_pretrained(model_id).to(device).eval()
    for max_len in (512, 1024):
        try:
            enc = tok(pairs, padding=True, truncation=True, max_length=max_len, return_tensors="pt")
            seq_len = int(enc["input_ids"].shape[1])
            enc = {k: v.to(device) for k, v in enc.items()}
            with torch.inference_mode():
                _ = model(**enc).logits
                if device == "mps":
                    torch.mps.synchronize()
                t0 = time.perf_counter()
                _ = model(**enc).logits
                if device == "mps":
                    torch.mps.synchronize()
                dt = time.perf_counter() - t0
            print(f"max_len={max_len} seq_len={seq_len} infer_s={dt:.3f}")
        except Exception as exc:
            print(f"max_len={max_len} ERROR: {type(exc).__name__}: {exc}")
PY
```

## What to Return

Paste the complete outputs from sections 1-3. That is enough to decide whether to prioritize host migration (macOS + MPS) or stay on VM and optimize reranker workload/backends first.
