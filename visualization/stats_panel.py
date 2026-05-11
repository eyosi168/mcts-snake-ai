import pygame
from core.constants import *


class StatsPanel:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen, phase, current_iter, total_iter, mode):
        texts = [
            "MCTS Snake Visualizer",
            "",
            f"Phase: {phase}",
            f"Iteration: {current_iter}/{total_iter}",
            f"Mode: {mode}",
            "",
            "Controls:",
            "SPACE - Pause",
            "R - Reset",
            "1 - Demo",
            "2 - Balanced",
            "3 - Fast",
            "",
            "Colors:",
            "Blue = Selection",
            "Yellow = Expansion",
            "Red = Simulation",
            "Green = Backpropagation"
        ]

        y = 30

        for text in texts:
            color = WHITE

            if "MCTS Snake" in text:
                color = BLUE

            surf = self.font.render(text, True, color)
            screen.blit(surf, (650, y))
            y += 35