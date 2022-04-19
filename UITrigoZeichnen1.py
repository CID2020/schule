import tkinter as tk                    
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
class App():
  def __init__(self,root):
    self.gc=[] #guide code
    self.gt=[] #guide text
    #self.type1=0 #sss or sws or wsw
    self.step1=0
    self.root=root
    root.geometry('800x800+300+100')
    root.title('Dreieck Konstruktion')
    root.option_add('*Font', '30')
    self.fb1=ttk.Frame(self.root)
    ttk.Button(self.fb1,text='SSS',command=self.sss).grid()
    ttk.Button(self.fb1,text='SWS',command=self.sws).grid(row=0,column=1)
    ttk.Button(self.fb1,text='WSW',command=self.wsw).grid(row=0,column=2)
    ttk.Button(self.fb1,text='WSS1',command=self.wss1).grid(row=0,column=3)
    ttk.Button(self.fb1,text='WSS2',command=self.wss2).grid(row=0,column=4)
    ttk.Button(self.fb1,text='WSS3',command=self.wss3).grid(row=0,column=5)
    self.fb1.pack()

    self.f1=ttk.Frame(self.root)
    self.l1=ttk.Label(self.f1, text="s1:")
    self.l1.grid(row=0)
    self.e1=ttk.Entry(self.f1,width=10)
    self.e1.grid(row=0,column=1)
    self.l2=ttk.Label(self.f1, text="s2")
    self.l2.grid(row=0,column=2)
    self.e2=ttk.Entry(self.f1,width=10)
    self.e2.grid(row=0,column=3)
    self.l3=ttk.Label(self.f1, text="s3:")
    self.l3.grid(row=0,column=4)
    self.e3=ttk.Entry(self.f1,width=10)
    self.e3.grid(row=0,column=5)
    #self.f1.pack()
    
    self.fb=ttk.Frame(self.root) #frame of button
    ttk.Button(self.fb,text='<<',command=self.reset).grid()
    #ttk.Button(self.fb,text='Beginn',command=self.guide1).grid(row=0,column=1)
    ttk.Button(self.fb,text='Reset',command=self.reset).grid(row=0,column=2)
    ttk.Button(self.fb,text='>>',command=self.next).grid(row=0,column=3)
    self.fb.pack()
    self.lg=ttk.Label(root,text='(guide)') #label guide
    self.lg.pack()
    self.fig = matplotlib.figure.Figure(figsize=(3,4), dpi=100)
    self.wx = self.fig.add_subplot()
    self.canvas = FigureCanvasTkAgg(self.fig)
    self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.wx.set_xlim(0,1)
    self.wx.set_ylim(0,1)
    self.wx.set_aspect('equal')
    self.wx.get_xaxis().set_visible(False)
    self.wx.get_yaxis().set_visible(False)
    self.ll=[self.l1,self.l2,self.l3]
  def sss(self):
    self.gc=[] #guide code
    self.gt=[] #guide text
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.80,0.30,0.60,0.60
    r1=((x1-x3)**2+(y1-y3)**2)**(1/2)
    r2=((x2-x3)**2+(y2-y3)**2)**(1/2)
    self.gt.append('Eine Strecke mit der Länge s1 ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x2}],[{y1},{y2}],linewidth=3)") #,color='k'
    self.gt.append('Eine Strecke mit der Länge s1 ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x2})/2,({y1}+{y2})/2-0.05,'s1',fontsize=16)")
    self.gt.append('Ein Kreis um link Ende mit Radius s2 ziehen')
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x1},{y1}),{r1},fill=False,linestyle=':',linewidth=1))")
    self.gt.append('Ein Kreis um recht Ende mit Radius s3 ziehen')
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x2},{y2}),{r2},fill=False,linestyle=':',linewidth=1))")
    self.gt.append('Die 2 Kreise Schneiden sich auf ein Punkt')
    self.gc.append(f"self.wx.plot([{x3}],[{y3}],marker='.',markersize=10)")
    self.gt.append('Eine Strecke von link Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Eine Strecke von link Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x3})/2-0.1,({y1}+{y3})/2,'s2',fontsize=16)")
    self.gt.append('Eine Strecke von recht Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.plot([{x2},{x3}],[{y2},{y3}],linewidth=3)")
    self.gt.append('Eine Strecke von recht Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.text(({x2}+{x3})/2+0.05,({y2}+{y3})/2,'s3',fontsize=16)")
  def sws(self):
    self.gc=[] #guide code
    self.gt=[] #guide text
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.5,0.30,0.60,0.7
    r1=x2-x1
    r2=((x1-x3)**2+(y1-y3)**2)**(1/2)
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1}],[{y1}],marker='.',markersize=10)")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1},1],[{y1},{y2}],linestyle=':')")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1},0.9],[{y1},1],linestyle=':')")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.text({x1}+0.05,{y1}+0.02,'α',fontsize=16)")
    self.gt.append('Ein Kreis mit Radius s1 ziehen')
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x1},{y1}),{r1},fill=False,linestyle=':'))")
    self.gt.append('Schneidet auf ein Punkt auf dem Strahl')
    self.gc.append(f"self.wx.plot([{x1}+{r1}],[{y1}],marker='.',markersize=10)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x2}],[{y1},{y2}],linewidth=3)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x2})/2,({y1}+{y2})/2-0.05,'s1',fontsize=16)")
    self.gt.append('Ein Kreis mit Radius s2 ziehen')
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x1},{y1}),{r2},fill=False,linestyle=':'))")
    self.gt.append('Schneidet auf ein Punkt auf dem 2. Strahl')
    self.gc.append(f"self.wx.plot([{x3}],[{y3}],marker='.',markersize=10)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x3})/2-0.05,({y1}+{y3})/2,'s2',fontsize=16)")
    self.gt.append('Die 3. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x3},{x2}],[{y3},{y2}],linewidth=3)")
  def wsw(self):
    self.gc=[] #guide code
    self.gt=[] #guide text
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.80,0.30,0.54,0.56
    r1=((x1-x3)**2+(y1-y3)**2)**(1/2)
    r2=((x2-x3)**2+(y2-y3)**2)**(1/2)
    self.gt.append('Eine Strecke mit der Länge s ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x2}],[{y1},{y2}],linewidth=3)")
    self.gt.append('Eine Strecke mit der Länge s ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x2})/2,({y1}+{y2})/2-0.05,'s',fontsize=16)")
    self.gt.append('Die Winkel1 vom link Ende ziehen')
    self.gc.append(f"self.wx.plot([{x1},1],[{y1},0.9],linestyle=':')")
    self.gt.append('Die Winkel1 vom link Ende ziehen')
    self.gc.append(f"self.wx.text({x1}+0.07,{y1}+0.02,'α',fontsize=16)")
    self.gt.append('Die Winkel2 vom recht Ende ziehen')
    self.gc.append(f"self.wx.plot([{x2},0.1],[{y1},1],linestyle=':')")
    self.gt.append('Die Winkel2 vom recht Ende ziehen')
    self.gc.append(f"self.wx.text({x2}-0.1,{y1}+0.02,'β',fontsize=16)")
    self.gt.append('Zwei Strahle schneiden sich auf ein Punkt')
    self.gc.append(f"self.wx.plot([{x3}],[{y3}],marker='.',markersize=10)")
    self.gt.append('Eine Strecke von link Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Eine Strecke von recht Ende zum Schnittpunkt ziehen')
    self.gc.append(f"self.wx.plot([{x3},{x2}],[{y3},{y2}],linewidth=3)")
    self.canvas.draw()
  def wss(self):
    self.gc=[] #guide code
    self.gt=[] #guide text
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.5,0.30,0.60,0.7
    r1=x2-x1
    r2=((x1-x3)**2+(y1-y3)**2)**(1/2)
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1}],[{y1}],marker='.',markersize=10)")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1},1],[{y1},{y2}],linestyle=':')")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.plot([{x1},0.9],[{y1},1],linestyle=':')")
    self.gt.append('Die Winkel ziehen')
    self.gc.append(f"self.wx.text({x1}+0.05,{y1}+0.02,'α',fontsize=16)")
    self.gt.append('Ein Kreis mit Radius s1 ziehen')
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x1},{y1}),{r2},fill=False,linestyle=':'))")
    self.gt.append('Schneidet auf ein Punkt auf dem Strahl')
    self.gc.append(f"self.wx.plot([{x3}],[{y3}],marker='.',markersize=10)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Eine Strecke ziehen')
    self.gc.append(f"self.wx.text(({x1}+{x3})/2-0.05,({y1}+{y3})/2,'s1',fontsize=16)")
    self.gt.append('Ein Kreis um Schnittpunkt mit Radius s2 ziehen')
  def wss1(self):
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.5,0.30,0.60,0.7
    r1=x2-x1
    r2=y3-y1-0.1
    self.wss()
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x3},{y3}),{r2},fill=False,linestyle=':'))")
    self.gt.append('Kein Schnittpunkt auf dem Strahl, unmöglich')
    self.gc.append('pass')
  def wss2(self):
    self.wss()
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.5,0.30,0.60,0.7
    r1=x2-x1
    r2=y3-y1
    self.wss()
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x3},{y3}),{r2},fill=False,linestyle=':'))")
    self.gt.append('Ein Schnittpunkt auf dem Strahl')
    self.gc.append(f"self.wx.plot([{x3}],[{y1}],marker='.',markersize=10)")
    self.gt.append('Die 2. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x3},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Die 2. Strecke ziehen')
    self.gc.append(f"self.wx.text({x3}+0.03,({y1}+{y3})/2,'s2',fontsize=16)")
    self.gt.append('Die 3. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x3}],[{y1},{y1}],linewidth=3)")
  def wss3(self):
    self.wss()
    x1,y1,x2,y2,x3,y3=0.20,0.30,0.5,0.30,0.60,0.7
    r1=x2-x1
    r2=y3-y1+0.05
    x4,x5=x3-0.2,x3+0.2
    self.wss()
    self.gc.append(f"self.wx.add_patch(plt.Circle(({x3},{y3}),{r2},fill=False,linestyle=':'))")
    self.gt.append('2 Schnittpunkte auf dem Strahl')
    self.gc.append(f"self.wx.plot([{x4}],[{y1}],marker='.',markersize=10)")
    self.gt.append('2 Schnittpunkte auf dem Strahl')
    self.gc.append(f"self.wx.plot([{x5}],[{y1}],marker='.',markersize=10)")
    self.gt.append('Die 2. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x4},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Die 2. Strecke ziehen')
    self.gc.append(f"self.wx.text(({x4}+{x3})/2+0.04,({y1}+{y3})/2,'s2',fontsize=16)")
    self.gt.append('Die 3. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x4}],[{y1},{y1}],linewidth=3)")
    self.gt.append('Die 2. Strecke ziehen (2. Möglichkeit)')
    self.gc.append(f"self.wx.plot([{x5},{x3}],[{y1},{y3}],linewidth=3)")
    self.gt.append('Die 2. Strecke ziehen (2. Möglichkeit)')
    self.gc.append(f"self.wx.text(({x5}+{x3})/2+0.04,({y1}+{y3})/2,'s2',fontsize=16)")
    self.gt.append('Die 3. Strecke ziehen')
    self.gc.append(f"self.wx.plot([{x1},{x5}],[{y1},{y1}],linewidth=3)")
  def sammeln(self):
    input1=[self.e1.get(), self.e2.get(),self.e3.get()]
    inputn=[]
    for i in input1:
      if not len(i):
        self.lg.config(text='Die Eingaben vollständig geben')
        break
      try:inputn.append(float(i))
      except ValueError:
        self.lg.config(text='Alle Eingaben müssen Zahlen sein')        
        break
    return inputn
  def reset(self):
    self.step1=0
    self.lg.config(text='(Guide)')
    self.wx.clear()
    self.wx.set_xlim(0,1)
    self.wx.set_ylim(0,1)
    self.wx.set_aspect('equal')
    self.canvas.draw()
  def next(self):
    if self.step1<len(self.gc):
      exec(self.gc[self.step1])
      self.lg.config(text=self.gt[self.step1])
      self.step1+=1
    self.canvas.draw()
if __name__ == '__main__':
  root = tk.Tk()
  root.title("Tab Widget")
  app = App(root)
  def keyp(event):
    app.next()
  root.bind("<Return>",keyp)
  root.mainloop()