from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class SwarmConfig(BaseModel):
    name: str
    version: str = "1.0.0"
    api_key: Optional[str] = None
    target_path: str

class EvolutionLog(BaseModel):
    timestamp: float
    action: str
    status: str
    energy_state: float
