from manim import *

import src.config.config as c

class BulletList(VMobject):
    def __init__(self, bulletpoints:list[str]|None, **kwargs):
        super().__init__(**kwargs)
        self.bulletpoints = bulletpoints

    def make_points():
        pass
