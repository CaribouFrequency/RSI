import tkinter as tk

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

class baseFrame(tk.Frame):

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

		


	def createTargets(self):
		controller = self.controller
		m = motionCapture(controller)
		controller.geometry("600x400")
		canvas = tk.Canvas(controller, width=600, height=400)
		canvas.pack()
		print(isinstance(controller, tk.Tk))
		"""
		self.m = motionCapture(self.tk)	#Created a mocap object within the game window.
		self.tk.attributes('-zoomed', False)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
		self.tk.attributes('-fullscreen','false')
		self.frame = Frame(self.tk, width=400, height=400)
		self.frame.pack()
		self.state = True
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