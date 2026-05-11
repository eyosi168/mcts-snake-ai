import random
from mcts.node import MCTSNode
from core.snake import SnakeGame


class MCTS:
    def __init__(self, iterations=150):
        self.iterations = iterations

    def search(self, game):
        root = MCTSNode(game.get_state())

        for _ in range(self.iterations):
            node = root

            sim_game = SnakeGame()
            sim_game.load_state(root.state)

            while node.children:
                node = node.best_child()
                sim_game.step(node.action)

            if sim_game.alive:
                for action in SnakeGame.ACTIONS:
                    child = MCTSNode(
                        sim_game.get_state().clone(),
                        parent=node,
                        action=action
                    )
                    node.children.append(child)

                node = random.choice(node.children)
                sim_game.step(node.action)

            reward = self.rollout(sim_game)

            while node:
                node.visits += 1
                node.reward += reward
                node = node.parent

        return max(
            root.children,
            key=lambda c: c.visits
        ).action

    def rollout(self, game, depth=20):
        for _ in range(depth):
            if not game.alive:
                break

            action = random.choice(SnakeGame.ACTIONS)
            game.step(action)

        return game.score