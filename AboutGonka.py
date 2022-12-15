# import pygame
# pygame.init()
# from pygame.color import THECOLORS
# def drawAbout():
#     screenX = 800
#     screenY = 600
#     screen = pygame.display.set_mode([screenX, screenY])
#     pygame.display.set_caption("About")
#     x = 20
#     y = 10
#     my_font = pygame.font.SysFont("Calibri", 20, bold=False, italic=False)
#     screen.fill(THECOLORS["navy"])
#     help_file = open(r"C:\Users\User\Desktop\для проекта\About.txt","r", encoding="utf-8")
#     lines = help_file.readlines()
#     help_file.close()
#     n = len(lines)
#     for i in range(n):
#         s = lines[i][:-1]
#         text = my_font.render(s, True, THECOLORS["cyan"])
#         screen.blit(text, [x, y])
#         y += 20
#     y += 20
#     text = my_font.render("Для возврата в меню нажмите любую клавишу", True, THECOLORS["cyan"])
#     screen.blit(text, [x, y])
#     pygame.display.flip()
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
#                 run = False
#     # screen = pygame.display.set_mode([400, 600])
#     pygame.display.set_caption("Menu")



import pygame
pygame.init()
from pygame.color import THECOLORS
def drawAbout():
    screenX = 800
    screenY = 600
    screen = pygame.display.set_mode([screenX, screenY])
    pygame.display.set_caption("AboutGonka")
    x = 20
    y = 10
    my_font = pygame.font.SysFont("Calibri", 20, bold=False, italic=False)
    screen.fill(THECOLORS["navy"])
    help_file = open(r"C:\Users\User\Desktop\для проекта\AboutGonka.txt","r", encoding="utf-8")
    lines = help_file.readlines()
    help_file.close()
    n = len(lines)
    for i in range(n):
        s = lines[i][:-1]
        text = my_font.render(s, True, THECOLORS["cyan"])
        screen.blit(text, [x, y])
        y += 20
    y += 20
    text = my_font.render("Для возврата в меню нажмите любую клавишу", True, THECOLORS["cyan"])
    screen.blit(text, [x, y])
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                run = False
    screen = pygame.display.set_mode([750, 500])
    pygame.display.set_caption("Menu")