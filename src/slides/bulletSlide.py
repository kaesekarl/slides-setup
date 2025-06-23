from manim import *

import src.config.config as c
from src.tools.slideCounter import Counter

class BulletSlide(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
