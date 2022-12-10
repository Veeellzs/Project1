import pygame, random, time

pygame.init()
from pygame.color import THECOLORS

clock = pygame.time.Clock()
screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX,screenY])

# my_font = pygame.font.SysFont('Arial', 24, bold = False, italic = False)
# text = my_font.render('', True, THECOLORS['black'])

# переменные
yr = 200  # координата левого верхнего угла машинки?
h = 120  # ширина машинки
width = 135  # длина машины

step = 93  # шаг / смещение на 1 полосу
stepLeft = 10  # шаг / движение встречных машин

xr = 0  # X-координата для машинки игрока
yr = 360  # Y-координата для машинки игрока

# движение встречных машин
dx = 2
dy = 2
x = 51
y = 51
r = 20
carA_x = 700
carA_y = 90
carB_x = 700
carB_y = 200
carC_x = 700
carC_y = 450
carD_x = 700
carD_y = 590
#carE_x = 700
#carE_y = 290
prize_x = 700
prize_y = 290
speed = 0.2  # уровень сложности - скорость встречных машин
count = 0
kolvo = 0    # количество встречных машин

# загрузка спрайтов
prize = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")
car1 = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")
carA = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")
carB = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\зеленая.png")
carC = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png")
carD = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png")
carE = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png")
background_image = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
pygame.display.set_caption('Game')


def move_r(yr, h, step):  # движение машинки
    if event.key == pygame.K_UP:
        if (yr - step > 0):
            yr -= step
    if event.key == pygame.K_DOWN:
        if (yr + h + step < screenY):
            yr += step
    return (yr)


def countm(xr, xy, prize_x, prize_y, count, speed):  # счет
    if xr == prize_x and xy == prize_y:
        count += 1
        # заставить монетку исчезнуть
    if count > 10:
        speed -= 0.2
    elif count > 20:
        speed -= 0.4
    elif count > 30:
        speed -= 0.6
    elif count > 40:
        speed -= 0.8
    elif count > 50:
        speed -= 1
    elif count > 60:
        speed -= 1.2
    elif count > 70:
        speed -= 1.4
    elif count > 80:
        speed -= 1.6
    elif count > 90:
        speed -= 1.8
    elif count > 100:
        speed -= 2
    return (count, speed)


import threading

#for i in range(1,300):     # СДЕЛАТЬ ГЕНЕРАЦИЮ МАШИНОК РАЗ В НЕСКОЛЬКО СЕКУНД

#     time.sleep(3000)
kolvo = random.randint(1,4)
if kolvo == 4:
    carA_x = screenX
    carA_y = 90
    carB_x = screenX
    carB_y = 200
    carC_x = screenX
    carC_y = 450
    carD_x = screenX
    carD_y = 590
elif kolvo == 3:
    carA_x = screenX
    carA_y = 90
    carB_x = screenX
    carB_y = 200
    carC_x = screenX
    carC_y = 450
elif kolvo == 2:
    carA_x = screenX
    carA_y = 90
    carB_x = screenX
    carB_y = 200
elif kolvo == 1:
    carA_x = screenX
    carA_y = 90

running = True
while running:
    count, speed = countm(xr, yr, prize_x, prize_y, count, speed)
    carA_x = carA_x - stepLeft * speed  # ускорение в зависимости от прогрееса
    carB_x = carB_x - stepLeft * speed
    carC_x = carC_x - stepLeft * speed
    carD_x = carD_x - stepLeft * speed
    prize_x = prize_x - stepLeft * speed
    if carA_x < 0:
        #threading.Event().wait(1)
        pygame.time.delay(5)
        kolvo = random.randint(1, 4)
        if kolvo == 4:
            carA_x = 1
            carA_y = 90
            carB_x = 1
            carB_y = 200
            carC_x = 1
            carC_y = 450
            carD_x = 1
            carD_y = 590
        elif kolvo == 3:
            carA_x = 1
            carA_y = 90
            carB_x = 1
            carB_y = 200
            carC_x = 1
            carC_y = 450
        elif kolvo == 2:
            carA_x = 1
            carA_y = 90
            carB_x = 1
            carB_y = 200
        elif kolvo == 1:
            carA_x = 1
            carA_y = 90

    screen.blit(background_image, (0, 0))  # отрисовка положений встречных машин
    screen.blit(car1, (xr, yr))
    screen.blit(carA, (carA_x, carA_y))
    screen.blit(carC, (carB_x, carB_y))
    screen.blit(carB, (carC_x, carC_y))
    screen.blit(carD, (carD_x, carD_y))
    screen.blit(prize, (prize_x, prize_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            yr = move_r(yr, h, step)
    pygame.display.flip()
pygame.quit()