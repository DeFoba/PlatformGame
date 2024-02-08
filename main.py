from ursina import *
# from modules.particles import CreateParticles
from modules.player import Player
from modules.config_loader import config
from modules.map_creator import Block

app = Ursina()
player = Player()

Block(player, 0, -2)
Block(player, 1, -2)
Block(player, 2, -2)
Block(player, 3, -2)

app.run()