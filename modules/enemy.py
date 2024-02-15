from ursina import Entity, color, PointLight
from ursina.shaders import lit_with_shadows_shader

class Cannon(Entity):
    def __init__(self, x, y, z, player):
        super().__init__()

        self.model = 'assets/cannon.obj'
        self.x, self.y, self.z = x, y, z
        self.player = player
        self.shader = lit_with_shadows_shader

        self.scale = 0.3
        self.color = color.rgb(255, 255, 0)
        self.light = PointLight(x = self.x, y = self.y - 0.5, z = self.z)


    def update(self):
        self.look_at(self.player)
