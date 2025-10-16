import pygame
from game.paddle import Paddle
from game.ball import Ball

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)

        self.winning_score = 5  # Default winning score

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-self.player.speed, self.height)
        if keys[pygame.K_s]:
            self.player.move(self.player.speed, self.height)

    def update(self):
        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        # Check scoring
        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw scores
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

    def check_game_over(self, screen):
        if self.player_score >= self.winning_score or self.ai_score >= self.winning_score:
            screen.fill(BLACK)
            if self.player_score >= self.winning_score:
                text = self.font.render("Player Wins!", True, WHITE)
            else:
                text = self.font.render("AI Wins!", True, WHITE)

            # Center text
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()

            # Pause so players can see the message
            pygame.time.delay(2000)
            return True
        return False

    def reset_game(self):
        """Reset scores and ball for a new match."""
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset()

    def replay_menu(self, screen):
        """Show replay options after game over and wait for user input."""
        screen.fill(BLACK)
        lines = [
            "Choose match type:",
            "Press 3 for Best of 3",
            "Press 5 for Best of 5",
            "Press 7 for Best of 7",
            "Press ESC to Exit"
        ]

        for i, line in enumerate(lines):
            text = self.font.render(line, True, WHITE)
            rect = text.get_rect(center=(self.width // 2, self.height // 2 - 60 + i * 40))
            screen.blit(text, rect)

        pygame.display.flip()

        # Wait for player input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        return 2  # Best of 3 -> first to 2
                    elif event.key == pygame.K_5:
                        return 3  # Best of 5 -> first to 3
                    elif event.key == pygame.K_7:
                        return 4  # Best of 7 -> first to 4
                    elif event.key == pygame.K_ESCAPE:
                        return None
