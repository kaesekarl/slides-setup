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

tracker_current_slide_mobject = None

####################################################################################################################################################
# Begin File
####################################################################################################################################################

class Scene1(Scene):
    def construct(self):
        self.add(TitleSlide(title=["Dies ist ein Titel", "für meine Präsentation"],
                            subtitle=["Das hier ist der Untertitel.", "Dies ist zum testen für sehr lange Untertitel"],
                            author="Jan Bielawa")
                            .make_all())

class Scene2(Scene):
    def construct(self):
        count = Counter(1, 10)
        self.add(BasicSlide("Testg", count).make_all())
        dots = VGroup()
        for i in range(-6, 7):
            for j in range(-3, 4):
                if i == 0 or j == 0:
                    dots += Dot((i, j, 0), color=RED)
                else:
                    dots += Dot((i, j, 0))
        self.play(Create(dots), run_time=2, lag_ratio=1/len(dots))
        self.wait(2)

class Scene3(Slide):
    def construct(self):
        pass

class Scene4(Scene):
    def construct(self):
        count = Counter(currentSlide=1, maxSlides=10)

        scenes = VGroup()
        for i in range(4):
            i += 1
            sl = BasicSlide(f"Test Nummer {i}", count).make_all()
            rec = SurroundingRectangle(sl, color=c.Colors.white_muted, buff=MED_LARGE_BUFF)
            scenes += VGroup(sl, rec).scale(0.45)
            count.inc_slide()

        scenes.arrange_in_grid(2, 2).center()
        self.play(Create(scenes), lag_ratio=1/len(scenes))
        self.wait(2)

# with tempconfig({"quality": "high_quality", "preview": True}):
#     scene = Scene2()
#     scene.render()
