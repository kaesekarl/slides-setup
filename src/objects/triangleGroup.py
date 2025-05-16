from manim import *

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
        self.sectors = []

        # add all relavant mobjects 
        self.add(self.tri)

        if draw_labels:
            self.add(*self.labels)

        if draw_sectors:
            self.add(*self.sectors)

    def get_center(self):
        return self.tri.get_center_of_mass()

    def __get_corner(self, vertex:int):
        return self.tri.point_from_proportion(vertex/3)

    def __color_sector(self, vertex, color, distance):
        pass

    def __label_position(self, vertex:int, distance=0.7):
        center_point = self.get_center()
        corner_point = self.tri.__get_corner(vertex)
        vec = corner_point - center_point
        return center_point + vec*distance

