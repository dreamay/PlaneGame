import pygame
import sys
from demo_plane_sprites import *

pygame.init()

size = width, height = 480, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Demo")
bg = pygame.image.load("images/background.png")
hero = pygame.image.load("images/me1.png")
hero_rect = pygame.Rect(150,500,102,126)
clock = pygame.time.Clock()

enemy = GameSprite("images/enemy1.png")
enemy1 = GameSprite("images/enemy1.png",2)
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出。")
            pygame.quit()
            exit()

    hero_rect.y -=1

    if hero_rect.y <= 0:
        hero_rect.y = 700

    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()


# pygame.quit()