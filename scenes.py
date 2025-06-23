####################################################################################################################################################
#Python Imports
####################################################################################################################################################

import numpy as np

####################################################################################################################################################
# Manim Imports
####################################################################################################################################################

from manim import *
from manim_presentation import Slide # I don't use this for the presentation itself, i create separate files in the end (see concat_scenes.py)

####################################################################################################################################################
# Slides-Setup Imports
####################################################################################################################################################

import src.config.config as c

# All kinds of Slide-Types
from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

# All kinds of Tool-Types
from src.tools.slideCounter import Counter

# All kinds of Custom VMobject-Types
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
        slide0 = TitleSlide("Dies ist ein Test für den Titel", "Dies könnte ein funny Subtitle für die Präsi sein", "und so heiße ich")
        slide1 = BasicSlide("Erster Part", count)

        self.play(Write(slide0))
        self.wait()
        self.pause()

        self.play(FadeOut(slide0), FadeIn(slide1), run_time=0.5)
        self.wait()
        self.pause()
        count.inc_slide()

        tri = TriangleGroup()

        self.play(Create(tri))
        self.wait()
        self.pause()
        self.wait()

class Scene2(Slide):
    def construct(self):
        slide0 = BasicSlide("Sinnvolle Programme", count)

        self.play(Write(slide0))
        self.wait()
        self.pause()
        count.inc_slide()

        slide1 = BasicSlide("Sinnfreie Programme", count)

        self.play(FadeOut(slide0), Write(slide1), run_time=0.5)
        self.wait()
        self.pause()
        self.wait()

class Scene3(Slide):
    def construct(self):
        tri = TriangleGroup()
        self.add(tri)
        self.wait()

# with tempconfig({"quality": "high_quality", "preview": True}):
#     scene = Scene1()
#     scene.render()
