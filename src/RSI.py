import tkinter as tk
import threading

def main():
	"""
	TODO: put main stuff here
	"""
	w = appWindow()
	#m = motionCapture(w.tk)
	w.tk.mainloop()


class appWindow(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.createWidgets()
		self.timer = threading.Timer(0.5, self.animator)
		self.timer.start()

	def createWidgets(self):
		# frame container
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# frames
		self.frames = {}
		for f in (baseFrame, menuWindow, gameWindow):
			frame = f(container, self)
			frame.grid(row=0, column=0, sticky=tk.NW+tk.SE)
			self.frames[f] = frame
		self.showFrame(baseFrame)

	def showFrame(self, frameClass):
		self.frames[frameClass].tkraise()
		self.frames[frameClass].focus_set()

	def animator(self):
		self.frames[gameWindow].animateTargets()
		self.timer = threading.Timer(0.5, self.animator)
		self.timer.start()


class baseFrame(tk.Frame):
	"""
	Master: container frame (tk.Frame)
	Controller: appWindow (tk.Tk)
	"""

	def __init__(self, master, controller):
		tk.Frame.__init__(self, master)
		self.controller = controller
		self.createWidgets()
		self.grid()
		

	def createWidgets(self):
		"""Create the widgets for the frame."""
		controller = self.controller
		label = tk.Label(self, text="switch pages")
		label.pack()

		button1 = tk.Button(self, text="go to menu window",
			command=lambda: controller.showFrame(menuWindow))
		button2 = tk.Button(self, text="go to gameWindow",
			command=lambda: controller.showFrame(gameWindow))

		button1.pack()
		button2.pack()



class menuWindow(tk.Frame):

	def __init__(self, master, controller):
		tk.Frame.__init__(self, master)
		self.controller = controller
		self.createWidgets()
		self.configure(background="blue")
		self.grid()

	def createWidgets(self):
		"""Create the widgets for the frame."""
		controller = self.controller
		label = tk.Label(self, text="menu window", background="blue")
		label.pack()

		button1 = tk.Button(self, text="go to menu window",
			command=lambda: controller.showFrame(menuWindow))
		button2 = tk.Button(self, text="go to gameWindow",
			command=lambda: controller.showFrame(gameWindow))

		button1.pack()
		button2.pack()
	"""
	TODO: 	create game main menu, including:
			-just a single game mode for row
			-high scores


	TODO:	make it pretty
	"""


class gameWindow(tk.Frame):
	"""
	TODO: 	implement game. Mechanics involve moving the cursor to a
			sequence of circles that appear on the screen. Points will
			be assigned based on cursor speed, and proximity to circle
			centre. Will be time based.

	TODO:	implement keybinds to exit game mode
	
	TODO:	implement sequential drawing of shrinking circles on canvas
	"""
	
	def __init__(self, master, controller):

		tk.Frame.__init__(self, master, height=600, width=400)
		self.controller = controller
		#self.createWidgets()
		self.createTargets()
		self.grid()
		controller.attributes("-fullscreen", False)



	def createWidgets(self):
		controller = self.controller
		label = tk.Label(self, text="game window")
		label.pack()

		button1 = tk.Button(self, text="go to menu window",
			command=lambda: controller.showFrame(menuWindow))
		button2 = tk.Button(self, text="go to gameWindow",
			command=lambda: controller.showFrame(gameWindow))

		button1.pack()
		button2.pack()

		# target creation and animation sholud probably
		# be in a class of its own. Do later.


	def createTargets(self):
		controller = self.controller
		master = self.master
		m = motionCapture(controller)
		controller.geometry("600x400")
		self.canvas = tk.Canvas(self, width=600, height=400)
		self.canvas.pack(fill="both", expand="True")

		self.frameCounter = 0
		self.centre = [200, 200]
		self.radius = 50


		self.setBounds()
		topLeft = self.topLeft
		bottomRight = self.bottomRight
		self.target_1 = self.canvas.create_oval(topLeft[0],topLeft[1],bottomRight[0],bottomRight[1], fill="blue")


	def animateTargets(self):
		self.radius -= 1
		self.setBounds()
		a = self.topLeft[0]
		b = self.topLeft[1]
		c = self.bottomRight[0]
		d = self.bottomRight[1]
		self.canvas.coords(self.target_1, a, b, c, d)
		self.master.update()


	def setBounds(self):

		self.topLeft = [self.centre[0] - self.radius, self.centre[1] - self.radius]
		self.bottomRight = [self.centre[0] + self.radius, self.centre[1] + self.radius]

		"""
		self.tk.bind("<F11>", self.toggle_fullscreen)
		self.tk.bind("<Escape>", self.end_fullscreen)
		self.tk.bind("<Button-1>", self.m.printCoords)
		"""
		

	

	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.tk.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.tk.attributes("-fullscreen", False)
		return "break"


class motionCapture:
	"""
	COMPLETE:	send positional data somewhere. Call from somewhere?
	"""
	def __init__(self, master):
		master.bind('<Motion>', self.motion)
		print("Motion capture initialized.")

	def motion(self, event):
		self.x, self.y = event.x, event.y
		self.printCoords()

	def printCoords(self, event=None):
		print('{}, {}'.format(self.x, self.y))


if __name__ == '__main__':

	main()