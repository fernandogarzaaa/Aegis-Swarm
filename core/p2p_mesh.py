import subprocess
import os

class DistributedMesh:
    def __init__(self):
        self.engine_path = os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)
        
    def start_node(self):
        print("[Exo] Starting local inference node...")
        cmd = ["python", "-m", "exo.node"]
        self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Node active. Waiting for peers..."
