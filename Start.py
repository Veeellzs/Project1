import os.path

import pygame
import random
import time
pygame.init()
from pygame.color import THECOLORS


def load_sprite(path):
    return pygame.image.load(os.path.join(path))

step = 100  # шаг / смещение на 1 полосу   (93)
h = 120  # высота машинки игрока
# xr = 0  # X-координата для машинки игрока
yr = 400  # Y-координата для машинки игрока   (360)   (верхний левый угол машинки)
game_over = False   # проигрыш и экран смерти

screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX, screenY])

player_x = 0   # х - координата игрока
yr= 360   # у - координата игрока
player_y = 360  # удалить
player_sprite = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")

background_image = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
gameover = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\d55285388e843b575b4b89986ad65ef2.png")

pygame.display.set_caption(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")  # монетка

FPS = 60  # frames per seconds
TICKER_MAX_COUNT = FPS * 60 * 3  # tick count will be set to 0 every 3rd minute
CAR_STEP = 1

carSprites = [
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png"),   #    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\зеленая.png"),  обрезана не так
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\GreenCar.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")
]


def move_r(yr, h, step):  # управляемое движение машинки
    if event.key == pygame.K_UP:
        if (yr - step > 0):
            yr -= step
    if event.key == pygame.K_DOWN:
        if (yr + h + step < screenY):
            yr += step
    return (yr)


def load_random_car_sprite():   # выбираем  случайный спрайт для машинки

    random_sprite_index = random.randint(0, len(carSprites) - 1)
    random_sprite = carSprites[random_sprite_index]

    return random_sprite

#стоп1

def get_random_lane():   # выбираем случайную полосу
    lane = random.randint(0, 5)
    if lane == 0:
        lane = 100
    elif lane == 1:
        lane = 200
    elif lane == 2:
        lane = 300
    elif lane == 3:
        lane = 400
    elif lane == 4:
        lane = 500
    elif lane == 5:
        lane = 600
    return lane   # (100 + 100 * lane) не робит, ибо далековато уходят


carsX = []
carsY = []
carsSprite = []

prizeSprite = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")
prizeX = screenX - 20
prizeY = get_random_lane()   # выбираем случайную линию для приза


def append_random_car():   # выбираем случайную X - координату для встречной машинки

    x = screenX + random.randint(0, 300) if len(carsX) > 0 else screenX

    carsX.append(x)
    carsY.append(get_random_lane())
    carsSprite.append(load_random_car_sprite())    # добавляем в списки данные


def crash(yr,player_x, carsX, carsY, game_over):   # столкновение
    for i in range(len(carsY)):
        if player_x == carsX[i]:   #and yr == carsY[i] не робит, ибо координаты кривые получились
            game_over  = True
    return game_over



my_font = pygame.font.SysFont("Calibri", 20, bold=False, italic=False)
text1 = my_font.render('Подождите для возвращения в меню',True, THECOLORS['white'])

def death(gameover,text1):
    screen.blit(gameover,[100,80])
    screen.blit(text1,[100, 500])   # координаты примерные, исправлю, когда заработает
    pygame.display.flip()
    pygame.time.delay(500)
    run = False
    return run

clock = pygame.time.Clock()
timerSeconds = 0

append_random_car()

run = True
while run == True:
    screen.blit(background_image, (0, 0))
    clock.tick(FPS)

    timerSeconds = timerSeconds + 1 if timerSeconds < TICKER_MAX_COUNT else 1

    if timerSeconds % (FPS * 4) == 0:   # добавляем встречные машины каждые 4 секунды
        kolvo = random.randint(1,5)
        for i in range(1,kolvo+1):
            append_random_car()

    carsIndexesToDelete = []

    for i in range(len(carsX)):
        carsX[i] -= CAR_STEP
        screen.blit(carsSprite[i], (carsX[i], carsY[i]))

        if carsX[i] < - 200:   # машинки пропадают при достижении левого края (заежзая за экран)
            carsIndexesToDelete.append(i)

        # todo поверка на столкновение каждой машинки с игроком по координатам
        # с помощью screen.blit можно сделать экран смерти
        # просто в конце ставишь скрин блит с картинкой во весь экран

    for i in carsIndexesToDelete:
        del carsX[i]
        del carsY[i]
        del carSprites[i]

    prizeX -= CAR_STEP
    screen.blit(prizeSprite, (prizeX, prizeY))
    # screen.blit(player_sprite, (player_x, player_y))
chet = 0
#text1 = my_font.render(chet,True, THECOLORS['white'])

    # todo проверка по кординатам на столкновение монеты с игроком
def prize_delete(player_x, player_y, prizeX, prizeY, chet):
    if player_x == prizeX and player_y == prizeY:
        chet += 1
    return chet

    # todo вывод счета монеток
    # todo проверка что монетка на экране, а если нет, то закидываем ее вправо

    game_over = crash(yr,player_x, carsX, carsY,game_over)
    if game_over == True:
        run = death(gameover,text1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            yr = move_r(yr, h, step)
    screen.blit(player_sprite,(player_x,yr))
    pygame.display.flip()

pygame.quit()
