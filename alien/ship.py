import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        # 初始化飞船并设置其初始位置
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('./images/rocket.png')
        target_size = (200, 200)
        self.image = pygame.transform.scale(self.image, target_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        # 根据移动标志调整飞船的位置
        if self.rect.right < self.screen_rect.right and self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.rect.left > self.screen_rect.left and self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据center更新rect
        self.rect.centerx = self.center

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        # 让飞船屏幕居中
        self.center = self.screen_rect.centerx