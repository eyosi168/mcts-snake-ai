import random
from mcts.node import MCTSNode
from core.snake import SnakeGame
from mcts.rollout import random_rollout


class MCTS:
    PHASES = [
        "Selection",
        "Expansion",
        "Simulation",
        "Backpropagation"
    ]

    def __init__(self, iterations=20):
        self.iterations = iterations
        self.current_phase_index = 0
        self.current_phase = "Selection"

        self.last_path = []
        self.expanded_node = None
        self.root = None

        self.current_iteration = 0
        self.rollout_positions = []

    def start(self, game):
        self.root = MCTSNode(game.get_state())
        self.current_iteration = 0
        self.current_phase_index = 0
        self.rollout_positions = []

    def iterate(self, game):
        if self.current_iteration >= self.iterations:
            return True

        phase = self.PHASES[self.current_phase_index]
        self.current_phase = phase

        if phase == "Selection":
            self.selection(game)

        elif phase == "Expansion":
            self.expansion(game)

        elif phase == "Simulation":
            self.simulation()

        elif phase == "Backpropagation":
            self.backprop()

            self.current_iteration += 1

        self.current_phase_index = (self.current_phase_index + 1) % 4

        return False

    def selection(self, game):
        self.sim_game = SnakeGame()
        self.sim_game.load_state(self.root.state)

        self.node = self.root
        self.last_path = [self.node]

        while self.node.children:
            self.node = self.node.best_child()
            self.last_path.append(self.node)

            self.sim_game.load_state(
                self.node.state.clone()
            )

    def expansion(self, game):
        if self.sim_game.alive and not self.node.children:

            for action in SnakeGame.ACTIONS:

                child_game = SnakeGame()
                child_game.load_state(
                    self.sim_game.get_state().clone()
                )

                child_game.step(action)

                child = MCTSNode(
                    child_game.get_state(),
                    parent=self.node,
                    action=action
                )

                self.node.children.append(child)

        if self.node.children:
            self.node = random.choice(self.node.children)
            self.expanded_node = self.node

            self.sim_game.load_state(
                self.node.state.clone()
            )

    def simulation(self):
        self.reward, self.rollout_positions = random_rollout(
        self.sim_game
    )

    def backprop(self):
        node = self.node

        while node:
            node.visits += 1
            node.reward += self.reward
            node = node.parent

    def best_action(self):
        if not self.root.children:
            return random.choice(SnakeGame.ACTIONS)

        return max(
            self.root.children,
            key=lambda c: c.visits
        ).action