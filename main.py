#codigo para ver a hora usando tela com tkinter

from tkinter import *
    
import time

class Relogio():
  def __init__(self, root):
    self.label1 = Label(root, text="")
    self.label1.pack()
    self.atualizar_hora()

  def atualizar_hora(self):
    now = time.strftime("%H:%M:%S")
    self.label1['text']= now
    root.after(1000, self.atualizar_hora)

root = Tk()
app = Relogio(root)
root.mainloop()