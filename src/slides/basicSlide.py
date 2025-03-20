from manim import *

import src.config.config as c
from src.tools.slideCounter import Counter

class BasicSlide:
    def __init__(self, title:str="Title", counter:Counter|None=None):
        self.title = title
        self.counter = counter

    def make_title(self, title=None):
        conf = c.BasicSlide.Title
        if title is None:
            title = self.title

        return VGroup(MarkupText(title, color=conf.color, font=conf.font, weight=conf.weight))
    
    def make_counter(self, counter=None):
        if counter is None:
            counter = self.counter
        if counter is None: # check again, because self.counter could also be None
            raise Exception("Counter is None, has to be given via this function or the BasicSlide")
        return counter.make_counter().to_corner(DR)

    def make_separator(self):
        conf = c.BasicSlide.Separator
        return VGroup(DashedLine(start=[-6, 3.2, 0], end=[6, 3.2, 0], color=conf.color))

    def make_all(self) -> VGroup:
        """
        Creates all provided VMobjects. If no Counter is specified in the Object, it is omitted.
        """
        conf = c.BasicSlide
        sep = self.make_separator()
        title = self.make_title().scale(conf.Title.size).align_to(sep, LEFT).align_to(sep, DOWN).shift(UP*0.1+RIGHT*0.2)

        if self.counter is None:
            return VGroup(sep, title)

        count = self.make_counter()
        return VGroup(sep, title, count)

