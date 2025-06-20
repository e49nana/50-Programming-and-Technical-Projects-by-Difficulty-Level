import pygame
import math

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pendulum Simulation")

clock = pygame.time.Clock()

# Paramètres physiques
g = 9.81
L = 200  # longueur en pixels
angle = math.pi / 4  # 45 degrés
a_vel = 0
a_acc = 0
origin = (WIDTH // 2, 100)

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def to_cartesian(angle, length):
    x = origin[0] + length * math.sin(angle)
    y = origin[1] + length * math.cos(angle)
    return int(x), int(y)

running = True
while running:
    screen.fill(WHITE)

    # Physique (Euler)
    a_acc = -g / L * math.sin(angle)
    a_vel += a_acc
    angle += a_vel
    a_vel *= 0.99  # amortissement

    bob = to_cartesian(angle, L)

    # Dessin
    pygame.draw.line(screen, BLACK, origin, bob, 2)
    pygame.draw.circle(screen, RED, bob, 20)

    pygame.display.flip()
    clock.tick(60)

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
