from manim import *

import src.config.config as c

class BulletList(VMobject):
    def __init__(self, bulletpoints:list[str], **kwargs):
        super().__init__(**kwargs)

        self.bulletpoints = bulletpoints
        self.dots = self.__make_points()
        self.texts = self.__make_text()
        self.lineheights = self.__get_line_heights()

        self.__align_elements()
        self.add(self.dots, self.texts)

    @property
    def num_of_bulletpoints(self):
        return len(self.bulletpoints)

    def __make_points(self):
        ret = VGroup()
        for _ in range(self.num_of_bulletpoints):
            ret += Dot(radius=c.Text.font_size/450, color=c.Colors.text)
        return ret

    def __make_text(self):
        ret = VGroup()
        for i in self.bulletpoints:
            ret += Text(i, font=c.Bulletpoints.font, font_size=c.Bulletpoints.font_size, line_spacing=0.5)
        ret.arrange(DOWN, buff=c.Bulletpoints.vertical_spacing, aligned_edge=LEFT)
        ret.move_to((-5.5, 2.5, 0), UL)
        return ret

    def __align_elements(self):
        for i in range(self.num_of_bulletpoints):
            self.dots[i].next_to(self.texts[i], UL).shift(DOWN*0.5)

    def __get_line_heights(self):
        pass
