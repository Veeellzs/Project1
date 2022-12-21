import pygame #импорт библиотеки pygame
pygame.init() #инициализация графического режима
from pygame.color import THECOLORS #импорт стандартных цветовых конста
screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY]) #задаем размеры граф окна
my_font = pygame.font.SysFont("Arial", 24, bold=False, italic=False)
text = my_font.render("", True, THECOLORS['red'])
x = 300
y = 240
dx = 2
dy = 2
r = 20
xr = 750
yr = 200
w = 30
h = 200
step = 30
score = 0
def move_ball(x, y, r, dx, dy, color):
    x += dx
    y += dy
    pygame.draw.circle(screen, color, [x, y], r, 0)
    if (x + r >= screenX or x - r <= 0):
        dx = -dx
    if (y + r >= screenY or y - r <= 0):
        dy = -dy
    return (x, y, dx, dy)

def move_r(yr, h, step):
    if event.key == pygame.K_UP:
       if (yr - step > 0):
        yr -= step
    if event.key == pygame.K_DOWN:
        if (yr + h + step < screenY):
            yr += step
    return (yr)


def check_collision(x, y, r, xr, yr, w, h, dx, score):
    if (y >= (yr - r)) and (y <= (yr + h)) and (x >= (xr - r)) and (x <= (xr + w + r)):
        dx = -dx
        score += 1

    return (dx, score)

run = True
my_delay = 100
interval = 50
while run == True: #пока переменная run равна True
    screen.fill(THECOLORS['white'])
    x, y, dx, dy = move_ball(x, y, r, dx, dy, THECOLORS["green"])

    dx, score = check_collision(x, y, r, xr, yr, w, h, dx, score)
    text = my_font.render("Счет:" + str(score), True, THECOLORS['red'])
    screen.blit(text, [200, 50])
    pygame.time.delay(10)
    for event in pygame.event.get(): #просматриваем очередь событий
        if event.type == pygame.QUIT: #если был нажат крестик
            run = False #выходим из цикла
        elif event.type == pygame.KEYDOWN:
            yr = move_r(yr, h, step)
    pygame.draw.rect(screen, THECOLORS["yellow"], [xr, yr, w, h],  0)
    pygame.display.flip()
pygame.quit()#закрываем окно и завершаем работу приложения