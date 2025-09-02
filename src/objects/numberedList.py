from manim import *
import src.config.config as c

from typing import Dict

class NumberedList(VMobject):
    def __init__(self, bulletpoints:list[str], **kwargs):
        super().__init__(**kwargs)

        self.bulletpoints = bulletpoints
        self.table = self.__make_table()

        self.add(self.__make_table())

    def __make_data(self, bulletpoints_list:list[str]):
        return [[Text(f"{i+1}."), Text(item)] for i, item in enumerate(bulletpoints_list)]

    def __make_table(self) -> VMobject:
        ret = MobjectTable(
            self.__make_data(self.bulletpoints),
            h_buff=0.5,
            v_buff=0.5,
            arrange_in_grid_config={"col_alignments": ["r", "l"]}
        )
        ret.remove(*ret.get_vertical_lines())
        ret.remove(*ret.get_horizontal_lines())

        return ret
