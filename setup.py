####################################################################################################################################################
# Python Imports
####################################################################################################################################################

import numpy as np
from manim import *
from manim_presentation import (
    Slide,
)  # I don't use this for the presentation itself, i create separate files in the end (see concat_scenes.py)

import src.config.config as c
from src.objects.bulletList import BulletList
from src.objects.numberedList import NumberedList

# All kinds of Custom VMobject-Types
from src.objects.triangleGroup import TriangleGroup
from src.slides.basicSlide import BasicSlide

# All kinds of Slide-Types
from src.slides.titleSlide import TitleSlide

# All kinds of Tool-Types
from src.tools.slideCounter import Counter

####################################################################################################################################################
# Manim Imports
####################################################################################################################################################


####################################################################################################################################################
# Slides-Setup Imports
####################################################################################################################################################


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


####################################################################################################################################################
# Stuff to import at the Start of Files
####################################################################################################################################################
# import os
# import sys
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parent_dir)
#
# from setup import *
