from ursina import Entity, color, camera, Text

class Stamina(Entity):
    def __init__(self, x):
        super().__init__()

        self.model = 'quad'
        self.color = color.rgb(255, 255, 0, 255)

        self.scale_max = x
        self.scale_x = x

        self.scale = (self.scale_x, .05)
        self.position = (-.63, .47)

        self.parent = camera.ui

    def update(self):
        pass

class Exit:
    def __init__(self):
        self.background = Entity(model='quad', color=color.rgb(130, 130, 130), parent = camera.ui, scale = 5)
        self.inforamtion = Text('Closing Game...', scale = 2, parent = camera.ui)