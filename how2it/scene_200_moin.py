import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Chapter_200_Moin(Slide):
    def construct(self):
        slide = BasicSlide("Moin!", count)

        self.add(slide)
        self.pause()
        self.wait()

        bup = BulletList(["Moin!", "Jan Bielawa", "Timeline", "Bias Disclaimer"])
        bup.save_state()

        arrow = Arrow(start=SEPARATOR_TOP, end=SEPARATOR_BOT)
        t_time = Text("t").next_to(arrow, DOWN)
        notches_pos = [arrow.point_from_proportion(i) for i in np.linspace(0.1, 0.9, 4)]
        stretch = (0.2, 0, 0)
        notches = [Line(start=p - stretch, end=p + stretch) for p in notches_pos]

        timeline_texts = [
            "Abi 2019",
            "Gründung NULL e.V.",
            "Studium bis 2025",
            "Grafschafter Nachrichten",
        ]
        timeline_points = VGroup()
        for num, t in enumerate(timeline_texts):
            timeline_points += Text(t).next_to(notches[num])
        img = ImageMobject("assets/symbolbild_studieren.jpg").scale(0.7).to_edge(LEFT)

        disclaimer_texts = [
            "5 Jahre nur von Nerds umgeben",
            "Linux Mensch, liebe FOSS",
            "Leidenschaftlicher Hass auf\nGoogle, MS, Facebook, etc.",
        ]

        disclaimers = BulletList(disclaimer_texts).to_edge(RIGHT).set_y(0)
        sep = Line(SEPARATOR_TOP, SEPARATOR_BOT).shift(0.6 * LEFT)
        self.add(bup)
        self.wait()
        self.play(
            bup[2].animate.set_color(c.Colors.accent1),
            Create(arrow),
            Write(t_time),
            *[Create(notch) for notch in notches],
        )

        self.wait()
        for i, p in enumerate(timeline_points):
            if i == 2:
                self.play(Write(p), GrowFromCenter(img))
                self.wait(0.2)
                self.pause()
                self.play(ShrinkToCenter(img))
                self.wait(0.2)
                self.pause()
            else:
                self.play(Write(p))
                self.wait(0.2)
                self.pause()
        self.wait()
        self.play(
            *[Uncreate(i) for i in [arrow, t_time, *notches, timeline_points]],
            Restore(bup),
        )

        self.play(bup[3].animate.set_color(c.Colors.accent1))
        self.wait(0.2)
        self.pause()
        self.play(Write(disclaimers), Create(sep))
        self.wait(0.2)
        self.pause()
        self.wait()
