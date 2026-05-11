import pygame
from core.constants import *
from core.snake import SnakeGame
from visualization.renderer import Renderer
from visualization.stats_panel import StatsPanel
from visualization.tree_view import TreeView
from mcts.search import MCTS


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MCTS Snake Visualizer")

    clock = pygame.time.Clock()

    game = SnakeGame()
    renderer = Renderer(screen)
    stats = StatsPanel()
    tree = TreeView()

    mcts = MCTS(iterations=25)

    mode = "Balanced"
    phase_delay = 40
    paused = False

    mcts.start(game)

    phase_timer = 0

    running = True

    while running:
        dt = clock.tick(60)
        phase_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_r:
                    game.reset()
                    mcts.start(game)

                elif event.key == pygame.K_1:
                    mode = "Demo"
                    mcts.iterations = 8
                    phase_delay = 120

                elif event.key == pygame.K_2:
                    mode = "Balanced"
                    mcts.iterations = 40
                    phase_delay = 35

                elif event.key == pygame.K_3:
                    mode = "Fast"
                    mcts.iterations = 120
                    phase_delay = 5

        if not paused and phase_timer > phase_delay:

            finished = mcts.iterate(game)
            phase_timer = 0

            if finished:
                move = mcts.best_action()

                game.step(move)

                if not game.alive:
                    game.reset()

                mcts.start(game)

        renderer.draw(game, mcts.rollout_positions)

        stats.draw(
            screen,
            mcts.current_phase,
            mcts.current_iteration,
            mcts.iterations,
            mode
        )

        tree.draw(screen, mcts.root, mcts)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()