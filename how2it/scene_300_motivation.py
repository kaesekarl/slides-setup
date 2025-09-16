import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from setup import *


class Chapter_300_Motivation(Slide):
    def construct(self):
        slide = BasicSlide("Motivation", count)
        slide.save_state()
        self.add(slide)
        self.wait(0.2)
        self.pause()

        ein_kleines_rechenbeispiel = (
            Text("Ein kleines Rechenbeispiel")
            .scale(1.2)
            .to_edge(UP, buff=0.2)
            .set_color(c.Colors.accent1)
        )

        annahmen_text = Text("Annahmen")
        underline_annahmen_text = (
            Line(LEFT, RIGHT)
            .set(width=annahmen_text.width * 1.1)
            .next_to(annahmen_text, DOWN, buff=0.1)
        )
        annahmen_text = VGroup(annahmen_text, underline_annahmen_text).move_to(
            (-6, 3, 0), aligned_edge=UL
        )
        wochenstunden = (
            VGroup(
                Text("Wochenstunden:"),
                MathTex(r"50\ \mathrm{Stunden}"),
                Text("davon am PC/Laptop:"),
                MathTex(r"10\ \mathrm{Stunden}"),
                Text("pro Jahr:"),
                MathTex(r"40\ \mathrm{Wochen}"),
                Text("Zeit im Beruf:"),
                MathTex(r"45\ \mathrm{Jahre}"),
            )
            .arrange_in_grid(None, 2, cell_alignment=LEFT)
            .next_to(annahmen_text, DOWN, buff=0.3, aligned_edge=LEFT)
        )
        underline_wochenstunden = (
            Line(LEFT, RIGHT)
            .set(width=wochenstunden.width * 1.1)
            .next_to(wochenstunden, DOWN, buff=0.2)
        )
        ergebnis = MathTex(
            r"10 \cdot 40 \cdot 45\ = \ 18.000\ \mathrm{Stunden}"
        ).next_to(underline_wochenstunden, DOWN, buff=0.2)

        rechnung = VGroup(
            annahmen_text,
            wochenstunden,
            ein_kleines_rechenbeispiel,
            underline_wochenstunden,
            ergebnis,
        )

        achtzehnk_stunden = Text("18.000 Stunden").move_to((6, 3, 0), UR)
        self.play(Create(rechnung), slide.animate.set_opacity(0).scale(1.2))
        self.wait(0.2)
        self.pause()
        self.play(Uncreate(rechnung), Restore(slide), Create(achtzehnk_stunden))
        self.wait(0.2)
        self.pause()

        tradeoffer = ImageMobject("assets/trade_offer.jpg").scale(1.2).to_edge(DOWN)
        self.add(tradeoffer)
        self.wait(0.2)
        self.pause()
        self.remove(tradeoffer)
        self.wait(0.2)
        self.pause()

        self.wait()
