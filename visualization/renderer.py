import pygame
from core.constants import *


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, game, rollout=None):
        self.screen.fill(BLACK)

        pygame.draw.rect(
            self.screen,
            GRAY,
            (0, 0, BOARD_WIDTH, BOARD_HEIGHT),
            2
        )

        for x, y in game.snake:
            pygame.draw.rect(
                self.screen,
                GREEN,
                (x * GRID_SIZE, y * GRID_SIZE,
                 GRID_SIZE, GRID_SIZE)
            )

        fx, fy = game.food
        pygame.draw.rect(
            self.screen,
            RED,
            (fx * GRID_SIZE, fy * GRID_SIZE,
             GRID_SIZE, GRID_SIZE)
        )

        if rollout:
            for x, y in rollout:
                pygame.draw.rect(
                    self.screen,
                    YELLOW,
                    (x * GRID_SIZE, y * GRID_SIZE,
                     GRID_SIZE, GRID_SIZE),
                    2
                )

        score = self.font.render(
            f"Score: {game.score}",
            True,
            WHITE
        )

        self.screen.blit(score, (650, 50))