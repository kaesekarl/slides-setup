# This is the Title Slide for a Presentation. It should be used for the Starting Slide of the Presentation

from manim import *

import src.config.config as s

class TitleSlide:
    """
    This Class is used to Create a TitleSlide. It is intended to be used as the first Slide in a Presentation.
    It Contains a Title, a Subtitle and an Author. 
    If one (or multiple) of those aren't needed, give an empty String as a Parameter.
    The Colors, fonts, sizes, etc. are derived from the config.py.
    """

    def __init__(self, title:str | list[str]="Title", subtitle:str | list[str]="Subtitle", author:str | list[str]="Author"):
        """
        Parameters
        ----------
        title : str | list
            The Title of the Presentation
        subtitle : str | list
            The Subtitle of the Presentation
        author : str | list
            The Author of the Presentation
        """

        self.title = title
        self.subtitle = subtitle
        self.author = author

    def make_title(self, title=None) -> VGroup:
        if title is None:
            title = self.title
        conf = s.TitleSlide.Title

        if type(title) is str:
            return VGroup(MarkupText(title, color=conf.color))

        if type(title) is list:
            ret = VGroup(*[MarkupText(i, color=conf.color, font=conf.font, weight=conf.weight) for i in title]).arrange(DOWN, aligned_edge=conf.alignment)
            return ret
        raise Exception(f"make_title needs a str or List[str] as title-parameter but is {type(title)}")

    def make_subtitle(self, subtitle=None) -> VMobject:
        if subtitle is None:
            subtitle = self.subtitle
        conf = s.TitleSlide.Subtitle

        if type(subtitle) is str:
            return VGroup(MarkupText(subtitle, color=conf.color))

        if type(subtitle) is list:
            ret = VGroup(*[MarkupText(i, color=conf.color, font=conf.font, weight=conf.weight) for i in subtitle]).arrange(DOWN, aligned_edge=conf.alignment)
            return ret

        raise Exception(f"make_subtitle needs a str or List[str] as subtitle-parameter but is {type(subtitle)}")

    def make_author(self, author=None) -> VMobject:
        if author is None:
            author = self.author
        conf = s.TitleSlide.Author

        if type(author) is str:
            return VGroup(MarkupText(author, color=conf.color))

        if type(author) is list:
            ret = VGroup(*[MarkupText(i, color=conf.color, font=conf.font, weight=conf.weight) for i in author]).arrange(DOWN, aligned_edge=conf.alignment)
            return ret

        raise Exception(f"make_subtitle needs a str or List[str] as subtitle-parameter but is {type(author)}")

    def make_separator(self) -> VMobject:
        conf = s.TitleSlide.Separator
        ret = DashedLine(start=[-6, 1, 0], end=[6, 1, 0], color=conf.color)
        return ret

    def make_all(self) -> VGroup:
        sep = self.make_separator()
        title = self.make_title().scale(s.TitleSlide.Title.size).align_to(sep, DOWN).align_to(sep, RIGHT).shift(0.3*UP+0.5*LEFT)
        subtitle = self.make_subtitle().scale(s.TitleSlide.Subtitle.size).align_to(sep, UP).align_to(sep, LEFT).shift(0.3*DOWN+0.5*RIGHT)
        author = self.make_author().scale(s.TitleSlide.Author.size).next_to(subtitle, DOWN).align_to(subtitle, LEFT)

        ret = VGroup(sep, title, subtitle, author)
        return ret


