# print("a")

import pygame

# image_path='/data/data/org.test.myapp/files/app/'

clock=pygame.time.Clock()

pygame.init() # С этого момента происходит разработка игры
screen=pygame.display.set_mode((1920,1080)) # Размер экрана ((600,300),flags=pygame.NOFRAME)
pygame.display.set_caption("Mi First Game RA") # Устанавливаем название окна
icon=pygame.image.load("images/icon.png").convert_alpha() # Создаем переменную "иконки" Берем, например с сайта "https://www.iconfinder.com/"
pygame.display.set_icon(icon) # Устанавливаем иконку для окна игры
# square=pygame.Surface((50, 170)) # surface - поверхность, экран
# square.fill("Blue") # Задаем цвет

# myfont=pygame.font.Font("fonts/Roboto-Medium.ttf",40) #Параметры класса Font() - название шрифта, размер шрифта. Название шрифта берем отсюда "https://fonts.google.com/"
# text_surface=myfont.render("FirstGame", True, "Yellow") #Устанавливаем параметры для текста


Fon=pygame.image.load("images/Fon_Planet.jpg").convert_alpha() # Ищем картинку в гуле в качестве фона и вставляем на задний план
# player=pygame.image.load("images/player_left/player_left1.png") # Создаем переменную игрока (находится в гугле spitesheet, затем вырезаются отдельные картинки снимки анимации)
walk_left=[
    pygame.image.load("images/player_left/player_left1.png").convert_alpha(), #Конвертируем все изображения, чтобы библиотека PyGame проще обрабатывала изображения
    pygame.image.load("images/player_left/player_left2.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left3.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left4.png").convert_alpha(),
]
walk_right=[
    pygame.image.load("images/player_right/player_right1.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right2.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right3.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right4.png").convert_alpha(),
]

ghost=pygame.image.load('images/Ghost.png').convert_alpha()
# ghost_x=2000 # Задаем изначальную позицию приведения (за пределами экрана)
ghost_list_in_game=[] #Создаем список с монстрами


player_anim_count=0
Fon_x=0

player_speed=10 # Задали скорость игрока (изменения переменной)
player_x=800 # Задаем начальную координату игрока
player_y=880 # Вертикальная координата игрока

is_jump=False
jump_count=8 # Высота прыжка


bg_sound=pygame.mixer.Sound("sounds/bg_sound_ogg.ogg")
# bg_sound.play()

ghost_timer=pygame.USEREVENT+1 # Обязательно прибавлять 1, чтобы работало!
pygame.time.set_timer(ghost_timer,5000)

label=pygame.font.Font("fonts/Roboto-Medium.ttf", 100) # Создаем переменную и задаем шрифт (тип шрифта и размер)
lose_lable=label.render('Вы проиграли!', False, 'red') # False означает, что сглаживания шрифта не будет!
restart_lable=label.render('Играть заново!', True, 'blue') # Создаем надпись рестарта
restart_lable_rect=restart_lable.get_rect(topleft=(640,340))

bullets_left=5
bullet=pygame.image.load('images/bullet.png').convert_alpha()
bullets=[]

gameplay=True # Создаем переменную хода игры

running=True
while running:

    # # Любой последующий объект перекрывает собой предыдущий, если они находятся в одинаковых координатах
    # pygame.draw.circle(screen, 'Red', (100, 50), 100)  # Более лаконичная запись (нарисовали круг внутри квадрата)
    # # screen.blit(square, (100,50)) # Выводим на экран прямоугольник, задав координаты его верхнего левого угла (оси начинаются с верхнего левого угла)
    # screen.blit(text_surface, (100,150))
    # screen.blit(player, (100,50))

    screen.blit(Fon, (Fon_x, 0)) # Выводим фон на экран
    screen.blit(Fon,(Fon_x+1920,0)) # Задаем движение фона
    # screen.blit(ghost,(ghost_x,880)) #Убрали строчку кода, так как вместо монстров уже будут "квадраты-границы" врагов
    # screen.blit(walk_right[player_anim_count],(player_x,880)) # Выводим после фона, чтобы фон не перекрывал основного игрока!
    # screen.fill((12, 10, 94))  # (Синий цвет) Создаем цвет фона, передав формат rgb

    if gameplay:
        #Квадратом изображаем границы изображений
        player_rect=walk_left[0].get_rect(topleft=(player_x,player_y)) # Изобразили квадрат вокруг игрока
        ghost_rect=ghost.get_rect(topleft=(2000,880)) # Изобразили квадрат вокруг "врага"

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game): # Перебираем врагов в списке
                screen.blit(ghost,el) # Перебираем "квадраты-границы"
                el.x -=10

                if el.x < -10:
                    ghost_list_in_game.pop(i) # Удаляем врагов, которые вышли за пределы экрана

                if player_rect.colliderect(el): # отслеживаем соприкосновение квадратов
                    gameplay=False # Как только игрок столкнется с врагом игра заканчивается



        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: # Задаем направление взгляда игрока
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x>50:  # Задаем границы, чтобы игрок не выходил за границы
            player_x-=player_speed  # Вычитаем скорость
        elif keys[pygame.K_RIGHT] and player_x<1870:
            player_x+=player_speed  # Уменьшаем скорость

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump=True
        else:
            if jump_count>=-8:
                if jump_count>0:
                    player_y-=(jump_count**2)/2
                else:
                    player_y+=(jump_count**2)/2
                jump_count-=1
            else:
                is_jump=False
                jump_count=8


        if player_anim_count==3: # Чтобы не выйти за границы списка, обнуляем его
            player_anim_count=0
        else:   # Если счетчик не достиг конца списка, добавляем к нему единицу
            player_anim_count+=1

        Fon_x-=2 # Задаем движение заднего фона, скорость 2 смены фона пикселя!
        if Fon_x==-1980: # Как только задний фон сместился на величину экрана, обнуляем значение переменной фона
            Fon_x=0


        if bullets:
            for (i,el) in enumerate(bullets):
                screen.blit(bullet,(el.x, el.y)) # Указываем что снаряд будет находиться по ранее заданной координате игрока
                el.x+=4
        # ghost_x-=10
                if el.x>2000: # Если элемент за границами экрана
                    bullets.pop(i)
                if ghost_list_in_game: # Проверяем существуют ли монстры в игре
                    for (index, ghost_el) in enumerate(ghost_list_in_game): # Перебираем всех монстров в игре
                        if el.colliderect(ghost_el): # Если снаряд столкнулся с монстром
                            ghost_list_in_game.pop(index)  # Удаляем монстра
                            bullets.pop(i) # Удаляем патрон
    else:
        screen.fill((87,88,89)) # Меняем цвет, если игра закончилась
        screen.blit(lose_lable, (640, 640))
        screen.blit(restart_lable,restart_lable_rect)

        mouse=pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]: # За счет этого метода провери соприкасается ли квадрат с координатами мышки!
            # pygame.mouse.get_pressed() - возвращает 3 bool-значения True/False, нажатие ЛКМ, ПКМ или СКМ
            gameplay=True
            player_x=800
            ghost_list_in_game.clear()
            bullets.clear()  # Очищаем список после перезапуска
            bullets_left=5
    # строчка кода pygame.display.update() должна быть предпоследней (последняя - закрытие игры)
    pygame.display.update()  # Постоянно обновляем экран приложения

    for event in pygame.event.get(): # Перебираем полностью все события в pygame
        if event.type==pygame.QUIT: # Если тип действия - это выход, то:
            running=False
            pygame.quit() # Закрываем программу
        # elif event.type==pygame.KEYDOWN: # Меняем цвет по нажатию какой-либо клавиши
        #     if event.key==pygame.K_a:
        #         screen.fill((176, 11, 11))
        if event.type==ghost_timer: # Если время подошло, добавляем монстров в список
            ghost_list_in_game.append(ghost.get_rect(topleft=(2000,880)))

        if gameplay and event.type == pygame.KEYUP and event.key==pygame.K_b and bullets_left>0: # Событие будет осуществляться только в момент отпускания клавиши
            bullets.append(bullet.get_rect(topleft=(player_x+30,player_y+10))) # Каждый раз при нажатии клавиши K мы будем создавать патрон
            bullets_left-=1
    clock.tick(7) # 12 фреймов (смен картинки) за 1 секунду!