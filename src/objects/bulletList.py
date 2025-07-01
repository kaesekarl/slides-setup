from manim import *

import src.config.config as c

class BulletList(VMobject):
    def __init__(self, bulletpoints:list[str], **kwargs):
        super().__init__(**kwargs)
        self.bulletpoints = bulletpoints
        self.num_of_bulletpoints = len(bulletpoints)

    def make_points():
        pass
