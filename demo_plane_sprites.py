import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed