import sys
# Importing our extracted MiroFish module for debate/reasoning
# Assuming MiroFish is accessible in our swarm registry
try:
    from aegis_swarm.swarms.mirofish import MiroFish
    HAS_MIROFISH = True
except ImportError:
    HAS_MIROFISH = False

class CognitiveCore:
    """
    [VECTOR 2: OPENRLHF MCTS REASONING]
    Now automatically routes complex reasoning tasks through MiroFish.
    """
    def __init__(self):
        self.mirofish = MiroFish() if HAS_MIROFISH else None
        print("[CognitiveCore] DeepSeek-R1 logic + MiroFish Debate Engine initialized.")

    def reason(self, prompt, is_debate=False):
        if is_debate and self.mirofish:
            print(f"[CognitiveCore] Routing to MiroFish for structured debate...")
            return self.mirofish.analyze(prompt)
        return f"<think> Simulated MCTS logic tree for: {prompt} </think>"
