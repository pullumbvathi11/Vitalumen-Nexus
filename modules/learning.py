class LearningEngine:
    def __init__(self):
        self.knowledge = []

    def learn(self, data):
        self.knowledge.append(data)
        return f"Learning from: {data}"

    def insights(self):
        if not self.knowledge:
            return "No insights yet."
        return f"Insights generated from {len(self.knowledge)} data points."

    def predict_opportunities(self):
        if len(self.knowledge) < 2:
            return "Not enough data for predictions."
        return "Predicted: 3 strong market opportunities."
