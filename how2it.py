from setup import *

class Intro(Slide):
    def construct(self):
        # title = TitleSlide("How2IT", "Wie man Computer richtig benutzt", "Jan Bielawa")
        #
        # self.add(title)
        # self.wait()
        # self.pause()
        # self.clear()
        #
        # toc = BasicSlide("Inhalt")
        # self.add(toc)
        # bp = ["Moin!",
        #       "Motivation",
        #       "Gute Programme",
        #       "Best Practices",
        #       "Fragerunde"]
        # bp = VGroup(*[Text(i).scale(0.8) for i in bp]).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=2)
        # self.play(Write(bp))
        #
        # arrow = Arrow().next_to(bp[0], LEFT).set_color(c.Colors.accent1).set_y(5)
        # self.play(Create(arrow))
        # self.wait()
        # self.pause()
        #
        # for i in bp:
        #     self.play(arrow.animate.set_y(i.get_y()))
        #     self.wait()
        #     self.pause()
        #
        # self.clear()
        #
        moin = BasicSlide("Moin!")
        self.play(Create(moin))

        test = BulletList([
            "Test",
            "Ein Test mit tiefen buchstaben g und am besten auch noch\nüberlang, also sowas hier zum beispiel\nhoffentlich läuft das nicht über g",
            "Noch ein Test",
        ])
        self.add(test)


        self.wait()
