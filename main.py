import pygame
from game.game_engine import GameEngine

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game engine
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic
        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        # Check for game over
        if engine.check_game_over(SCREEN):
            running = False  # stop the loop after showing message

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
