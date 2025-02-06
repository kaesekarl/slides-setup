from manim import *

import src.config.config as c
from src.tools.slideCounter import Counter

class BasicSlide:
    def __init__(self, title:str="Title", counter:Counter|None=None):
        self.title = title
        self.counter = counter

    def make_title(self, title=None):
        if title is None:
            title = self.title

        return VGroup()
    
    def make_counter(self, counter=None):
        if counter is None:
            counter = self.counter
        if counter is None: # check again, because self.counter could also be None
            raise Exception("Counter is None, has to be given via this function or the BasicSlide")
        return counter.make_counter()

    def make_separator():
        conf = c.BasicSlide.Separator
        return VGroup(DashedLine(start=[-6, 3, 0], end=[6, 3, 0], color=conf.color))

    def make_all(self) -> VGroup:
        sep = self.make_separator()
        title = self.make_title()
        return VGroup(sep, title)

