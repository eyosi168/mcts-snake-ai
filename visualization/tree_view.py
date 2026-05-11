import pygame
from core.constants import *


class TreeView:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 16)

    def layout(self, node, x, y, spacing=80):
        node.x = x
        node.y = y

        if not node.children:
            return

        start = x - (len(node.children) - 1) * spacing // 2

        for i, child in enumerate(node.children):
            self.layout(child, start + i * spacing, y + 80, spacing // 2)

    def draw_node(self, screen, node, mcts):
        color = WHITE

        if node in mcts.last_path:
            color = BLUE

        if node == mcts.expanded_node:
            color = YELLOW

        if mcts.current_phase == "Simulation" and node == mcts.expanded_node:
            color = RED

        if mcts.current_phase == "Backpropagation" and node in mcts.last_path:
            color = GREEN

        pygame.draw.circle(screen, color, (node.x, node.y), 15)

        text = f"{node.visits}"

        if node.visits > 0:
            avg = node.reward / node.visits
            text += f":{avg:.1f}"

        label = self.font.render(text, True, WHITE)
        screen.blit(label, (node.x - 20, node.y - 8))

        for child in node.children:
            pygame.draw.line(
                screen,
                GRAY,
                (node.x, node.y),
                (child.x, child.y),
                2
            )
            self.draw_node(screen, child, mcts)

    def draw(self, screen, root, mcts):
        if not root:
            return

        self.layout(root, 1020, 430, 120)
        self.draw_node(screen, root, mcts)