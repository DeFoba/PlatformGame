from ursina import *
from modules.player import Player
from modules.scene import SceneCreator


if __name__ == '__main__':
    app = Ursina(icon='assets/slime.ico', title='Maori Slime Game')

    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    try:
        window.entity_counter.enabled = False
        window.collider_counter.enabled = False
    except: pass

    window.fullscreen = True
    window.borderless = True

    player = Player()
    _scene = SceneCreator(player)

    # Run Main App
    app.run()