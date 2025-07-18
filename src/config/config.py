from manim import LEFT, RIGHT, ManimColor
from dataclasses import dataclass

@dataclass
class Colors:
    # Primaries (shouldnt be referenced in config, create function color instead)
    white = ManimColor.from_hex("#ffffff")
    white_muted = ManimColor.from_hex("#d0d0d0")

    red = ManimColor.from_hex("#ff0000")
    green = ManimColor.from_hex("#00ff00")
    blue = ManimColor.from_hex("#0000ff")

    # ZUT Colors
    zut_blue = ManimColor.from_hex("#6CADDF")
    dark_gray = ManimColor.from_hex("#2B2E34")

    # NULL Colors
    null_blue = ManimColor.from_hex("#4860A3")

    # Function Colors
    text = white
    text_muted = white_muted
    header1 = zut_blue

    background = dark_gray

@dataclass 
class Text:
    color: ManimColor = Colors.text
    weight: str = "NORMAL"
    font: str = "Lato"

@dataclass 
class Slide:

    @dataclass 
    class Text(Text):
        pass

    @dataclass
    class Background:
        color: ManimColor = Colors.background

    @dataclass
    class Counter(Text):
        color: ManimColor = Colors.text_muted
        size: float = 0.7

        @dataclass
        class ProgressBar:
            bar_color1: ManimColor = Colors.header1
            bar_color2: ManimColor = Colors.text_muted
            thickness: float = 0.1

@dataclass
class BasicSlide(Slide):

    @dataclass
    class Title(Text):
        size: float = 0.7
        weight: str = "BOLD"
        color: ManimColor = Colors.header1

    @dataclass
    class Separator():
        color = Colors.text_muted

@dataclass
class TitleSlide(Slide):

    @dataclass
    class Title(Text):
        weight: str = "BOLD"
        size: float = 1
        color: ManimColor = Colors.header1
        alignment = RIGHT

    @dataclass
    class Subtitle(Text):
        weight: str = "BOLD"
        size: float = 0.7
        alignment = LEFT

    @dataclass
    class Author(Text):
        weight: str = "BOLD"
        size: float = 0.6
        color: ManimColor = Colors.text_muted
        alignment = LEFT

    @dataclass 
    class Separator:
        color: ManimColor = Colors.text_muted
        start = [-6, 1, 0]
        end = [6, 1, 0]
        dashed_ratio = 0.5
        dash_length = 0.07

@dataclass
class TriangleGroup:

    @dataclass
    class Angles:
        angle_1 = Colors.red
        angle_2 = Colors.green
        angle_3 = Colors.blue
