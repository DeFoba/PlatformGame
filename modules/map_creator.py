from ursina import Entity, color, invoke, random, time
from modules.config_loader import config, is_exit
from threading import Thread

class Block(Entity):
    def __init__(self, x, y, z):
        super().__init__()

        self.scale = 1
        self.model = 'cube'
        self.texture = 'white_cube'

        self.default_y = y

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
        self.animate_color(color.rgb(255, 0, 0), 1)
        time.sleep(1)
            
        self.animate_y(-2, duration=0.5)

        self.texture = 'noise'
        time.sleep(1)
        self.color = (255, 0, 0, 255)

    def make_red(self):
        Thread(target=self._thread_colorize).start()

    def update(self):
        if self.color == (255, 0, 0, 255):
            # self.y -= .1
            self.animate_y(self.default_y, duration=0.5)

            self.texture = 'white_cube'
            self.animate_color(color.rgb(255, 255, 255), 0.5)

            self.start_delay()

def CreatePlatform(x = 0, y = 0, z = 0, width = config['Block']['max-width'], height = config['Block']['max-height']):
    for n in range(x, width):
        for m in range(z, height):
            Block(n, y, m)
