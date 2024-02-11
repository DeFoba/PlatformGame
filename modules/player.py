from ursina import Entity, color, held_keys, SpriteSheetAnimation, camera, invoke, BoxCollider
from modules.config_loader import config, is_exit
from modules.particles import SpawnParticles, HitParticles
from modules.HUD import Stamina, Exit

ANIMATION_SET = {
    'walk': ('assets/Blue_Slime/walk', (8, 1)),
    'idle': ('assets/Blue_Slime/idle', (8, 1)),
    'run': ('assets/Blue_Slime/run', (7, 1)),
    'jump': ('assets/Blue_Slime/Jump', (13, 1)),
}

class Player(SpriteSheetAnimation):
    '''Main Player class, for init Player entity'''
    def __init__(self):
        # Init Sprite Sheet Animation
        super().__init__('assets/Blue_Slime/idle', {
            'walk': ((0, 0), (7, 0)),
            'idle': ((0, 0), (7, 0)),
            'run': ((0, 0), (6, 0)),
            'jump': ((0, 0), (12, 0)),
            }, fps=12)
        
        self.collider = BoxCollider(self, center=(0, -.3, 0), size=(0.4, 0.3, 0.3))
        # self.collider.visible = True

        # Configure Player
        self.position = config['Player']['position']
        self.model = 'quad'
        self.color = color.rgb(*config['Player']['color'])
        self.scale = 1.5
        self.tileset_size=(8, 1)
        self.autoplay = True
        self.double_sided = True
        self._collider = 'box'

        # Hitting
        self.hitting = False
        self.lives = 3

        # Load HUD
        self.stamina = Stamina(.5)

        # Check variables
        self.is_shift = False

        # Run Idle Animation
        self.play_animation('idle')

    def change_animation(self, anim):
        '''Change Player Animation'''
        self.texture, self.tileset_size = ANIMATION_SET[anim]

    def update(self):
        '''Player movement and Camera forward'''
        speed = config['Player']['speed']
        if held_keys['shift']:
            if self.stamina.scale_x > .05:
                self.stamina.scale_x -= .01
                speed = config['Player']['run-speed']

        if self.stamina.scale_x < self.stamina.scale_max and not held_keys['shift']:
            self.stamina.scale_x += .002

        if held_keys['a']:
            self.rotation_y = 180
            if self.x > -.2:
                self.x -= speed
            else: self.x = -.2

        if held_keys['d']:
            self.rotation_y = 0
            if self.x < config['Block']['max-width'] - 0.7:
                self.x += speed
            else: self.x = config['Block']['max-width'] - 0.7

        if held_keys['w']:
            if self.z < config['Block']['max-height'] - 0.6:
                self.z += speed
            else:
                self.z = config['Block']['max-height'] - 0.6

        if held_keys['s']:
            if self.z > -.5:
                self.z -= speed
            else:
                self.z = -.5

        if self.hitting:
            self.collision = False
            self.hitting = False
            # camera.shake(1, magnitude=10)
            HitParticles(self.x, self.y - self.scale_x / 2, self.z)
            invoke(self.turn_on_collision, delay=3)
    

        # Camera poition forward
        camera.x += (self.x - camera.x) / 8
        camera.z += (self.z - camera.z) / 8 - 1.5
        camera.y += (self.y - camera.y) / 6 + 0.5

        # Camera rotation
        camera.look_at(self)

    def turn_on_collision(self):
        self.collision = 'box'

    def close_app(self):
        global is_exit
        is_exit = True
        quit()
            

    def input(self, key):
        '''Check Player inputs for change animation'''
        if key == 'shift':
            SpawnParticles(self.x, self.y - self.scale_x / 2, self.z)

        if key == 'space':
            SpawnParticles(self.x, self.y - self.scale_x / 2, self.z)
            # self.change_animation('jump')
            # self.play_animation('jump')

        if key == 'shift': self.is_shift = True
        if key == 'shift up': self.is_shift = False

        if key == 'a' or key == 'd' or key == 'w' or key == 's':
            if self.is_shift:
                self.change_animation('run')
                self.play_animation('run')
            else:
                self.change_animation('walk')
                self.play_animation('walk')
        
        if key == 'a up' or key == 'd up' or key == 'w up' or key == 's up':
            if not held_keys['a'] and not held_keys['d'] and not held_keys['w'] and not held_keys['s']:
                self.change_animation('idle')
                self.play_animation('idle')

        if key == 'escape':
            Exit()
            invoke(self.close_app, delay=2)
            
