from kivy.app import App 
from kivy.uix.image import Image 


class MainApp(App):
	def build(self):
		img = Image(source="/home/atulrpai/Downloads/SL_mango.jpg")

		return img

if __name__ == "__main__":
	app = MainApp()
	app.run()