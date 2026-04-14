from dataclasses import dataclass

from manim import LEFT, RIGHT, ManimColor


@dataclass
class Colors:
    """
    Color palette based on Tailwind CSS v4.
    Each hue has 11 steps: 50 (lightest) → 950 (darkest).

    COLOR FAMILIES:
    ─── Reds/Pinks (warm): red, rose, pink, fuchsia
    ─── Purples:          purple, violet, indigo
    ─── Blues:            blue, sky, cyan
    ─── Greens:           teal, emerald, green, lime
    ─── Yellows/Oranges:  yellow, amber, orange
    ─── Neutrals (cool):  slate, gray, zinc
    ─── Neutrals (warm):  stone, taupe, neutral
    ─── Subtle tints:     mist, mauve, olive

    STEP GUIDE:
    50        → near-white background tint
    100-200   → very light, good for backgrounds/fills
    300-400   → light, good for borders and muted elements
    500       → mid/pure tone — the 'identity' color of the family
    600-700   → dark enough for text on white, good for primary buttons
    800-900   → very dark, strong text/icon use
    950       → near-black tint
    """

    # ── Reds & Pinks (warm tones) ─────────────────────────────────────
    red_50 = ManimColor.from_hex("#fef2f2")
    red_100 = ManimColor.from_hex("#ffe2e2")
    red_200 = ManimColor.from_hex("#ffc9c9")
    red_300 = ManimColor.from_hex("#ffa2a2")
    red_400 = ManimColor.from_hex("#ff6467")
    red_500 = ManimColor.from_hex("#fb2c36")
    red_600 = ManimColor.from_hex("#e7000b")
    red_700 = ManimColor.from_hex("#c10007")
    red_800 = ManimColor.from_hex("#9f0712")
    red_900 = ManimColor.from_hex("#82181a")
    red_950 = ManimColor.from_hex("#460809")

    rose_50 = ManimColor.from_hex("#fff1f2")
    rose_100 = ManimColor.from_hex("#ffe4e6")
    rose_200 = ManimColor.from_hex("#ffccd3")
    rose_300 = ManimColor.from_hex("#ffa1ad")
    rose_400 = ManimColor.from_hex("#ff637e")
    rose_500 = ManimColor.from_hex("#ff2056")
    rose_600 = ManimColor.from_hex("#ec003f")
    rose_700 = ManimColor.from_hex("#c70036")
    rose_800 = ManimColor.from_hex("#a50036")
    rose_900 = ManimColor.from_hex("#8b0836")
    rose_950 = ManimColor.from_hex("#4d0218")

    pink_50 = ManimColor.from_hex("#fdf2f8")
    pink_100 = ManimColor.from_hex("#fce7f3")
    pink_200 = ManimColor.from_hex("#fccee8")
    pink_300 = ManimColor.from_hex("#fda5d5")
    pink_400 = ManimColor.from_hex("#fb64b6")
    pink_500 = ManimColor.from_hex("#f6339a")
    pink_600 = ManimColor.from_hex("#e60076")
    pink_700 = ManimColor.from_hex("#c6005c")
    pink_800 = ManimColor.from_hex("#a3004c")
    pink_900 = ManimColor.from_hex("#861043")
    pink_950 = ManimColor.from_hex("#510424")

    fuchsia_50 = ManimColor.from_hex("#fdf4ff")
    fuchsia_100 = ManimColor.from_hex("#fae8ff")
    fuchsia_200 = ManimColor.from_hex("#f6cfff")
    fuchsia_300 = ManimColor.from_hex("#f4a8ff")
    fuchsia_400 = ManimColor.from_hex("#ed6aff")
    fuchsia_500 = ManimColor.from_hex("#e12afb")
    fuchsia_600 = ManimColor.from_hex("#c800de")
    fuchsia_700 = ManimColor.from_hex("#a800b7")
    fuchsia_800 = ManimColor.from_hex("#8a0194")
    fuchsia_900 = ManimColor.from_hex("#721378")
    fuchsia_950 = ManimColor.from_hex("#4b004f")

    # ── Purples ─────────────────────────────────────
    violet_50 = ManimColor.from_hex("#f5f3ff")
    violet_100 = ManimColor.from_hex("#ede9fe")
    violet_200 = ManimColor.from_hex("#ddd6ff")
    violet_300 = ManimColor.from_hex("#c4b4ff")
    violet_400 = ManimColor.from_hex("#a684ff")
    violet_500 = ManimColor.from_hex("#8e51ff")
    violet_600 = ManimColor.from_hex("#7f22fe")
    violet_700 = ManimColor.from_hex("#7008e7")
    violet_800 = ManimColor.from_hex("#5d0ec0")
    violet_900 = ManimColor.from_hex("#4d179a")
    violet_950 = ManimColor.from_hex("#2f0d68")

    purple_50 = ManimColor.from_hex("#faf5ff")
    purple_100 = ManimColor.from_hex("#f3e8ff")
    purple_200 = ManimColor.from_hex("#e9d4ff")
    purple_300 = ManimColor.from_hex("#dab2ff")
    purple_400 = ManimColor.from_hex("#c27aff")
    purple_500 = ManimColor.from_hex("#ad46ff")
    purple_600 = ManimColor.from_hex("#9810fa")
    purple_700 = ManimColor.from_hex("#8200db")
    purple_800 = ManimColor.from_hex("#6e11b0")
    purple_900 = ManimColor.from_hex("#59168b")
    purple_950 = ManimColor.from_hex("#3c0366")

    indigo_50 = ManimColor.from_hex("#eef2ff")
    indigo_100 = ManimColor.from_hex("#e0e7ff")
    indigo_200 = ManimColor.from_hex("#c6d2ff")
    indigo_300 = ManimColor.from_hex("#a3b3ff")
    indigo_400 = ManimColor.from_hex("#7c86ff")
    indigo_500 = ManimColor.from_hex("#615fff")
    indigo_600 = ManimColor.from_hex("#4f39f6")
    indigo_700 = ManimColor.from_hex("#432dd7")
    indigo_800 = ManimColor.from_hex("#372aac")
    indigo_900 = ManimColor.from_hex("#312c85")
    indigo_950 = ManimColor.from_hex("#1e1a4d")

    # ── Blues ─────────────────────────────────────
    blue_50 = ManimColor.from_hex("#eff6ff")
    blue_100 = ManimColor.from_hex("#dbeafe")
    blue_200 = ManimColor.from_hex("#bedbff")
    blue_300 = ManimColor.from_hex("#8ec5ff")
    blue_400 = ManimColor.from_hex("#51a2ff")
    blue_500 = ManimColor.from_hex("#2b7fff")
    blue_600 = ManimColor.from_hex("#155dfc")
    blue_700 = ManimColor.from_hex("#1447e6")
    blue_800 = ManimColor.from_hex("#193cb8")
    blue_900 = ManimColor.from_hex("#1c398e")
    blue_950 = ManimColor.from_hex("#162456")

    sky_50 = ManimColor.from_hex("#f0f9ff")
    sky_100 = ManimColor.from_hex("#dff2fe")
    sky_200 = ManimColor.from_hex("#b8e6fe")
    sky_300 = ManimColor.from_hex("#74d4ff")
    sky_400 = ManimColor.from_hex("#00bcff")
    sky_500 = ManimColor.from_hex("#00a6f4")
    sky_600 = ManimColor.from_hex("#0084d1")
    sky_700 = ManimColor.from_hex("#0069a8")
    sky_800 = ManimColor.from_hex("#00598a")
    sky_900 = ManimColor.from_hex("#024a70")
    sky_950 = ManimColor.from_hex("#052f4a")

    cyan_50 = ManimColor.from_hex("#ecfeff")
    cyan_100 = ManimColor.from_hex("#cefafe")
    cyan_200 = ManimColor.from_hex("#a2f4fd")
    cyan_300 = ManimColor.from_hex("#53eafd")
    cyan_400 = ManimColor.from_hex("#00d3f2")
    cyan_500 = ManimColor.from_hex("#00b8db")
    cyan_600 = ManimColor.from_hex("#0092b8")
    cyan_700 = ManimColor.from_hex("#007595")
    cyan_800 = ManimColor.from_hex("#005f78")
    cyan_900 = ManimColor.from_hex("#104e64")
    cyan_950 = ManimColor.from_hex("#053345")

    # ── Greens & Teals ─────────────────────────────────────
    teal_50 = ManimColor.from_hex("#f0fdfa")
    teal_100 = ManimColor.from_hex("#cbfbf1")
    teal_200 = ManimColor.from_hex("#96f7e4")
    teal_300 = ManimColor.from_hex("#46ecd5")
    teal_400 = ManimColor.from_hex("#00d5be")
    teal_500 = ManimColor.from_hex("#00bba7")
    teal_600 = ManimColor.from_hex("#009689")
    teal_700 = ManimColor.from_hex("#00786f")
    teal_800 = ManimColor.from_hex("#005f5a")
    teal_900 = ManimColor.from_hex("#0b4f4a")
    teal_950 = ManimColor.from_hex("#022f2e")

    emerald_50 = ManimColor.from_hex("#ecfdf5")
    emerald_100 = ManimColor.from_hex("#d0fae5")
    emerald_200 = ManimColor.from_hex("#a4f4cf")
    emerald_300 = ManimColor.from_hex("#5ee9b5")
    emerald_400 = ManimColor.from_hex("#00d492")
    emerald_500 = ManimColor.from_hex("#00bc7d")
    emerald_600 = ManimColor.from_hex("#009966")
    emerald_700 = ManimColor.from_hex("#007a55")
    emerald_800 = ManimColor.from_hex("#006045")
    emerald_900 = ManimColor.from_hex("#004f3b")
    emerald_950 = ManimColor.from_hex("#002c22")

    green_50 = ManimColor.from_hex("#f0fdf4")
    green_100 = ManimColor.from_hex("#dcfce7")
    green_200 = ManimColor.from_hex("#b9f8cf")
    green_300 = ManimColor.from_hex("#7bf1a8")
    green_400 = ManimColor.from_hex("#05df72")
    green_500 = ManimColor.from_hex("#00c950")
    green_600 = ManimColor.from_hex("#00a63e")
    green_700 = ManimColor.from_hex("#008236")
    green_800 = ManimColor.from_hex("#016630")
    green_900 = ManimColor.from_hex("#0d542b")
    green_950 = ManimColor.from_hex("#032e15")

    lime_50 = ManimColor.from_hex("#f7fee7")
    lime_100 = ManimColor.from_hex("#ecfcca")
    lime_200 = ManimColor.from_hex("#d8f999")
    lime_300 = ManimColor.from_hex("#bbf451")
    lime_400 = ManimColor.from_hex("#9ae600")
    lime_500 = ManimColor.from_hex("#7ccf00")
    lime_600 = ManimColor.from_hex("#5ea500")
    lime_700 = ManimColor.from_hex("#497d00")
    lime_800 = ManimColor.from_hex("#3c6300")
    lime_900 = ManimColor.from_hex("#35530e")
    lime_950 = ManimColor.from_hex("#192e03")

    # ── Yellows & Oranges ─────────────────────────────────────
    yellow_50 = ManimColor.from_hex("#fefce8")
    yellow_100 = ManimColor.from_hex("#fef9c2")
    yellow_200 = ManimColor.from_hex("#fff085")
    yellow_300 = ManimColor.from_hex("#ffdf20")
    yellow_400 = ManimColor.from_hex("#fdc700")
    yellow_500 = ManimColor.from_hex("#f0b100")
    yellow_600 = ManimColor.from_hex("#d08700")
    yellow_700 = ManimColor.from_hex("#a65f00")
    yellow_800 = ManimColor.from_hex("#894b00")
    yellow_900 = ManimColor.from_hex("#733e0a")
    yellow_950 = ManimColor.from_hex("#432004")

    amber_50 = ManimColor.from_hex("#fffbeb")
    amber_100 = ManimColor.from_hex("#fef3c6")
    amber_200 = ManimColor.from_hex("#fee685")
    amber_300 = ManimColor.from_hex("#ffd230")
    amber_400 = ManimColor.from_hex("#ffb900")
    amber_500 = ManimColor.from_hex("#fe9a00")
    amber_600 = ManimColor.from_hex("#e17100")
    amber_700 = ManimColor.from_hex("#bb4d00")
    amber_800 = ManimColor.from_hex("#973c00")
    amber_900 = ManimColor.from_hex("#7b3306")
    amber_950 = ManimColor.from_hex("#461901")

    orange_50 = ManimColor.from_hex("#fff7ed")
    orange_100 = ManimColor.from_hex("#ffedd4")
    orange_200 = ManimColor.from_hex("#ffd6a7")
    orange_300 = ManimColor.from_hex("#ffb86a")
    orange_400 = ManimColor.from_hex("#ff8904")
    orange_500 = ManimColor.from_hex("#ff6900")
    orange_600 = ManimColor.from_hex("#f54900")
    orange_700 = ManimColor.from_hex("#ca3500")
    orange_800 = ManimColor.from_hex("#9f2d00")
    orange_900 = ManimColor.from_hex("#7e2a0c")
    orange_950 = ManimColor.from_hex("#441306")

    # ── Neutrals — Cool-tinted (blue-gray) ─────────────────────────────────────
    slate_50 = ManimColor.from_hex("#f8fafc")
    slate_100 = ManimColor.from_hex("#f1f5f9")
    slate_200 = ManimColor.from_hex("#e2e8f0")
    slate_300 = ManimColor.from_hex("#cad5e2")
    slate_400 = ManimColor.from_hex("#90a1b9")
    slate_500 = ManimColor.from_hex("#62748e")
    slate_600 = ManimColor.from_hex("#45556c")
    slate_700 = ManimColor.from_hex("#314158")
    slate_800 = ManimColor.from_hex("#1d293d")
    slate_900 = ManimColor.from_hex("#0f172b")
    slate_950 = ManimColor.from_hex("#020618")

    gray_50 = ManimColor.from_hex("#f9fafb")
    gray_100 = ManimColor.from_hex("#f3f4f6")
    gray_200 = ManimColor.from_hex("#e5e7eb")
    gray_300 = ManimColor.from_hex("#d1d5dc")
    gray_400 = ManimColor.from_hex("#99a1af")
    gray_500 = ManimColor.from_hex("#6a7282")
    gray_600 = ManimColor.from_hex("#4a5565")
    gray_700 = ManimColor.from_hex("#364153")
    gray_800 = ManimColor.from_hex("#1e2939")
    gray_900 = ManimColor.from_hex("#101828")
    gray_950 = ManimColor.from_hex("#030712")

    zinc_50 = ManimColor.from_hex("#fafafa")
    zinc_100 = ManimColor.from_hex("#f4f4f5")
    zinc_200 = ManimColor.from_hex("#e4e4e7")
    zinc_300 = ManimColor.from_hex("#d4d4d8")
    zinc_400 = ManimColor.from_hex("#9f9fa9")
    zinc_500 = ManimColor.from_hex("#71717b")
    zinc_600 = ManimColor.from_hex("#52525c")
    zinc_700 = ManimColor.from_hex("#3f3f46")
    zinc_800 = ManimColor.from_hex("#27272a")
    zinc_900 = ManimColor.from_hex("#18181b")
    zinc_950 = ManimColor.from_hex("#09090b")

    # ── Neutrals — Warm-tinted (brown-gray) ─────────────────────────────────────
    stone_50 = ManimColor.from_hex("#fafaf9")
    stone_100 = ManimColor.from_hex("#f5f5f4")
    stone_200 = ManimColor.from_hex("#e7e5e4")
    stone_300 = ManimColor.from_hex("#d6d3d1")
    stone_400 = ManimColor.from_hex("#a6a09b")
    stone_500 = ManimColor.from_hex("#79716b")
    stone_600 = ManimColor.from_hex("#57534d")
    stone_700 = ManimColor.from_hex("#44403b")
    stone_800 = ManimColor.from_hex("#292524")
    stone_900 = ManimColor.from_hex("#1c1917")
    stone_950 = ManimColor.from_hex("#0c0a09")

    taupe_50 = ManimColor.from_hex("#fbfaf9")
    taupe_100 = ManimColor.from_hex("#f3f1f1")
    taupe_200 = ManimColor.from_hex("#e8e4e3")
    taupe_300 = ManimColor.from_hex("#d8d2d0")
    taupe_400 = ManimColor.from_hex("#aba09c")
    taupe_500 = ManimColor.from_hex("#7c6d67")
    taupe_600 = ManimColor.from_hex("#5b4f4b")
    taupe_700 = ManimColor.from_hex("#473c39")
    taupe_800 = ManimColor.from_hex("#2b2422")
    taupe_900 = ManimColor.from_hex("#1d1816")
    taupe_950 = ManimColor.from_hex("#0c0a09")

    neutral_50 = ManimColor.from_hex("#fafafa")
    neutral_100 = ManimColor.from_hex("#f5f5f5")
    neutral_200 = ManimColor.from_hex("#e5e5e5")
    neutral_300 = ManimColor.from_hex("#d4d4d4")
    neutral_400 = ManimColor.from_hex("#a1a1a1")
    neutral_500 = ManimColor.from_hex("#737373")
    neutral_600 = ManimColor.from_hex("#525252")
    neutral_700 = ManimColor.from_hex("#404040")
    neutral_800 = ManimColor.from_hex("#262626")
    neutral_900 = ManimColor.from_hex("#171717")
    neutral_950 = ManimColor.from_hex("#0a0a0a")

    # ── Subtle Tints ─────────────────────────────────────
    mist_50 = ManimColor.from_hex("#f9fbfb")
    mist_100 = ManimColor.from_hex("#f1f3f3")
    mist_200 = ManimColor.from_hex("#e3e7e8")
    mist_300 = ManimColor.from_hex("#d0d6d8")
    mist_400 = ManimColor.from_hex("#9ca8ab")
    mist_500 = ManimColor.from_hex("#67787c")
    mist_600 = ManimColor.from_hex("#4b585b")
    mist_700 = ManimColor.from_hex("#394447")
    mist_800 = ManimColor.from_hex("#22292b")
    mist_900 = ManimColor.from_hex("#161b1d")
    mist_950 = ManimColor.from_hex("#090b0c")

    mauve_50 = ManimColor.from_hex("#fafafa")
    mauve_100 = ManimColor.from_hex("#f3f1f3")
    mauve_200 = ManimColor.from_hex("#e7e4e7")
    mauve_300 = ManimColor.from_hex("#d7d0d7")
    mauve_400 = ManimColor.from_hex("#a89ea9")
    mauve_500 = ManimColor.from_hex("#79697b")
    mauve_600 = ManimColor.from_hex("#594c5b")
    mauve_700 = ManimColor.from_hex("#463947")
    mauve_800 = ManimColor.from_hex("#2a212c")
    mauve_900 = ManimColor.from_hex("#1d161e")
    mauve_950 = ManimColor.from_hex("#0c090c")

    olive_50 = ManimColor.from_hex("#fbfbf9")
    olive_100 = ManimColor.from_hex("#f4f4f0")
    olive_200 = ManimColor.from_hex("#e8e8e3")
    olive_300 = ManimColor.from_hex("#d8d8d0")
    olive_400 = ManimColor.from_hex("#abab9c")
    olive_500 = ManimColor.from_hex("#7c7c67")
    olive_600 = ManimColor.from_hex("#5b5b4b")
    olive_700 = ManimColor.from_hex("#474739")
    olive_800 = ManimColor.from_hex("#2b2b22")
    olive_900 = ManimColor.from_hex("#1d1d16")
    olive_950 = ManimColor.from_hex("#0c0c09")

    # ── Special ─────────────────────────────────────────────────
    black = ManimColor.from_hex("#000000")
    white = ManimColor.from_hex("#ffffff")

    # ── Project Colors ───────────────────────────────────────────
    # ZUT Colors
    zut_blue = ManimColor.from_hex("#6CADDF")
    dark_gray = ManimColor.from_hex("#2B2E34")

    # NULL Colors
    null_blue = ManimColor.from_hex("#4860A3")

    # ── Semantic / Function Colors ───────────────────────────────
    # Override these to change the visual theme
    text = white
    text_muted = gray_400

    accent1 = zut_blue
    header1 = accent1

    background = dark_gray


@dataclass
class Text:
    color: ManimColor = Colors.text
    weight: str = "NORMAL"
    font: str = "Noto Sans"
    font_size: float = 30


@dataclass
class Bulletpoints(Text):
    vertical_spacing: float = 0.4


@dataclass
class NumberedList(Text):
    vertical_spacing: float = 0.4


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
        color: ManimColor = Colors.accent1

    @dataclass
    class Separator:
        color = Colors.text_muted


@dataclass
class TitleSlide(Slide):

    @dataclass
    class Title(Text):
        weight: str = "BOLD"
        scaling: float = 1.3
        color: ManimColor = Colors.accent1
        alignment = RIGHT

    @dataclass
    class Subtitle(Text):
        weight: str = "BOLD"
        scaling: float = 1
        alignment = LEFT

    @dataclass
    class Author(Text):
        weight: str = "BOLD"
        scaling: float = 0.85
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
        angle_1 = Colors.red_200
        angle_2 = Colors.green_200
        angle_3 = Colors.blue_200
