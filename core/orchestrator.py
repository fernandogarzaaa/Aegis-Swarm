import os
import sys

# Set root project path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from swarms.analysis import AnalysisSwarm
from swarms.audit import AuditSwarm
from swarms.devops import DevOpsSwarm
from swarms.god import GodSwarm
from core.whatsapp import WhatsAppNotifier
from core.token_manager import TokenManager

class SwarmOrchestrator:
    def __init__(self, target_project):
        self.target = target_project
        self.analysis = AnalysisSwarm()
        self.audit = AuditSwarm()
        self.devops = DevOpsSwarm()
        self.god = GodSwarm()
        self.notifier = WhatsAppNotifier()
        self.tm = TokenManager()

    def run(self):
        print(f"--- Production Evolution Cycle: {self.target} ---")
        
        # 1. Activation
        report = self.analysis.run(self.target)
        # Apply Token Fracture
        report = self.tm.fracture(str(report))
        
        # 2. Audit Swarm
        audit = self.audit.run(self.target, report)
        
        # 3. DevOps Swarm (Sandbox)
        sandbox = self.devops.prepare_sandbox(self.target, audit)
        
        # 4. God Swarm (Ascension Engine + Quantum Engine + Mirofish)
        print("--- CIRCUIT BREAKER: Human Approval Required ---")
        status = self.god.verify(sandbox)
        
        # 5. Report
        self.notifier.notify(f"Production Ready: {status}")
        return status
