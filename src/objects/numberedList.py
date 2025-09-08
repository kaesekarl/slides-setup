from typing import Dict

from manim import *

import src.config.config as c


class NumberedList(VMobject):
    def __init__(self, bulletpoints: list[str], **kwargs):
        super().__init__(**kwargs)

        self.bulletpoints = bulletpoints
        self.table = self.__make_table().move_to((-6, 2.5, 0), UL)

        self.add(self.table)

    def __getitem__(self, index):
        """
        returns the List Item specified by the index, going from 0 to len-1
        """
        all_entries = self.table.get_entries()
        if 0 <= index < len(all_entries) / 2:
            return VGroup(all_entries[index * 2], all_entries[index * 2 + 1])
        else:
            raise IndexError("index is out of bounds")

    def __make_data(self, bulletpoints_list: list[str]):
        ret = []
        for i, item in enumerate(bulletpoints_list):

            number = f"|g{i+1}."
            number = Text(
                number,
                font=c.NumberedList.font,
                font_size=c.NumberedList.font_size,
                line_spacing=0.5,
            )
            number[0:2].set_opacity(0)

            text = "|g" + item
            text = Text(
                text,
                font=c.NumberedList.font,
                font_size=c.NumberedList.font_size,
                line_spacing=0.5,
            )
            text[0:2].set_opacity(0)

            ret.append([number, text])
        return ret

    def __make_table(self) -> VMobject:
        ret = MobjectTable(
            self.__make_data(self.bulletpoints),
            h_buff=0.0,
            v_buff=0.4,
            arrange_in_grid_config={"col_alignments": ["r", "l"]},
        )
        ret.remove(*ret.get_vertical_lines())
        ret.remove(*ret.get_horizontal_lines())

        return ret
