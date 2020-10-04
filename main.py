import string, pyperclip
import tkinter as tk
from random import choice, randint, sample
from configparser import ConfigParser


#characters = string.octdigits + string.ascii_letters# + string.punctuation



class ui(tk.Frame):

	def __init__(self):
		super().__init__()
		self.initiate_settings()
		self.initui()


	def initui(self):
		self.master.geometry("150x50+1700+60")
		self.master.title("pG")
		self.master.resizable(False,False)
		self.master.config(bg="#333")

		self.out = tk.Label(text="pass",font="Arial 13",bg="#222",fg="#fff")
		self.out.pack()
		
		tk.Button(text="Generate",font="Arial 12",bg="#444",fg="#fff",command=self.generate).pack()
		self.generate()
	
	def initiate_settings(self):
		try:
			cfg = ConfigParser()
			cfg.read('config.ini')
			self.s=int(cfg.get('main', 'symbols'))
			self.n=int(cfg.get('main', 'numbers'))
			self.p=int(cfg.get('main', 'punctuation'))
			self.c=int(cfg.get('main', 'is_copy_to_clipboard'))
		except:
			cfg['main'] = {'symbols' : '7', 'numbers' : '4', 'punctuation' : '1', 'is_copy_to_clipboard' : '1'}
			with open('config.ini', 'w') as configfile:
				cfg.write(configfile)
			self.initiate_settings()


	def generate(self):
		
		symbols = "".join(choice(string.ascii_letters) for x in range(self.s))
		numbers = "".join(choice(string.octdigits) for x in range(self.n))
		punctuation = "".join(choice(string.punctuation) for x in range(self.p))
		characters = symbols+numbers+punctuation
		password = ''.join(sample(characters,len(characters)))
		self.out.config(text=password)
		self.out.pack()
		if self.c == 1:
			pyperclip.copy(password)



if __name__ == "__main__":
	app = ui()
	app.master.mainloop()

#generate(4,3,3)

