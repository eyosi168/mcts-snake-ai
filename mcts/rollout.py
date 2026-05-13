import random
from core.snake import SnakeGame


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def random_rollout(game, depth=35):
    positions = []

    survived = 0

    for _ in range(depth):
        if not game.alive:
            break

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
            break

        action = random.choice(possible)

        game.step(action)

        positions.append(game.snake[0])
        survived += 1

    reward = evaluate(game, survived)

    return reward, positions


def evaluate(game, survived):
    if not game.alive:
        return -150

    reward = 0

    # Food matters
    reward += game.score * 120

    # Staying alive matters
    reward += survived * 3

    # Prefer approaching food
    reward -= manhattan(
        game.snake[0],
        game.food
    )

    return reward
