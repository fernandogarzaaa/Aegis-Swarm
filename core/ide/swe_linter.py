import py_compile
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

class SWELinter:
    """
    [Upgrade 3: SWE-AGENT STYLE LINTER]
    Runs a `git diff` syntax check on it BEFORE committing.
    """
    def check_patch(self, patch_file):
        print(f"[SWE-Linter] Validating syntax for {patch_file}...")
        if not os.path.exists(patch_file):
            return {"status": "error", "message": "File not found"}
        
        try:
            py_compile.compile(patch_file, doraise=True)
            print(f"[SWE-Linter] ✅ Validation passed. Clean AST.")
            return {"status": "passed"}
        except py_compile.PyCompileError as e:
            print(f"[SWE-Linter] ❌ Syntax Error detected. Patch rejected.")
            return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    linter = SWELinter()
    # Test on itself to prove it works
    print(linter.check_patch(__file__))