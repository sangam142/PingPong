import pygame
import random
import os

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

        # Load sounds
        assets_path = os.path.join(os.path.dirname(__file__), "..", "assets")
        self.paddle_sound = pygame.mixer.Sound(os.path.join(assets_path, "paddle_hit.wav"))
        self.wall_sound = pygame.mixer.Sound(os.path.join(assets_path, "wall_bounce.wav"))
        self.score_sound = pygame.mixer.Sound(os.path.join(assets_path, "score.wav"))

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            self.wall_sound.play()  # play wall bounce sound

    def check_collision(self, player, ai):
        future_rect = self.rect()
        future_rect.x += self.velocity_x

        # Collision with player paddle
        if future_rect.colliderect(player.rect()):
            self.velocity_x = abs(self.velocity_x)
            offset = (self.y + self.height/2) - (player.y + player.height/2)
            self.velocity_y = offset * 0.1
            self.paddle_sound.play()  # play paddle hit sound

        # Collision with AI paddle
        elif future_rect.colliderect(ai.rect()):
            self.velocity_x = -abs(self.velocity_x)
            offset = (self.y + self.height/2) - (ai.y + ai.height/2)
            self.velocity_y = offset * 0.1
            self.paddle_sound.play()  # play paddle hit sound

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        self.score_sound.play()  # play scoring sound

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
