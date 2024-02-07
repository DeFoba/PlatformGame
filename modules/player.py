from ursina import Entity, color, held_keys, SpriteSheetAnimation
from modules.config_loader import config
from modules.particles import SpawnParticles

ANIMATION_SET = {
    'walk': ('assets/Blue_Slime/walk', (8, 1)),
    'idle': ('assets/Blue_Slime/idle', (8, 1)),
    'run': ('assets/Blue_Slime/run', (7, 1)),
    'jump': ('assets/Blue_Slime/Jump', (13, 1)),
}

class Player(SpriteSheetAnimation):
    def __init__(self):
        super().__init__('assets/Blue_Slime/idle', {
            'walk': ((0, 0), (7, 0)),
            'idle': ((0, 0), (7, 0)),
            'run': ((0, 0), (6, 0)),
            'jump': ((0, 0), (12, 0)),
            })

        self.position = config['Player']['position']
        self.model = 'quad'
        self.color = color.rgb(*config['Player']['color'])
        self.scale = 1
        self.tileset_size=(8, 1)
        self.autoplay = True
        self.double_sided = True

        self.is_shift = False

        self.play_animation('idle')

    def change_animation(self, anim):
        self.texture, self.tileset_size = ANIMATION_SET[anim]

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
            self.change_animation('jump')
            self.play_animation('jump')

        if key == 'shift': self.is_shift = True
        if key == 'shift up': self.is_shift = False

        if key == 'a' or key == 'd':
            if self.is_shift:
                self.change_animation('run')
                self.play_animation('run')
            else:
                self.change_animation('walk')
                self.play_animation('walk')
        
        if key == 'a up' or key == 'd up':
            if not held_keys['a'] and not held_keys['d']:
                self.change_animation('idle')
                self.play_animation('idle')

