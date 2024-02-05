from ursina import Entity, color, held_keys
from modules.config_loader import config
from modules.particles import SpawnParticles

class Player(Entity):
    def __init__(self):
        super().__init__()

        self.position = config['Player']['position']
        self.model = 'quad'
        self.color = color.rgb(*config['Player']['color'])
        self.scale = 1

    def update(self):
        speed = config['Player']['speed']
        if held_keys['shift']: speed = config['Player']['run-speed']
        
        if held_keys['space']: SpawnParticles(self.x / 8, self.y / 8)

        if held_keys['a']: self.x -= speed
        if held_keys['d']: self.x += speed

        if held_keys['w']: self.y += speed
        if held_keys['s']: self.y -= speed