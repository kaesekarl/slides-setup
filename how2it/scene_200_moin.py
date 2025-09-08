import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Moin(Slide):
    def construct(self):
        slide = BasicSlide("Moin!", count)

        self.add(slide)
        self.pause()
        self.wait()

        bup = BulletList(["Moin!", "Jan Bielawa", "Timeline", "Bias Disclaimer"])
        bup.save_state()

        timeline = VGroup()

        arrow = Arrow(start=(0, 3, 0), end=(0, -3, 0))
        t_time = Text("t").next_to(arrow, DOWN)
        notches_pos = [arrow.point_from_proportion(i) for i in np.linspace(0.1, 0.9, 4)]
        stretch = (0.2, 0, 0)
        notches = [Line(start=p - stretch, end=p + stretch) for p in notches_pos]
        point_pos = (3, 2.8, 0)

        timeline_texts = [
            "Abi 2019",
            "Gründung NULL e.V.",
            "Studium bis 2025",
            "Grafschafter Nachrichten",
        ]
        timeline_points = VGroup()
        for num, t in enumerate(timeline_texts):
            timeline_points += Text(t).next_to(notches[num])

        self.add(bup)
        self.wait()
        self.play(
            bup[2].animate.set_color(c.Colors.accent1),
            Create(arrow),
            Write(t_time),
            *[Create(notch) for notch in notches],
        )

        self.wait()
        for p in timeline_points:
            self.play(Write(p))
        self.wait()
        self.play(
            *[Uncreate(i) for i in [arrow, t_time, *notches, timeline_points]],
            Restore(bup),
        )
        self.wait()
