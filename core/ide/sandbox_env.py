import docker
import os

class PlaywrightSandbox:
    def __init__(self):
        try:
            self.client = docker.from_env()
            self.image = "mcr.microsoft.com/playwright:v1.42.0-jammy"
        except Exception as e:
            print("[Sandbox] Docker not running or not installed.")
            self.client = None

    def run_tests(self, test_script_path):
        if not self.client: return "Docker unavailable."
        print(f"[Sandbox] Spinning up isolated container for {test_script_path}")
        container = self.client.containers.run(
            self.image,
            command=f"npx playwright test /tests/{os.path.basename(test_script_path)}",
            volumes={os.path.dirname(test_script_path): {'bind': '/tests', 'mode': 'ro'}},
            remove=True,
            detach=False
        )
        return container.decode('utf-8')
