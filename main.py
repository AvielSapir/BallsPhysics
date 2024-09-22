import math
import random

import pygame
import balls

screen = pygame.display.set_mode((800, 600))

isRun = True


balls_list = []
for b in range(20):
    ball = balls.Balls(12, random.randint(30, 700), random.randint(30, 600), random.randint(1, 5)/10 -0.3, random.randint(1, 5)/10 -0.3)
    balls_list.append(ball)


while isRun:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                continue
    for i in range(len(balls_list)):
        for j in range(i + 1, len(balls_list)):
            balls_list[i].check_collider(balls_list[j])
            disX = balls_list[i].posX - balls_list[j].posX
            disY = balls_list[i].posY - balls_list[j].posY
            distance = math.hypot(disX, disY)
            if distance > 300:
                x = 0
                a = 0
            elif distance > 200:
                x = 1
                a = 5
            elif distance > 150:
                x = 2
                a = 10
            elif distance > 75:
                x = 3
                a = 25
            elif distance > 50:
                x = 4
                a = 40
            else:
                x = 5
                a = 70
            #pygame.draw.line(screen, (150, 150, 150, a), (balls_list[i].posX, balls_list[i].posY), (balls_list[j].posX, balls_list[j].posY),x)
    for i in balls_list:
        i.pos_update(balls_list)
        i.ball_draw(screen)

    pygame.display.update()
