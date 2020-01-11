# author:28487
# datetime:2020/1/8 21:29
# software: PyCharm

"""
文件说明：
"""


class Settings():
    """存储所有的设置的类"""

    def __init__(self):
        """
        初始化游戏设置
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
