class GameState:
    def __init__(self, snake, direction, food, score=0, alive=True):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.score = score
        self.alive = alive

    def clone(self):
        return GameState(
            self.snake[:],
            self.direction,
            self.food,
            self.score,
            self.alive
        )