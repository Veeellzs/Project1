import os.path

import pygame, random, time
pygame.init()
from pygame.color import THECOLORS

screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("My game")


def load_sprite(path):
    return pygame.image.load(os.path.join(path))

step = 100  # шаг / смещение на 1 полосу   (93)
h = 120  # высота машинки игрока
yr = 400  # Y-координата для машинки игрока   (360)   (верхний левый угол машинки)
player_x = 0   # х - координата игрока
game_over = False   # проигрыш и экран смерти

player_sprite = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")
background_image = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
gameover = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\d55285388e843b575b4b89986ad65ef2.png")
winner = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\victory.png")
prizeSprite = load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")

FPS = 60  # кол - во тиков цикла / кадров в секунду
TICKER_MAX_COUNT = FPS * 4  # tick count will be set to 0 every 4th second
CAR_STEP = 1   # шаг встречной машинки за один тик цикла
speed = 3   # множитель скорости / сложность

carSprites = [
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png"),   # список спрайтов
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\GreenCar.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png"),
    load_sprite(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")]

def move_r(yr, h, step):  # управляемое движение машинки
    if event.key == pygame.K_UP:
        if (yr - step > 0):
            yr -= step
    if event.key == pygame.K_DOWN:
        if (yr  + step < screenY):
            yr += step
    return (yr)


def load_random_car_sprite():   # выбираем  случайный спрайт для машинки

    random_sprite_index = random.randint(0, len(carSprites) - 1)
    random_sprite = carSprites[random_sprite_index]

    return random_sprite

def get_random_lane():   # выбираем случайную полосу и в lane присваиваем У - координату
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
    return lane


carsX = []   # список Х - координат встречных машинок
carsY = []   # список У - координат встречных машинок
carsSprite = []   # список спрайтов встречных машинок

prizeX = screenX - 20
prizeY = get_random_lane()   # выбираем случайную линию для приза

def append_random_car(carsX,carsY,carsSprite):   # выбираем случайную X - координату для встречной машинки

    x = screenX + random.randint(0, 200) if len(carsX) > 0 else screenX

    carsX.append(x)
    carsY.append(get_random_lane())
    carsSprite.append(load_random_car_sprite())    # добавляем в списки данные
    return (carsX,carsY,carsSprite)

def crash(yr,player_x, carsX, carsY, game_over):   # столкновение
    for i in range(len(carsY)):
        if carsX[i] < player_x + 120 and carsX[i] > player_x and yr == carsY[i]:
            game_over = True
    return game_over

count= 0

def crash_prize(player_x, yr, prizeX, prizeY, count, carsX, carsY): # собираем монетки
    if prizeX < player_x + 120 and prizeX > player_x and yr == prizeY:
        count += 1
        prizeX = screenX
        prizeY = get_random_lane()
    elif prizeX < 0:
        prizeX = screenX + 20
        prizeY = get_random_lane()
    for i in range(len(carsY)): #делаем проверку чтобы монетка не накладывалась на машинки
        while prizeY == carsY[i] and prizeX > carsX[i] - 50:
            prizeY = get_random_lane()
    return prizeX, prizeY, count

my_font = pygame.font.SysFont("Calibri", 40, bold=False, italic=False)
text1 = my_font.render('Подождите для возвращения в меню',True, THECOLORS['white'])

def death(gameover,text1):
    screen.blit(gameover,[100,80])
    screen.blit(text1,[100, 500])
    pygame.display.flip()
    pygame.time.delay(500)
    run = False
    return run

timerSeconds1 = 0
stopcount = 0
speed_text1 = 'l'
def speedy(speed, count,timerSeconds1, stopcount, TICKER_MAX_COUNT, speed_text1): #сложность, ускорение
    if timerSeconds1 % 600 == 0:
        speed += 1
        speed_text1 = my_font.render("Ускорение", True, THECOLORS['black'])
    if timerSeconds1 % 900 == 0:
        if TICKER_MAX_COUNT > 60:
            TICKER_MAX_COUNT -= 30
            print(TICKER_MAX_COUNT)
    if count > 0 and count % 5 == 0 and count != stopcount:
        speed -= 1
        speed_text1 = my_font.render("Замедление", True, THECOLORS['black'])
        stopcount = count
    return speed, count, stopcount, TICKER_MAX_COUNT, speed_text1


def win(count, run): # победа
    screen.blit(winner,[0,0])
    pygame.display.flip()
    pygame.time.delay(3000)
    run = False
    return run


timerSeconds2 = 0
Seconds = 0
Minutes = 0
def timers(timerSeconds2, Seconds, Minutes):
    if timerSeconds2 == 60:
        if Seconds < 60:
            Seconds += 1
        else:
            Seconds = 0
            Minutes += 1
        if Minutes == 60:
            Minutes = 0
        timerSeconds2 = 0
    return Seconds, Minutes, timerSeconds2





clock = pygame.time.Clock()
timerSeconds = 0

# append_random_car()

run = True
while run == True:
    screen.blit(background_image, (0, 0))


    clock.tick(FPS)

    timerSeconds1 += 1
    timerSeconds2 += 1

    if timerSeconds <= TICKER_MAX_COUNT:
        timerSeconds += 1
    else:
        timerSeconds = 1

    if timerSeconds % (TICKER_MAX_COUNT) == 0:   # добавляем встречные машины каждые N секунды
        kolvo = random.randint(1,5)
        for i in range(1,kolvo+1):
            carsX,carsY,carsSprite = append_random_car(carsX,carsY,carsSprite)

    carsIndexesToDelete = []  # массив для удаления лишних машинок



    speed, count, stopcount, TICKER_MAX_COUNT, speed_text1 = speedy(speed, count, timerSeconds1, stopcount, TICKER_MAX_COUNT, speed_text1)

    for i in range(len(carsX)):
        carsX[i] -= CAR_STEP * speed
        screen.blit(carsSprite[i], (carsX[i], carsY[i]))

        if carsX[i] < - 200:   # машинки пропадают при достижении левого края (заежзая за экран)
            carsIndexesToDelete.append(i)



    for i in carsIndexesToDelete:   # удаляем из каждого списка данные для проехавших машинок
        del carsX[i]
        del carsY[i]
        del carsSprite[i]

    prizeX -= CAR_STEP * speed
    prizeX, prizeY, count = crash_prize(player_x, yr, prizeX, prizeY, count, carsX, carsY)
    screen.blit(prizeSprite, (prizeX, prizeY))


    text_count = my_font.render("Счет:" + str(count), True, THECOLORS['black'])
    screen.blit(text_count, [20, 30])


    Seconds, Minutes, timerSeconds2 = timers(timerSeconds2, Seconds, Minutes)
    timer_text =my_font.render(str(Minutes) + ":" + str(Seconds), True, THECOLORS['black'])
    screen.blit(timer_text, [800, 30])

    # screen.blit(speed_text1, [430, 30])   # не работает, 1st argument must be surface, not str

    if count >= 50:
        run = win(count, run)

    game_over = crash(yr, player_x, carsX, carsY, game_over)
    if game_over == True:
        run = death(gameover, text1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            yr = move_r(yr, h, step)
    screen.blit(player_sprite, (player_x, yr))

    pygame.display.flip()

pygame.quit()