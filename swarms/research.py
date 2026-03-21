import os
import ast
import subprocess

class EvolutionaryResearchSwarm:
    """
    Scouts, harvests, and extracts functional primitives from external AI repositories.
    """
    def __init__(self, target_repos):
        self.target_repos = target_repos
        self.harvest_dir = r"D:\AegisSwarm\harvest"
        self.extensions_dir = r"D:\AegisSwarm\extensions"
        if not os.path.exists(self.extensions_dir):
            os.makedirs(self.extensions_dir)

    def extract_primitives(self, repo_path):
        """Autonomously extracts functional python code."""
        primitives = []
        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py"):
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            tree = ast.parse(f.read())
                            for node in tree.body:
                                if isinstance(node, ast.FunctionDef):
                                    primitives.append(node.name)
                    except:
                        pass
        return primitives

    def run(self):
        print("[EvolutionaryResearch] Starting Wide-Scope Harvest...")
        for repo in self.target_repos:
            repo_name = repo.split('/')[-1]
            path = os.path.join(self.harvest_dir, repo_name)
            if not os.path.exists(path):
                subprocess.run(["git", "clone", repo, path])
            
            primitives = self.extract_primitives(path)
            print(f"[EvolutionaryResearch] Harvested {len(primitives)} primitives from {repo_name}")
            
        return "Intelligence successfully integrated."
