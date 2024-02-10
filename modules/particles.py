from ursina import Entity, random, destroy, color, camera, mouse
from modules.config_loader import config

class Particles(Entity):
    def __init__(self, x, y, z, color = color.rgb(*config['Particles']['color'])):
        super().__init__()

        # self.parent = camera.ui
        self.model = "circle"
        self.color = color
        self.scale = config['Particles']['scale']
        self.x = x
        self.y = y
        self.z = z

    def update(self):
        self.x += random.randint(-2, 2) / 50
        self.z += random.randint(-2, 2) / 50
        self.y += random.randint(0, 2) / 100
        self.scale -= .015
        if self.scale < config['Particles']['min-scale']:
            destroy(self)

def SpawnParticles(x, y, z):
    particles = [None] * config['Particles']['count']
    for i in range(len(particles)):
        particles[i] = Particles(x, y, z)