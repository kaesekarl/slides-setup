####################################################################################################################################################
#Python Imports
####################################################################################################################################################

import numpy as np

####################################################################################################################################################
# Manim Imports
####################################################################################################################################################

from manim import *
from manim_presentation import Slide

####################################################################################################################################################
# Other Imports
####################################################################################################################################################

import src.config.config as c

from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

from src.tools.slideCounter import Counter

####################################################################################################################################################
# Some basic settings for scene. Can be changed. Values should be stored in config
####################################################################################################################################################

config.background_color = c.Slide.Background.color
Text.set_default(font=c.Slide.Text.font)
MarkupText.set_default(font=c.Slide.Text.font)

####################################################################################################################################################
# Some values/states that should be tracked across Classes
####################################################################################################################################################

count = Counter(1, 10)

####################################################################################################################################################
# Begin File
####################################################################################################################################################

class Scene1(Slide):
    def construct(self):
        slide1 = TitleSlide().make_all()
        self.play(Create(slide1))
        self.wait()

        slide2 = BasicSlide("Another Test for stuff", count).make_all()
        self.play(FadeTransformPieces(slide1, slide2), run_time=3)

        self.wait()
        self.pause()
        count.inc_slide()

        self.wait()

# with tempconfig({"quality": "high_quality", "preview": True}):
#     scene = Scene2()
#     scene.render()
