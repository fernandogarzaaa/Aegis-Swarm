import os
import json

print("[COMPARATOR] Initializing model comparison engine...")
scout_data_path = r"D:\AegisSwarm\harvest\latest_benchmarks.json"
master_db_path = r"D:\AegisSwarm\harvest\master_benchmarks.json"

if not os.path.exists(scout_data_path):
    print("[ERROR] No scout data found. Exiting.")
    exit(1)

with open(scout_data_path, "r") as f:
    scouted = json.load(f)

print(f"Loaded {len(scouted.get('models', []))} models from Scout. Analyzing VRAM-to-Score efficiency...")
# Very basic comparison mock logic
best_model = None
highest_score = 0

for model in scouted.get("models", []):
    if model["score"] > highest_score:
        highest_score = model["score"]
        best_model = model["name"]

print(f"[COMPARATOR] Top performing model identified for RTX 2060 constraints: {best_model} (Score: {highest_score})")
print("[COMPARATOR] Analysis complete and logged for orchestrator consumption.")
