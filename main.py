# main.py

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Vault 901 Interface")

font = pygame.font.SysFont("Courier", 28)
white = (245, 245, 245)
bg = pygame.image.load("ui/vault_bg.png")
clock = pygame.time.Clock()

def draw_text(text, x, y):
    label = font.render(text, True, white)
    screen.blit(label, (x, y))

def main():
    running = True
    while running:
        screen.blit(bg, (0, 0))
        draw_text("VAULT 901", 310, 40)
        draw_text("OVERSEER: DECARLO", 270, 80)
        draw_text("[INVENTORY]  [STATS]  [QUESTS]", 160, 160)
        draw_text("Touchscreen or arrow input not active", 150, 360)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

