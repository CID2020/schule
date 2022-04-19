import tkinter as tk                    
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class App():
  def __init__(self,root):
    self.root = root
    root.title('Dreieck Konstruktion')
    root.option_add('*Font', '30')
    self.nb=ttk.Notebook(self.root)
    self.tab1 = ttk.Frame(self.nb)
    self.tab2 = ttk.Frame(self.nb)
    self.f1=ttk.Frame(self.tab1)
    ttk.Label(self.f1, text="s1:").grid(row=0)
    self.t11=ttk.Entry(self.f1,width=10)
    self.t11.grid(row=0,column=1)
    ttk.Label(self.f1, text="s2:").grid(row=0,column=2)
    self.t12=ttk.Entry(self.f1,width=10)
    self.t12.grid(row=0,column=3)
    ttk.Label(self.f1, text="s3:").grid(row=0,column=4)
    self.t13=ttk.Entry(self.f1,width=10)
    self.t13.grid(row=0,column=5)
    self.f1.pack()
    ttk.Label(self.tab2,
              text ="Lets dive into the\
              world of computers").grid(column = 0,
                                        row = 0, 
                                        padx = 30,
                                        pady = 30)     
    self.nb.add(self.tab1, text ='SSS')
    self.nb.add(self.tab2, text ='Tab 2')
    self.nb.pack(expand = 1, fill ="both")
    self.fb=ttk.Frame(self.tab1) #frame of button
    ttk.Button(self.fb,text='>>',command=self.guide1).pack()
    ttk.Button(self.fb,text='<<',command=self.guide1).pack()
    self.g1=ttk.Label(root,text='guide')
    self.g1.pack()
    self.fig = matplotlib.figure.Figure(figsize=(3,4), dpi=100)
    self.wx = self.fig.add_subplot()
    self.canvas = FigureCanvasTkAgg(self.fig)
    self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.wx.get_xaxis().set_visible(False)
    self.wx.get_yaxis().set_visible(False)
  def guide1(self):
    tabn=self.nb.index(self.nb.select())
    if tabn==0:
      pass
    elif tabn==1:
      pass
    print('test1')
if __name__ == '__main__':
  root = tk.Tk()
  root.title("Tab Widget")

  app = App(root)
  def keyp(event):
    app.answer()
  #root.bind("<Return>",keyp)
  root.mainloop()