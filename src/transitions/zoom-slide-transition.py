from manim import *
import numpy as np

class TrasitionSlide(Animation):
    def __init__(self, mobject, next_slide, **kwargs):
        super().__init__(mobject, **kwargs)
        self.next_slide = next_slide

    def begin(self):

