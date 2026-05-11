import math


class MCTSNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.x = 0
        self.y = 0

        self.children = []

        self.visits = 0
        self.reward = 0

    def ucb1(self, exploration=1.41):
        if self.visits == 0:
            return float("inf")

        return (
            self.reward / self.visits
            + exploration * math.sqrt(
                math.log(self.parent.visits) / self.visits
            )
        )

    def best_child(self):
        return max(self.children, key=lambda c: c.ucb1())