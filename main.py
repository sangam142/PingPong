import pygame
from game.game_engine import GameEngine

# Initialize pygame and mixer for sounds
pygame.init()
pygame.mixer.init()  # <-- initialize audio system

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 60

def replay_menu():
    SCREEN.fill(BLACK)
    font = pygame.font.SysFont("Arial", 30)
    lines = [
        "Choose match type:",
        "Press 3 for Best of 3",
        "Press 5 for Best of 5",
        "Press 7 for Best of 7",
        "Press ESC to Exit"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60 + i*40))
        SCREEN.blit(text, rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    return 2  # best of 3 => first to 2
                elif event.key == pygame.K_5:
                    return 3  # best of 5 => first to 3
                elif event.key == pygame.K_7:
                    return 4  # best of 7 => first to 4
                elif event.key == pygame.K_ESCAPE:
                    return None

def main():
    engine = GameEngine(WIDTH, HEIGHT)
    running = True

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        # Game over
        if engine.check_game_over(SCREEN):
            target_score = replay_menu()
            if target_score is None:
                running = False
            else:
                engine.winning_score = target_score
                engine.reset_game()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
