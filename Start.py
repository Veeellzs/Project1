import pygame
pygame.init()
from pygame.color import THECOLORS
clock = pygame.time.Clock()
screenX = 880
screenY = 700
screen = pygame.display.set_mode((880, 700))
my_font = pygame.font.SysFont('Arial', 24, bold = False, italic = False)
text = my_font.render('', True, THECOLORS['black'])
background_image = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
pygame.display.set_caption('Game')

#переменные
yr = 200
h = 120
width = 135 #длина машины1
step = 93 #ширина машины1
stepright = 100


# загрузка спрайтов
prize = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")
car1 = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")
police = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\полиция.png")
carA = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")
carB = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\зеленая.png")
carC = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png")
carD = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png")
carE = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png")

#движение машинки
def move_r(yr, h, step):
    if event.key == pygame.K_UP:
        if (yr - step > 0):
            yr -= step
    if event.key == pygame.K_DOWN:
        if (yr + h + step < screenY):
            yr += step
    if event.key == pygame.K_RIGHT:
        if (yr + width + step < screenX//2):
            yr += stepright

    return (yr)

# движение машин
dx = 2
dy = 2
x = 51
y = 51
r = 20









#счет






xr = 0
yr = 360
running = True
while running:

    screen.blit(background_image, (0, 0))
    screen.blit(car1, (xr, yr))
    screen.blit(carA, (700, 90))
    screen.blit(carC, (700, 200))
    screen.blit(carB, (700, 450))
    screen.blit(carD, (700, 590))
    screen.blit(prize, (700, 290))



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            yr = move_r(yr, h, step)
    pygame.display.flip()
pygame.quit()










