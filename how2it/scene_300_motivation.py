import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Motivation(Slide):
    def construct(self):
        slide = BasicSlide("Motivation", count)

        self.add(slide)
        self.pause()
        self.wait()
