from ursina import Entity, color, invoke, random, time
from modules.config_loader import config, is_exit
from threading import Thread

class Block(Entity):
    def __init__(self, x, y, z):
        super().__init__()

        self.scale = 1
        self.model = 'cube'
        self.texture = 'white_cube'

        self.x = x
        self.y = y
        self.z = z

        self._collider = 'cube'

        self.delay = int

        self.start_delay()

    def start_delay(self):
        self.delay = random.randint(5, 15)
        invoke(self.make_red, delay=self.delay)

    def _thread_colorize(self):
        for n in [x for x in range(1, self.delay + 1)]:
            if is_exit: break
            self.color = color.rgb(255, 255 // n, 255 // n, 255)
            time.sleep(0.2)
        self.y -= .1
        self.texture = 'noise'
        time.sleep(1)
        self.color = (255, 0, 0, 255)

    def make_red(self):
        Thread(target=self._thread_colorize).start()

    def update(self):
        if self.color == (255, 0, 0, 255):
            self.y += .1
            self.texture = 'white_cube'
            self.color = (255, 255, 255, 255)
            self.start_delay()

def CreatePlatform(x = 0, y = 0, z = 0, width = config['Block']['max-width'], height = config['Block']['max-height']):
    for n in range(x, width):
        for m in range(z, height):
            Block(n, y, m)
