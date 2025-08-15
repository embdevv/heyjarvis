# modules / visualizer.py
# SECURITY: Pure local UI (pygame). No network calls.

import pygame, random, math
from config import UI_WIDTH as WIDTH, UI_HEIGHT as HEIGHT

class Node:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(1, 3)
        self.speed_x = random.uniform(-0.6, 0.6)
        self.speed_y = random.uniform(-0.6, 0.6)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), (int(self.x), int(self.y)), self.radius)

def run_visualizer():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("J.A.R.V.I.S. Interface")

    nodes = [Node() for _ in range(120)]
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((8, 10, 26))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for n in nodes:
            n.move()
            n.draw(screen)

        for i in range(len(nodes)):
            xi, yi = nodes[i].x, nodes[i].y
            for j in range(i + 1, len(nodes)):
                xj, yj = nodes[j].x, nodes[j].y
                dist = math.hypot(xi - xj, yi - yj)

                if dist < 110:
                    pygame.draw.line(screen, (0, 120, 255), (xi, yi), (xj, yj), 1)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()