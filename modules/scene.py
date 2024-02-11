from modules.map_creator import CreatePlatform
from ursina import AmbientLight, color

class SceneCreator:
    def __init__(self, player):

        # Create Platform
        CreatePlatform(y= -1.3, player=player)

        # Create Ambient
        AmbientLight(color = color.rgb(100, 100, 100, .1))

        # Create Light