from ursina import *
from modules.particles import CreatePartiles
from modules.config_loader import config

app = Ursina()

mouse_btn = Button(text='', color=color.rgb(255, 255, 255, 0), scale=2)
mouse_btn.on_click = CreatePartiles


app.run()