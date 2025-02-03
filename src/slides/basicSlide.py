from manim import *

import src.config.config as conf

class BasicSlide:
    def __init__(self, title:str="Title", counter:Counter=None):
        self.title = title
        self.counter = counter

    def make_title(self, title=None):
        if title is None:
            title = self.title

        return VGroup()
    
    def make_counter(self, counter=None):
        if counter is None:
            counter = self.counter

    def make_all(self):
        return None

