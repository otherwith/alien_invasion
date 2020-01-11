# author:28487
# datetime:2020/1/8 21:42
# software: PyCharm

"""
文件说明：
"""

import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """
        初始化飞船并设置其初始位置
        """
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船你的属性center 中存储小数值
        self.center = float(self.rect.centerx)
        self.high = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        根据移动标识调整飞船的位置
        :return:
        """
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        elif self.moving_up and self.rect.top > 0:
            self.high -= self.ai_settings.ship_speed_factor

        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.high += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.high

    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)
