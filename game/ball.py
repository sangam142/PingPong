import pygame
import random

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

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1

    def check_collision(self, player, ai):
        # Create a future rect along ball's path
        future_rect = self.rect()
        future_rect.x += self.velocity_x

        # Collision with player paddle
        if future_rect.colliderect(player.rect()):
            self.velocity_x = abs(self.velocity_x)  # move right
            offset = (self.y + self.height/2) - (player.y + player.height/2)
            self.velocity_y = offset * 0.1  # adjust angle

        # Collision with AI paddle
        elif future_rect.colliderect(ai.rect()):
            self.velocity_x = -abs(self.velocity_x)  # move left
            offset = (self.y + self.height/2) - (ai.y + ai.height/2)
            self.velocity_y = offset * 0.1  # adjust angle

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
