# author:28487
# datetime:2020/1/8 22:11
# software: PyCharm

"""
文件说明：
"""

import sys
import pygame


def check_events():
    """
    响应按键和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    """
    更新屏幕上的图像并切换到新的屏幕上
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()