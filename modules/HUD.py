from ursina import Entity, color, camera, Text

class Stamina(Entity):
    def __init__(self, x, player):
        super().__init__()
        self.player = player

        self.model = 'quad'
        self.color = color.rgb(255, 255, 0, 255)
        self._billboard = True

        self.scale_max = x
        self.scale_x = x

        self.scale = (self.scale_x, .05)

    def update(self):
        self.position = (self.player.x, self.player.y, self.player.z)

class NickOnHead(Text):
    def __init__(self, nickname, player):
        super().__init__()
        self.player = player

        self.text = nickname
        self.color = color.rgb(255, 0, 255)

        self.origin = self.player.origin
        self.origin_y = self.player.origin_y - 1

    def update(self):
        self.position = (self.player.x, self.player.y, self.player.z)


class Exit:
    def __init__(self):
        self.background = Entity(model='quad', color=color.rgb(130, 130, 130), parent = camera.ui, scale = 5)
        self.inforamtion = Text('Closing Game...', scale = 2, parent = camera.ui)