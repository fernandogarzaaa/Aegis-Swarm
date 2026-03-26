import os
import sys
import subprocess

class SecuritySwarm:
    def __init__(self):
        pass

    def run_pentest(self, target_path):
        print(f"[Swarm][SecuritySwarm] Unleashing Strix AI Hacker on {target_path}...")
        
        # Setup environment variables for Strix
        env = os.environ.copy()
        
        # Fallback LLM logic. Use OpenRouter or Gemini if available.
        if "STRIX_LLM" not in env:
            # Prefer Gemini as it's highly capable and configured in OpenClaw ecosystem
            env["STRIX_LLM"] = "gemini/gemini-3.1-pro-preview"
            
            # Map Gemini key if missing explicitly for LLM_API_KEY
            if "GEMINI_API_KEY" in env and "LLM_API_KEY" not in env:
                env["LLM_API_KEY"] = env["GEMINI_API_KEY"]
            elif "OPENROUTER_API_KEY" in env and "LLM_API_KEY" not in env:
                env["STRIX_LLM"] = "openrouter/auto"
                env["LLM_API_KEY"] = env["OPENROUTER_API_KEY"]

        # Locate Strix executable in the virtual environment
        venv_scripts = os.path.join(os.getenv("OPENCLAW_ROOT", "./"), __file__)
        strix_exe = os.path.join(venv_scripts, "strix.exe")
        
        # Fallback to system PATH if not found in venv
        if not os.path.exists(strix_exe):
            strix_exe = "strix"

        report_path = os.path.join(target_path, "strix_security_report.log")

        try:
            # Running Strix in headless mode against the sandbox directory
            # -n / --non-interactive is necessary for automated CI/CD style pipelines
            print(f"[Swarm][SecuritySwarm] Executing: {strix_exe} -n --target {target_path}")
            result = subprocess.run(
                [strix_exe, "-n", "--target", target_path],
                env=env,
                capture_output=True,
                text=True
            )
            
            # Log output for Devops remediation integration
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write("\n--- STDERR ---\n" + result.stderr)

            if result.returncode == 0:
                print("[Swarm][SecuritySwarm] Strix completed: Codebase appears secure. No critical vulnerabilities found.")
                return {"status": "secure", "report": report_path}
            else:
                print(f"[Swarm][SecuritySwarm] Strix completed: VULNERABILITIES DETECTED! (Exit code: {result.returncode})")
                print(f"[Swarm][SecuritySwarm] Generating Proof-of-Concepts in {report_path}")
                return {"status": "vulnerable", "report": report_path}

        except FileNotFoundError:
            print("[Swarm][SecuritySwarm] Strix executable not found. Ensure 'strix-agent' is installed. Skipping pentest.")
            return {"status": "skipped", "reason": "strix_not_installed"}
        except Exception as e:
            print(f"[Swarm][SecuritySwarm] Strix execution failed due to environment error: {e}")
            return {"status": "error", "error": str(e)}
