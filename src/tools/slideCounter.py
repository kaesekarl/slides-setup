from manim import *
import src.config.config as c

class Counter:
    """
    This Class defines a Counter to keep track on which Slide the Presentation is at the moment.
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

    def inc_slide(self):
        self.currentSlide += 1

    def set_slide(self, number):
        self.currentSlide = number

    def make_counter(self) -> VGroup:
        conf = c.Slide.Counter
        if self.maxSlides < 0:
            text = f"{self.currentSlide}"
        else:
            text = f"{self.currentSlide}/{self.maxSlides}"
        return VGroup(MarkupText(text, color=conf.color, font=conf.font, weight=conf.weight).scale(conf.size))

    def make_progress_bar(self) -> VGroup:
        conf = c.Slide.Counter.ProgressBar
        if self.maxSlides < 0:
            raise Exception(f"Progressbar cannot be created without a positive maxSlides, maxSlides is {self.maxSlides}")

        start = (-6, -3, 0)
        end = (6, -3, 0)


        bar1 = Line(start, end, line_width=2, color=conf.bar_color1)
        bar2 = Line(start, end, line_width=4, color=conf.bar_color2).set_z_index(1)

        return VGroup(bar1, bar2)

