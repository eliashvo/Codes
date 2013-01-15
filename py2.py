import pyglet
from pyglet.gl import *
from time import sleep, time
from threading import *

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_LINE_SMOOTH)
glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)

pyglet.clock.set_fps_limit(30)

class gui (pyglet.window.Window):
	def __init__ (self):
		super(gui, self).__init__(320, 378, fullscreen = False)
		self.alive = 1
		self.megaman = AnimImage("megaman.jpg")
	def run(self):
		while self.alive == 1:
			self.render()
			event = self.dispatch_events()
	def on_draw(self):
		self.render()
	def on_close(self):
		self.alive = 0
	def render(self):
		self.clear()
		self.megaman.sprite.draw()
		self.megaman.update()
		self.flip()
		
class AnimImage():
	def __init__ (self, img):
		self.img = pyglet.image.load(img)
		self.x = 0
		self.sprite = pyglet.sprite.Sprite(self.img.get_region(self.x, 0, 320, 378))
		self.timing = time()
	def update(self):
		if time() - self.timing > 0.5:
			self.x = (self.x+320) % 1280
			self.sprite = pyglet.sprite.Sprite(self.img.get_region(self.x, 0, 320, 378))
			self.timing = time()
x = gui()
x.run() 