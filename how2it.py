from setup import *

class Intro(Slide):
    def construct(self):
        titleslide = TitleSlide("How2IT", "Ein Rundumschlag über alles mit Computern", "Jan Bielawa")

        self.add(titleslide)
        self.wait()
        self.pause()
        self.remove(titleslide)

        tocslide = BasicSlide("Inhalt")
        tocnum = NumberedList(["Moin",
                            "Motivation",
                            "Gute Programme",
                            "Text Based Files",
                            "Best Practices"])

        tocbul = BulletList(["Moin",
                            "Motivation",
                            "Gute Programme",
                            "Text Based Files",
                            "Best Practices"])
        self.add(tocslide)
        for i in range(5):
            self.play(Write(tocnum[i]))

        self.wait()
        self.pause()
        self.wait()
