import tkinter as tk

def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()
def test1():
  print('test1')    
HEIGHT = 300
WIDTH = 500

ws = tk.Tk()
ws.title("Python Guides")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(ws, text="Click ME", bg='White', fg='Black',
command=lambda:test1()) #command=lambda: New_Window())

button.pack()
ws.mainloop()