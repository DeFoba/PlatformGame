from ursina import *
# from modules.particles import CreateParticles
from modules.player import Player
from modules.config_loader import config

app = Ursina()
player = Player()

app.run()