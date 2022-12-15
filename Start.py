import os.path
import pygame, random
pygame.init()
from pygame.color import THECOLORS

#pygame.mixer.music.load(r"C:\Users\User\Desktop\для проекта\zvuki-na-ulice-goroda.mp3") #звук

screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX, screenY])

player_x = 0
player_y = 360

h = 120        # ширина машинки
width = 135    # длина машины

step = 93      # шаг / смещение на 1 полосу
stepLeft = 10  # шаг / движение встречных машин
speed = 0.2   # уровень сложности - скорость встречных машин

X = []   # список координат и спрайтов для встречных машин
z = 0   # переменная для случайного кол-ва машинок

# загрузка спрайтов
# prize = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\free-png.ru-52-340x340.png")
# car1 = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\бмв.png")
# carA = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\красная.png")
# carB = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\зеленая.png")
# carC = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\желтая.png")
# carD = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\розовая.png")
# carE = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\серая.png")
# background_image = pygame.image.load(r"C:\Users\User\Desktop\для проекта\рисунки\yol.png")
prize = pygame.image.load(os.path.join("./рисунки/free-png.ru-52-340x340.png"))
car1 = pygame.image.load(os.path.join("./рисунки/бмв.png"))
carA = pygame.image.load(os.path.join("./рисунки/красная.png"))
carB = pygame.image.load(os.path.join("./рисунки/зеленая.png"))
carC = pygame.image.load(os.path.join("./рисунки/розовая.png"))
carD = pygame.image.load(os.path.join("./рисунки/желтая.png"))
carE = pygame.image.load(os.path.join("./рисунки/серая.png"))
background_image = pygame.image.load(os.path.join("./рисунки/yol.png"))
pygame.display.set_caption('Game')

# def move_r(player_y, h, step):   #движение машинки (не надо пока)
#     if event.key == pygame.K_UP:
#         if (yr - step > 0):
#             yr -= step
#     if event.key == pygame.K_DOWN:
#         if (yr + h + step < screenY):
#             yr += step
#     return (yr)
def generate(X, z, cycleTick):   # генерация встречных машин
    if cycleTick == 180:   # генерация раз в три секунды
        z = random.randint(1, 5)    # количество машин
        C = list(range(1, z + 1))  # выбор полосы
        random.shuffle(C)   # чтобы цифры не повторялись
        for i in range(z):
            if C[i] == 1:   # ставим машинки по полосам
                X.append(carA)
                X.append(90)
                X.append(700)
            elif C[i] == 2:
                X.append(carB)
                X.append(200)
                X.append(700)
            elif C[i] == 3:
                X.append(carC)
                X.append(450)
                X.append(700)
            elif C[i] == 4:
                X.append(carD)
                X.append(590)
                X.append(700)
            elif C[i] == 5:
                X.append(carE)
                X.append(290)
                X.append(700)
            elif C[i] == 6:
                X.append(car1)   # спрайт
                X.append(700)   # у-координата
                X.append(700)   # х-координата
            for k in range(z*3):
                if k % 3 == 0:
                    X[k] = random.randint(1, 240)   # разные X-координаты
            return (X, z)

clock = pygame.time.Clock()
cycleTick = 0

run = True
while run:
    screen.blit(background_image, (0, 0))
    clock.tick(60)
    cycleTick = cycleTick + 1 if cycleTick < 180 else 0

    X, z = generate(X, z, cycleTick)
    for i in range(z*3):    # z*3 = количеству элементов списка Х
        if i == 3:
            X[i] = X[i]+1*speed   # шобы ехали
        elif i == 1:
            screen.blit(X[i], (X[i+2], X[i]+1))   # отрисовка на экран

    # for i in range(z):   #задаем неуправляемое движение
    #     C1 = random.randint(1,6)
    #     if C1 == 1:
    #         X[i] += speed * stepLeft
    #         screen.blit(carA, (X[i], Y[i]))
    #     elif C1 == 2:
    #         X[i] += speed * stepLeft
    #         screen.blit(carB,(X[i],Y[i]))
    #     elif C1 == 3:
    #         X[i] += speed * stepLeft
    #         screen.blit(carC,(X[i],Y[i]))
    #     elif C1 == 4:
    #         X[i] += speed * stepLeft
    #         screen.blit(carD,(X[i],Y[i]))
    #     elif C1 == 5:
    #         X[i] += speed * stepLeft
    #         screen.blit(carE,(X[i],Y[i]))
    #     elif C1 == 6:
    #         X[i] += speed * stepLeft
    #         screen.blit(prize,(X[i],Y[i]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     yr = move_r(yr, h, step)
    pygame.display.flip()
pygame.quit()
