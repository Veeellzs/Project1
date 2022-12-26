import pygame, Rules, AboutGonka #, Game
pygame.init()
from pygame.color import THECOLORS
left = 420
top = [60, 160, 260]
width = 260
height = 70
menu_text = [" Играть","Правила", "Помощь"]
menu_text1 = "Гонки"
screenX = 750
screenY = 500
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Menu")
my_font = pygame.font.SysFont("Calibri", 35, bold=False, italic=False)
my_font1 = pygame.font.SysFont("Arial", 50, bold=False, italic=True)
fon = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\photo_2022-12-14_13-58-26.png")

run = True

while run:
    screen.fill(THECOLORS["black"])
    screen.blit(fon, (0, 0))
    for i in range(3):
        pygame.draw.ellipse(screen, THECOLORS["grey"], [left, top[i], width-20, height], 0)
        text = my_font.render(menu_text[i], True, THECOLORS["black"])
        screen.blit(text, [left + 60, top[i] + 20])
    text1 = my_font1.render(menu_text1, True, THECOLORS["black"])
    screen.blit(text1,[40, 30])
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
                Rules.drawHelp()

            elif k == 2:
                print("About")
                AboutGonka.drawAbout()
