from ursina import Entity, color, held_keys, SpriteSheetAnimation
from modules.config_loader import config
from modules.particles import SpawnParticles

class Player(SpriteSheetAnimation):
    def __init__(self):
        super().__init__('assets/Blue_Slime/walk', {'idle': ((0, 0), (0, 0)), 'walk': ((0, 0), (7, 0))})

        self.position = config['Player']['position']
        self.model = 'quad'
        self.color = color.rgb(*config['Player']['color'])
        self.scale = 1
        self.tileset_size=(8, 1)
        self.autoplay = True
        self.double_sided = True

    def update(self):
        speed = config['Player']['speed']
        if held_keys['shift']: speed = config['Player']['run-speed']

        if held_keys['a']:
            self.rotation_y = 180
            self.x -= speed

        if held_keys['d']:
            self.rotation_y = 0
            self.x += speed

        if held_keys['w']: self.y += speed
        if held_keys['s']: self.y -= speed


    def input(self, key):
        if key == 'space':
            SpawnParticles(self.x, self.y)

        if key == 'a' or key == 'd': self.play_animation('walk')
        
        if key == 'a up' or key == 'd up':
            if not held_keys['a'] and not held_keys['d']: self.play_animation('idle')

