import random
from core.snake import SnakeGame


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def random_rollout(game, depth=15):
    positions = []

    initial_distance = manhattan(
        game.snake[0],
        game.food
    )

    for _ in range(depth):
        if not game.alive:
            return -100, positions

        possible = []

        for action in SnakeGame.ACTIONS:
            head = game.snake[0]

            nxt = (
                head[0] + action[0],
                head[1] + action[1]
            )

            if nxt not in game.snake:
                possible.append(action)

        if not possible:
            return -100, positions

        action = random.choice(possible)

        game.step(action)

        positions.append(game.snake[0])

        if game.snake[0] == game.food:
            return 100, positions

    final_distance = manhattan(
        game.snake[0],
        game.food
    )

    reward = initial_distance - final_distance

    reward += game.score * 50

    return reward, positions