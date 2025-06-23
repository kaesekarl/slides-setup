from manim import *
from src.config import config as c

class TriangleGroup(VMobject):
    def __init__(self, draw_labels=False, draw_sectors=True, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tri = Triangle().scale(2)

        # corner labels
        label_1 = Tex(r"a").add_updater(lambda m: m.move_to(self.__label_position(0)))
        label_2 = Tex(r"b").add_updater(lambda m: m.move_to(self.__label_position(1)))
        label_3 = Tex(r"c").add_updater(lambda m: m.move_to(self.__label_position(2)))
        self.labels = [label_1, label_2, label_3]

        # sector coloring
        sector_1 = self.__color_sector(0, RED)
        sector_2 = self.__color_sector(1, RED)
        sector_3 = self.__color_sector(2, c.TriangleGroup.Angles.angle_3)
        self.sectors = [sector_1, sector_2, sector_3]

        # add all relavant mobjects 

        if draw_labels:
            self.add(*self.labels)

        if draw_sectors:
            self.add(*self.sectors)

        self.add(self.tri)

    def get_center(self):
        return self.tri.get_center_of_mass()

    def __get_corner(self, vertex:int):
        vertex = vertex % 3
        return self.tri.point_from_proportion(vertex/3)

    def __color_sector(self, vertex, color):
        corner = self.__get_corner(vertex)
        corner_prev = self.__get_corner(vertex-1)
        corner_next = self.__get_corner(vertex+1)

        line1 = Line(corner, corner_next)
        line2 = Line(corner, corner_prev)
        return Angle(line1, line2, radius=0.3, stroke_width=60, color=color).set_z_index(-1)

    def __label_position(self, vertex:int, distance=0.7):
        center_point = self.get_center()
        corner_point = self.tri.__get_corner(vertex)
        vec = corner_point - center_point
        return center_point + vec*distance

