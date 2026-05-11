import pygame
from core.constants import *
from core.snake import SnakeGame
from visualization.renderer import Renderer
from mcts.search_fast import MCTS


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MCTS Snake - Intelligent Mode")

    clock = pygame.time.Clock()

    game = SnakeGame()
    renderer = Renderer(screen)

    mcts = MCTS(iterations=150)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game.alive:
            move = mcts.search(game)
            game.step(move)
        else:
            game.reset()

        renderer.draw(game)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()