# author:28487
# datetime:2020/1/8 21:12
# software: PyCharm

"""
文件说明：
"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    初始化游戏，并创建一个屏幕对象
    :return:
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    bg_color = ai_settings.bg_color

    ship = Ship(screen)

    # 开始游戏主循环 
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()

        gf.update_screen(ai_settings,screen,ship)


run_game()
