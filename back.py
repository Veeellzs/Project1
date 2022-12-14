import pygame, random, time
pygame.init()
from pygame.color import THECOLORS

screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("My game")

step = 100  # шаг / смещение на 1 полосу   (93)
h = 120  # высота машинки игрока
yr = 400  # Y-координата для машинки игрока   (360)   (верхний левый угол машинки)
player_x = 0   # х - координата игрока
game_over = False   # проигрыш и экран смерти

player_sprite = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")
background_image = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
gameover = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\d55285388e843b575b4b89986ad65ef2.png")
prizeSprite = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")

FPS = 60  # кол - во тиков цикла / кадров в секунду
TICKER_MAX_COUNT = FPS * 60 * 3  # tick count will be set to 0 every 3rd minute
CAR_STEP = 1   # шаг встречной машинки за один тик цикла
speed = 1   # множитель скорости / сложность

carSprites = [
    pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png"),   # список спрайтов
    pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\GreenCar.png"),
    pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png"),
    pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png"),
    pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")]

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
        if player_x + 135 == carsX[i] and yr == carsY[i]:
            game_over  = True
    return game_over

count= 0

def crash_prize(player_x, yr, prizeX, prizeY, count):
    if player_x + 135 == prizeX and yr == prizeY:
        count += 1
        prizeX = - 200
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


clock = pygame.time.Clock()
timerSeconds = 0

# append_random_car()

run = True
carsIndexesToDelete = []  # массив для удаления лишних машинок
while run == True:
    screen.blit(background_image, (0, 0))
    clock.tick(FPS)

    if timerSeconds < TICKER_MAX_COUNT:
        timerSeconds += 1
    else:
        timerSeconds = 1

    if timerSeconds % (FPS * 4) == 0:   # добавляем встречные машины каждые 4 секунды
        kolvo = random.randint(1,5)
        for i in range(1,kolvo+1):
            carsX,carsY,carsSprite = append_random_car(carsX,carsY,carsSprite)



    for i in range(len(carsX)):
        carsX[i] -= CAR_STEP * speed
        screen.blit(carsSprite[i], (carsX[i], carsY[i]))

        if carsX[i] < - 200:   # машинки пропадают при достижении левого края (заежзая за экран)
            del carsX[i]

    prizeX -= CAR_STEP * speed
    prizeX, prizeY, count = crash_prize(player_x, yr, prizeX, prizeY, count)
    screen.blit(prizeSprite, (prizeX, prizeY))


    # score = 0
    text_count = my_font.render("Счет:" + str(count), True, THECOLORS['black'])
    screen.blit(text_count, [20, 30])

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