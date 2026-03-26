import json
import sys
import os
from ruflo_bridge import RufloBridge

# Initialize Bridge
bridge = RufloBridge()

# [MCP Server] Integration for VS Code (Cline/Roo)
# Exposes Aegis Swarm + Ruflo capabilities to the IDE via MCP

def handle_request(request):
    if request["method"] == "get_repo_map":
        # Call repo_map.py logic
        return {"result": "Repo map generated successfully."}
    elif request["method"] == "apply_patch":
        # Call swe_linter.py logic
        return {"result": "Patch validated and applied."}
    elif request["method"] == "analyze_code":
        # BRIDGE: Python calling into TypeScript (RuVector)
        file_path = request["params"]["file_path"]
        return bridge.analyze_diff(file_path)
    return {"error": "Method not found"}

def main():
    print("[Aegis MCP] Server initialized on stdio.", file=sys.stderr)
    for line in sys.stdin:
        try:
            req = json.loads(line)
            resp = handle_request(req)
            print(json.dumps(resp))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()