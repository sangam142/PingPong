import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7

    def move(self, dy, screen_height):
        self.y += dy
        # Keep paddle inside screen
        self.y = max(0, min(self.y, screen_height - self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def auto_track(self, ball, screen_height):
        if ball.y + ball.height/2 < self.y + self.height/2:
            self.move(-self.speed, screen_height)
        elif ball.y + ball.height/2 > self.y + self.height/2:
            self.move(self.speed, screen_height)
