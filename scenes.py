#Python Imports

# Manim Imports

from manim import *
from manim_presentation import Slide

# Other Imports

import src.config.config as c
from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

config.background_color = c.Slide.Background.color
Text.set_default(font=c.Slide.Text.font)
MarkupText.set_default(font=c.Slide.Text.font)

class Scene1(Slide):
    def construct(self):
        self.add(TitleSlide(title=["Dies ist ein Titel", "für meine Präsentation"],
                            subtitle=["Das hier ist der Untertitel.", "Dies ist zum testen für sehr lange Untertitel"],
                            author="Jan Bielawa")
                            .make_all())

class Scene2(Slide):
    def construct(self):
        self.add(BasicSlide(title="Test").make_all())

class Scene3(Slide):
    def construct(self):
        self.play(Create(Circle()))
        self.play(Create(Square(color=BLUE).shift(UP)))

        self.wait()
        self.pause()

        self.add(Square().shift(DOWN))
        self.play(Create(Circle().to_edge(RIGHT)))

        self.wait()
        self.pause()

        self.play(Create(Square().shift(2*DOWN)))

        self.wait()
        self.pause()

        self.play(Create(Circle().to_edge(LEFT)))
        self.play(Create(Circle().to_edge(UP)))

        self.wait()
        self.pause()
        self.wait()

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Scene2()
    scene.render()
