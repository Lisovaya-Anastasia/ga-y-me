import pygame

FPS = 60
W = 800  # ширина экрана
H = 600  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

play = True  # Переменная для включения главного цикла
motion = 'STOP'  # Переменная для движения круга

_return = 0  # Триггер запуска возврата круга в начальные координаты

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x_start = W // 2
y_start = H // 2
x = W // 2
y = H // 2
r = 10

while play:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
            pygame.quit()
            break
        elif i.type == pygame.KEYDOWN:
            _return = 0
            if i.key == pygame.K_a:
                motion = 'LEFT'
            elif i.key == pygame.K_d:
                motion = 'RIGHT'
            elif i.key == pygame.K_w:
                motion = 'UP'
            elif i.key == pygame.K_s:
                motion = 'DOWN'
            elif i.key == pygame.K_ESCAPE:
                play = False
                pygame.quit()
                break
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                motion = 'STOP'
                _return = 1

    # Движение круга
    if motion == 'LEFT':
        x -= 3
    elif motion == 'RIGHT':
        x += 3
    elif motion == 'UP':
        y -= 3
    elif motion == 'DOWN':
        y += 3

# обработка щелчка мыши
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                attack() # вызывается правой кнопкой мыши
                pygame.display.update()
            elif i.button == 3:
                add_function() #тут будет функция, которая вызывается левой кнопкой мышы
                pygame.display.update()
            elif i.button == 2:
                sc.fill(WHITE)
                pygame.display.update()

    clock.tick(FPS)