import random
from core.constants import ROWS, COLS
from core.game_state import GameState


class SnakeGame:
    ACTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(10, 10)]
        self.direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.alive = True

    def spawn_food(self):
        while True:
            food = (
                random.randint(0, COLS - 1),
                random.randint(0, ROWS - 1)
            )
            if food not in self.snake:
                return food

    def get_state(self):
        return GameState(
            self.snake[:],
            self.direction,
            self.food,
            self.score,
            self.alive
        )

    def load_state(self, state):
        self.snake = state.snake[:]
        self.direction = state.direction
        self.food = state.food
        self.score = state.score
        self.alive = state.alive

    def step(self, direction=None):
        if direction:
            self.direction = direction

        head = self.snake[0]

        new_head = (
            head[0] + self.direction[0],
            head[1] + self.direction[1]
        )

        if (
            new_head[0] < 0 or new_head[0] >= COLS or
            new_head[1] < 0 or new_head[1] >= ROWS or
            new_head in self.snake
        ):
            self.alive = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()