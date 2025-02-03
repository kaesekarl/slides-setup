from manim import *
import src.config.config as conf

class Counter:
    """
    This Class defines a Counter to keep track on which Slide the Presentation is at the moment.
    It does not define any Mobjects, use only for Backend-Purposes
    """
    def __init__(self, currentSlide:int=1, maxSlides:int=-1) -> None:
        """
        Parameters
        ----------
        currentSlide : int
            The Slide on which the Counter should be Initialized. Default is 1, since most Presentations start there
        maxSlides : int
            The number of the last Slide. Default is -1, if not set differently, it should be omitted by Mobject-Creating functions
        """
        self.currentSlide = currentSlide
        self.maxSlides = maxSlides

    def inc_Slide(self):
        self.currentSlide += 1
