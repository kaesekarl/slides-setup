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
# from src.objects.triangleGroup import TriangleGroup

####################################################################################################################################################
# Some basic settings for scene. Can be changed. Values should be stored in config
####################################################################################################################################################

config.background_color = c.Slide.Background.color
Text.set_default(font=c.Slide.Text.font)
MarkupText.set_default(font=c.Slide.Text.font)

####################################################################################################################################################
# Some values/states that should be tracked across Classes
####################################################################################################################################################

count = Counter(1)

####################################################################################################################################################
# Begin File
####################################################################################################################################################

class Intro(Slide):
    def construct(self):
        title = TitleSlide("How2IT", "Wie man Computer richtig benutzt", "Jan Bielawa")

        self.add(title)
        self.wait()
        self.pause()
        self.clear()

        toc = BasicSlide("Inhalt")
        self.add(toc)
        bp = ["Moin!",
              "Motivation",
              "Gute Programme",
              "Best Practices",
              "Fragerunde"]
        bp = VGroup(*[Text(i) for i in bp]).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=2)

        for i in bp:
            self.play(Write(i))
            self.wait()
            self.pause()




        self.wait()
