from ursina import Entity, color, invoke, random, time, print_on_screen, Sky
from modules.config_loader import config, is_exit
from threading import Thread

class Block(Entity):
    def __init__(self, x, y, z, player):
        super().__init__()
        self.scale = 1
        self.model = 'cube'
        self.texture = 'assets/block'

        self.player = player

        self.default_y = y
        self.trap_default_y = y - 1

        self.x = x
        self.y = y
        self.z = z

        self._collider = 'cube'
        self.trap = Entity(model='assets/trap.obj', position=(self.x, self.y, self.z), scale=0.5, color=color.rgb(255, 255, 255), collider='box')
        # self.trap._collider.visible = True

        self.delay = int
        self.go_back = False

        self.start_delay()

    def start_delay(self):
        self.delay = random.randint(5, 15)
        invoke(self.make_red, delay=self.delay)

    def _thread_colorize(self):
        self.animate_color(color.rgb(255, 0, 0), 1)
        time.sleep(1)
            
        self.trap.animate_y(self.trap_default_y + 1.5, duration=0.5)

        # self.texture = 'noise'
        time.sleep(1)
        # self.color = (255, 0, 0, 255)
        self.go_back = True

    def make_red(self):
        Thread(target=self._thread_colorize).start()

    def update(self):
        hit_info = self.trap.intersects(ignore=(self, self.trap))

        if hit_info.entity == self.player:
            print_on_screen('HIT')
            self.player.hitting = True

        if self.go_back:
            self.trap.animate_y(self.default_y, duration=0.5)

            # self.texture = 'assets/block'
            self.animate_color(color.rgb(255, 255, 255), 0.5)
            self.go_back = False

            self.start_delay()

def CreatePlatform(x = 0, y = 0, z = 0, width = config['Block']['max-width'], height = config['Block']['max-height'], player=None):
    # water = Entity(model='quad', color=color.rgb(0, 0, 255), texture='noise', scale=20, rotation_x=90, position=(width / 2 - .5, y, height / 2))
    sky = Sky(color=color.black)
    for n in range(x, width):
        for m in range(z, height):
            Block(n, y, m, player)
