import re
from typing import Iterable, cast

from manim import *

import src.config.config as c


class BulletList(VMobject):
    def __init__(self, bulletpoints: list[str], **kwargs):
        super().__init__(**kwargs)

        self.__inv_ident = "|g"
        self.bulletpoints = bulletpoints
        self.texts = self.__make_text(self.bulletpoints)
        self.dots = self.__make_points()

        self.__align_elements()
        self.add(self.dots, self.texts)

    def __getitem__(self, index):
        """
        returns the List Item specified by the index, going from 0 to len-1
        """
        if 0 <= index < len(self.dots):
            texts_iterable = cast(Iterable[VMobject], self.texts[index])
            dots_iterable = cast(Iterable[VMobject], self.dots[index])

            return VGroup(*texts_iterable, *dots_iterable)
        else:
            raise IndexError("Index out of range")

    @property
    def num_of_bulletpoints(self):
        return len(self.bulletpoints)

    def __add_invisible_identifier(self, bulletpoints: list[str]):
        ret = []
        for point in bulletpoints:
            lines = point.splitlines()
            new_point = [f"{self.__inv_ident}{line}" for line in lines]
            ret.append("\n".join(new_point))
        return ret

    def __make_points(self):
        ret = VGroup()
        for _ in range(self.num_of_bulletpoints):
            ret += Dot(radius=c.Text.font_size / 450, color=c.Colors.text)
        return ret

    def __make_text(self, bulletpoints):
        bulletpoints = self.__add_invisible_identifier(bulletpoints)
        ret = VGroup()
        for i in bulletpoints:
            point = Text(
                i,
                font=c.Bulletpoints.font,
                font_size=c.Bulletpoints.font_size,
                line_spacing=0.5,
            )
            matches = re.finditer(re.escape(self.__inv_ident), i)
            inv_characters = [[match.start(), match.end()] for match in matches]
            for shift, pos in enumerate(inv_characters):
                if shift != 0:
                    shift += 1 + shift
                point[pos[0] - shift : pos[1] - shift].set_opacity(0)
            ret += point

        ret.arrange(DOWN, buff=c.Bulletpoints.vertical_spacing, aligned_edge=LEFT)
        ret.move_to((-6.0, 2.5, 0), UL)
        return ret

    def __align_elements(self):
        for i in range(self.num_of_bulletpoints):
            self.dots[i].next_to(self.texts[i], LEFT, aligned_edge=UL).shift(
                DOWN * 0.1 + RIGHT * 0.35
            )
