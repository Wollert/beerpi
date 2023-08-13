import os

os.environ['DISPLAY'] = ':0.0' # Set $DISPLAY to run GUI on RPi screen even when starting it over ssh
import pygame
from pygame.locals import *

pygame.init() # initializes the pygame engine