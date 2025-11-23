from .core_system import PlatformCore
from .learning import LearningEngine
from .actions import ActionEngine

class NexusIntegration:
    def __init__(self):
        self.core = PlatformCore()
        self.learning = LearningEngine()
        self.actions = ActionEngine()

    def process(self, input_data):
        learned = self.learning.learn(input_data)
        insight = self.learning.insights()
        action = self.actions.perform(insight)
        return {
            "learned": learned,
            "insight": insight,
            "action": action
        }

    def status(self):
        return "Nexus Integration Active — All Systems Connected."
