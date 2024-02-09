from ursina import *
# from modules.particles import CreateParticles
from modules.player import Player
from modules.config_loader import config
from modules.map_creator import Block, CreatePlatform


if __name__ == '__main__':
    app = Ursina()

    window.exit_button.enabled = False
    window.fps_counter.enabled = False
    window.entity_counter.enabled = False
    window.collider_counter.enabled = False

    player = Player()

    # Create Platform
    CreatePlatform(y= -1.5)

    # Run Main App
    app.run()