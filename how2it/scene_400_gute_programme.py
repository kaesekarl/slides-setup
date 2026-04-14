import os
import sys

from click import pause

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Chapter_400_Gute_Programme(Slide):
    def construct(self):
        slide = BasicSlide("Gute Programme", count)

        self.add(slide)
        self.wait()
        self.pause()

        kriterien_positiv = (
            BulletList(["Open Source", "Kostenlos", "Offene Dateiformate", "Cloudlos"])
            .set_color(c.Colors.green_200)
            .to_corner(UL, 1.5)
        )

        kriterien_negativ = (
            BulletList(["Abo-Modelle", "Proprietäre Dateiformate", "Datenkraken"])
            .set_color(c.Colors.red_200)
            .to_corner(UR, 1.5)
        )

        t_kriterien = VGroup(kriterien_positiv, kriterien_negativ)

        self.add(t_kriterien)
        self.wait()
        self.pause()

        self.wait()


class Chapter_410_Gute_Programme(Slide):
    def construct(self):
        slide = BasicSlide("Gute Programme 2", count)

        self.add(slide)
        self.wait()
        self.pause()

        self.remove(slide)
        self.wait()
        self.pause()

        self.wait()
