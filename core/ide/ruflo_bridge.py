import subprocess
import json
import os

class RufloBridge:
    """
    [BRIDGE: PYTHON -> RUFLO (TS/NODE)]
    Aegis Swarm uses this bridge to leverage the advanced AST analysis 
    and vector diff classifiers found in the 'ruflo' framework.
    """
    def __init__(self):
        self.node_path = "node" # Ensure node is in PATH
        self.ruflo_root = os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)

    def analyze_diff(self, file_path):
        # Calls the RuVector AST-Analyzer
        # We target the index.ts of the AST-analyzer module
        script = os.path.join(self.ruflo_root, "src", "ruvector", "index.ts")
        
        # We assume ts-node or similar is installed or we use a transpiled version
        cmd = ["npx", "ts-node", script, "--analyze", file_path]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.ruflo_root)
            return json.loads(result.stdout)
        except Exception as e:
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    bridge = RufloBridge()
    # Test bridge on a sample file
    print(bridge.analyze_diff(os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)))
