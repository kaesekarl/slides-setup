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
# Slides-Setup Imports
####################################################################################################################################################

import src.config.config as c

from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

from src.tools.slideCounter import Counter

from src.objects.triangleGroup import TriangleGroup

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
        slide1 = BasicSlide().make_all()
        self.play(Create(slide1))
        self.wait()

        test = TriangleGroup()

        self.play(*[Create(i) for i in test.all])
        self.play(Rotate(test.tri, TAU/3, about_point=[i for i in test.tri.get_center_of_mass()]))
        self.play(test.tri.animate.scale(0.5))

        self.wait()
        self.pause()

        

        count.inc_slide()

        self.wait()

# with tempconfig({"quality": "high_quality", "preview": True}):
#     scene = Scene1()
#     scene.render()
