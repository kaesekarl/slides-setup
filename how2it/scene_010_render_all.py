import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from scene_100_intro import Intro
from scene_200_moin import Moin
from scene_300_motivation import Motivation

from setup import *


class AllAnimations(Slide):
    def construct(self):
        intro = Intro()
        moin = Moin()
        motivation = Motivation()

        intro.construct()
        moin.construct()
        motivation.construct()
