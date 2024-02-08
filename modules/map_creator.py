from ursina import Entity
from modules.player import Player

class Block(Entity):
    def __init__(self, player: Player, x, y):
        super().__init__()

        self.player = player

        self.scale = 1
        self.model = 'quad'
        self.texture = 'white_cube'

        self.x = x
        self.y = y

        self._collider = 'box'

    def update(self):
        if self.player.x >= self.x - self.scale_x / 2 and self.player.x <= self.x + self.scale_x / 2:
            if self.player.y <= self.y + self.scale_y * 1.5 and self.player.y >= self.y + self.scale_y / 2:
                self.player.y += self.player.speed