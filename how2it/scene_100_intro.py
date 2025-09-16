import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Chapter_100_Intro(Slide):
    def construct(self):
        titleslide = TitleSlide(
            "How2IT", "Ein Rundumschlag über alles mit Computern", "Jan Bielawa"
        )

        self.add(titleslide)
        self.wait()
        self.pause()
        self.remove(titleslide)

        tocslide = BasicSlide("Inhalt")
        tocnum = NumberedList(
            [
                "Moin",
                "Motivation",
                "Gute Programme",
                "Text Based Files",
                "Best Practices",
                "Outro",
            ]
        )

        self.add(tocslide)
        self.add(tocnum)

        self.wait()
        self.pause()
        self.wait()
