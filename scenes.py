#Python Imports

# Manim Imports

from manim import *
from manim_presentation import Slide

# Other Imports

import src.config.config as conf
from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

config.background_color = conf.Slide.Background.color
Text.set_default(font=conf.Slide.Text.font)
MarkupText.set_default(font=conf.Slide.Text.font)

class Scene1(Slide):
    def construct(self):
        self.add(TitleSlide(title=["Dies ist ein Titel", "für meine Präsentation"],
                            subtitle=["Das hier ist der Untertitel.", "Dies ist zum testen für sehr lange Untertitel"],
                            author="Jan Bielawa")
                            .make_all())

class Scene2(Slide):
    def construct(self):
        self.add(BasicSlide(title="Test"))
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene1()
    scene.render()
