import pygame
pygame.init()
from pygame.color import THECOLORS
left = 100
top = [60, 210, 360]
width = 400
height = 80
menu_text = ["Start","Rules", "About"]
screenX = 750
screenY = 500
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Menu")
my_font = pygame.font.SysFont("Calibri", 40, bold=False, italic=False)
run = True
while run:
    screen.fill(THECOLORS["black"])
    for i in range(3):
        pygame.draw.ellipse(screen, THECOLORS["grey"], [left, top[i], width, height], 0)
        text = my_font.render(menu_text[i], True, THECOLORS["black"])
        screen.blit(text, [left + 150, top[i] + 30])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            for k in range(3):
                if x > left and x < left + width and y > top[k] and y < top[k] + height:
                    break
                else:
                    k = 10
            if k == 0:
                print("Start")

            elif k == 1:
                print("Rules")

            elif k == 2:
                print("About")

