import os
import subprocess
import json

class OmniParserVision:
    def __init__(self):
        self.engine_path = os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)
        self.weights_path = os.path.join(self.engine_path, "weights", "icon_detect", "model.pt")
        
    def capture_screen(self):
        # Calls the actual OmniParser local inference
        cmd = ["python", os.path.join(self.engine_path, "parse_screen.py"), "--weights", self.weights_path]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return json.loads(result.stdout)
        except Exception as e:
            return {"error": str(e), "status": "Engine compiling or weights missing"}
