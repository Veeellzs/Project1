import pygame, random
pygame.init()
from pygame.color import THECOLORS

screenX = 880
screenY = 700
screen = pygame.display.set_mode([screenX, screenY])

player_x = 0
player_y = 360

h = 120        #ширина машинки
width = 135    #длина машины

step = 93      #шаг / смещение на 1 полосу
stepLeft = 10  #шаг / движение встречных машин
speed = 0.2   #уровень сложности - скорость встречных машин

X = [0] * 6   #X-координата для встречной машины
Y = [0] * 6   #Y-координата для встречной машины
P = [0]*2     #список для машин

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

# def move_r(player_y, h, step):   #движение машинки (не надо пока)
#     if event.key == pygame.K_UP:
#         if (yr - step > 0):
#             yr -= step
#     if event.key == pygame.K_DOWN:
#         if (yr + h + step < screenY):
#             yr += step
#     return (yr)

def generate(X,Y):   #генерация встречных машин
    z = random.randint(1,5)    #количество машин
    C = list(range(1, z + 1))  # выбор полосы
    random.shuffle(C)   # чтобы цифры не повторялись
    for i in range (z):
        if C[i] == 1:   # ставим машинки по полосам
            Y[i] = 90
        elif C[i] ==2:
            Y[i] = 200
        elif C[i] == 3:
            Y[i] = 290
        elif C[i] == 4:
            Y[i] = 450
        elif C[i] == 5:
            Y[i] = 590
        elif C[i] == 6:
            Y[i] = 700
        for j in range(z):
            X[j] = random.randint(1,240)   #разные X-координаты
#       P = [0] * z
        return (X,Y,z)


run = True
while run:
    X, Y, z = generate(X, Y)
    screen.blit(background_image, (0, 0))

    for i in range(z):   #задаем неуправляемое движение для (тут, вероятнее всего, ошибка)
        C1 = random.randint(1,6)
        if C1 == 1:
            X[i] += speed * stepLeft
            screen.blit(carA, (X[i], Y[i]))
        elif C1 == 2:
            X[i] += speed * stepLeft
            screen.blit(carB,(X[i],Y[i]))
        elif C1 == 3:
            X[i] += speed * stepLeft
            screen.blit(carC,(X[i],Y[i]))
        elif C1 == 4:
            X[i] += speed * stepLeft
            screen.blit(carD,(X[i],Y[i]))
        elif C1 == 5:
            X[i] += speed * stepLeft
            screen.blit(carE,(X[i],Y[i]))
        elif C1 == 6:
            X[i] += speed * stepLeft
            screen.blit(prize,(X[i],Y[i]))




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # elif event.type == pygame.KEYDOWN:
        #     yr = move_r(yr, h, step)
    pygame.display.flip()
pygame.quit()










