import ast
import os

class RepoMapper:
    """
    [Upgrade 1: AIDER-STYLE CONTEXT MAP]
    Generates an AST-based bird's-eye view of the entire repository.
    Extracts class names, function signatures, and docstrings.
    """
    def __init__(self, root_path):
        self.root_path = root_path

    def generate_file_map(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=file_path)
            except SyntaxError:
                return f"[Syntax Error in {os.path.basename(file_path)}]"
        
        lines = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                lines.append(f"class {node.name}:")
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef):
                        lines.append(f"    def {subnode.name}(...):")
            elif isinstance(node, ast.FunctionDef):
                lines.append(f"def {node.name}(...):")
        
        return "\n".join(lines) if lines else "[No classes/functions]"

    def generate_map(self):
        repo_map = []
        for root, _, files in os.walk(self.root_path):
            if "__pycache__" in root or ".git" in root or "venv" in root: continue
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.root_path)
                    repo_map.append(f"\n--- {rel_path} ---")
                    repo_map.append(self.generate_file_map(full_path))
        return "\n".join(repo_map)

if __name__ == "__main__":
    mapper = RepoMapper(os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__))
    print(mapper.generate_map()[:500] + "\n...[TRUNCATED]")
