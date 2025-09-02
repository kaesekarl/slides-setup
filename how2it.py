from setup import *

class Intro(Slide):
    def construct(self):
        titleslide = TitleSlide("How2IT", "Ein Rundumschlag über alles mit Computern", "Jan Bielawa")

        self.add(titleslide)
        self.wait()
        self.pause()
        self.remove(titleslide)

        tocslide = BasicSlide("Inhalt")
        toc = BulletList(["Moin",
                            "Motivation\nress\ntest",
                            "Gute Programme",
                            "Text Based Files",
                            "Best Practices"])

        self.add(tocslide, toc)
        self.add(SurroundingRectangle(toc.texts[1]))

        self.wait()
        self.pause()
        self.wait()
