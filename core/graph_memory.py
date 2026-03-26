import os
import subprocess

class GraphMemory:
    def __init__(self):
        self.engine_path = os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)
        
    def index_repository(self, repo_path):
        print(f"[GraphRAG] Indexing {repo_path} into 3D Graph...")
        cmd = ["python", "-m", "graphrag.index", "--root", repo_path]
        subprocess.Popen(cmd) # Run async
        return "Indexing started in background."
        
    def query_graph(self, topic, repo_path):
        cmd = ["python", "-m", "graphrag.query", "--root", repo_path, "--method", "global", topic]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
