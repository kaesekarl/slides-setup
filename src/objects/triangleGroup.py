from manim import *

class TriangleGroup:
    def __init__(self, operations:str="") -> None:
        self.tri = Triangle().scale(2)

        self.label_1 = Tex(r"a").add_updater(lambda m: m.move_to(self._label_position(0)))
        self.label_2 = Tex(r"b").add_updater(lambda m: m.move_to(self._label_position(1)))
        self.label_3 = Tex(r"c").add_updater(lambda m: m.move_to(self._label_position(2)))

        if operations is not "":
            self._apply_operations(operations)

        self.all = [self.tri, self.label_1, self.label_2, self.label_3]

        # sector coloring

    @property
    def center(self):
        return self.tri.get_center_of_mass()

    def _get_corner(self, vertex:int):
        return self.tri.point_from_proportion(vertex/3)

    def _color_sector(self, vertex, color, distance):
        angle = Angle(Line(self._get_corner(vertex), ))

    def _label_position(self, vertex:int, distance=0.7):
        center_point = self.tri.get_center_of_mass()
        corner_point = self.tri.point_from_proportion(vertex/3)
        vec = corner_point - center_point
        return center_point + vec*distance

    def _apply_operations(self, operations):
        # still needs some work, if it is not to be removed
        for op in operations[::-1]:
            if op is "r":
                Rotate(self.tri, TAU/3, about_point=[i for i in self.tri.get_center_of_mass()])
            elif op is "m":
                Rotate(self.tri, TAU/2, axis=UP)


