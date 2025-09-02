####################################################################################################################################################
#Python Imports
####################################################################################################################################################

import numpy as np

####################################################################################################################################################
# Manim Imports
####################################################################################################################################################

from manim import *
from manim_presentation import Slide # I don't use this for the presentation itself, i create separate files in the end (see concat_scenes.py)

####################################################################################################################################################
# Slides-Setup Imports
####################################################################################################################################################

import src.config.config as c

# All kinds of Slide-Types
from src.slides.titleSlide import TitleSlide
from src.slides.basicSlide import BasicSlide

# All kinds of Tool-Types
from src.tools.slideCounter import Counter

# All kinds of Custom VMobject-Types
from src.objects.triangleGroup import TriangleGroup
from src.objects.bulletList import BulletList
from src.objects.numberedList import NumberedList

####################################################################################################################################################
# Some basic settings for scene. Can be changed. Values should be stored in config
####################################################################################################################################################

config.background_color = c.Slide.Background.color
Text.set_default(font=c.Slide.Text.font)
Text.set_default(font_size=c.Slide.Text.font_size)
# MarkupText.set_default(font=c.Slide.Text.font)
# MarkupText.set_default(font_size=c.Slide.Text.font_size)
# BulletedList.set_default(font=c.Slide.Text.font)
# BulletedList.set_default(font_size=c.Slide.Text.font_size)

####################################################################################################################################################
# Some values/states that should be tracked across Classes
####################################################################################################################################################

count = Counter(1, 10)

