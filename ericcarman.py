import pygame
import sys

# Inicialitza Pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Eric Cartman - South Park')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
SKIN = (255, 224, 189)


# Funció per dibuixar Eric Cartman
def draw_cartman():
    screen.fill(WHITE)

    # Cap (el·lipse)
    pygame.draw.ellipse(screen, SKIN, (320, 300, 160, 200))

    # Gorro (arc)
    pygame.draw.arc(screen, BLUE, (320, 300, 160, 200), 3.14, 6.28, 80)

    # Ulls
    pygame.draw.ellipse(screen, WHITE, (350, 340, 40, 20))
    pygame.draw.ellipse(screen, WHITE, (410, 340, 40, 20))
    pygame.draw.circle(screen, BLACK, (370, 350), 5)
    pygame.draw.circle(screen, BLACK, (430, 350), 5)

    # Celles (línies)
    pygame.draw.line(screen, BLACK, (350, 330), (390, 330), 2)
    pygame.draw.line(screen, BLACK, (410, 330), (450, 330), 2)

    # Boca
    pygame.draw.arc(screen, BLACK, (360, 380, 80, 40), 0, 3.14, 2)

    # Cos
    pygame.draw.rect(screen, RED, (330, 460, 140, 100))

    # Guants
    pygame.draw.circle(screen, YELLOW, (330, 480), 15)
    pygame.draw.circle(screen, YELLOW, (470, 480), 15)


# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_cartman()
    pygame.display.update()
