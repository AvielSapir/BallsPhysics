import math
import pygame.draw


class Balls:
    def __init__(self, r_size, posX, posY, velY, velX):
        self.r_size = r_size
        self.posX = posX
        self.posY = posY
        self.velY = velY
        self.velX = velX
        self.elast = 0.8
        self.gravity = 0.001

    def check_collider(self, obj):
        disX = self.posX - obj.posX
        disY = self.posY - obj.posY
        distance = math.hypot(disX, disY)
        if distance <= self.r_size + obj.r_size + 1 and distance != 0:
            # direction
            collider_directionX = disX / distance
            collider_directionY = disY / distance
            # speed
            collider_velocityX = self.velX - obj.velX
            collider_velocityY = self.velY - obj.velY
            # result of collision
            dot_collider = collider_velocityX*collider_directionX + collider_velocityY*collider_directionY
            self.velX -= dot_collider *collider_directionX
            self.velY -= dot_collider * collider_directionY
            obj.velX += dot_collider * collider_directionX
            obj.velY += dot_collider * collider_directionY
            # sticky bug
            overlap = 0.5 * (self.r_size + obj.r_size - distance + 1)
            self.posX += overlap * collider_directionX
            self.posY += overlap * collider_directionY
            obj.posX -= overlap * collider_directionX
            obj.posY -= overlap * collider_directionY
        else:
            return False

    def pos_update(self, balls):
        if self.posY >= 600 - self.r_size:
            self.posY = 600 - self.r_size
            self.velY *= -self.elast
        if self.posY <= 0 + self.r_size:
            self.velY *= -self.elast
        self.velY += self.gravity
        self.posY += self.velY

        if self.posX >= 800-self.r_size:  # or colider(x, objects, velx, vely):
            self.posX = 800-self.r_size
            self.velX *= -self.elast
        if self.posX <= 0 + self.r_size:
            self.posX = 0 + self.r_size
            self.velX *= -self.elast
        # self.velX *= 0.9999
        # if 0 < self.velX <= 0.009 or 0 > self.velX >= -0.009:
        #     self.velX = 0
        self.posX += self.velX

    def ball_draw(self, screen):
        pygame.draw.circle(screen, (150, 150, 150, 0), (self.posX, self.posY), self.r_size)

