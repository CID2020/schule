from os import error
from tkinter import *
import math
import matplotlib
#from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
matplotlib.use('TkAgg')
r4=4 #round to 4. digit after decimal
class Trigo():
  def __init__(self,v1=(),ns=0,nw=0):
    self.v1=v1
    self.ns=ns
    self.nw=nw
    self.fehler=0  #number of side, winkel
    self.lt=[] #latex text
    self.fmessage=['Please give at least 3 values',
    'Please make sure the inputs are numbers.(Write decimal as point)',
    'Please give at least 1 side length',
    'You cannot build a triangle with the 3 given number',
    'I only need 3 values',
    'All numbers must be positive',
    'Each angle in a triangle must be smaller than 180',
    'The sum of the two given angles must be smaller than 180']
  def generate(self):
    #in the function, it is shorter to write, 
    # therefore write seite länge as sl
    sl=[]
    wl=[]
    a1=random.randint(0,2)
    if a1==0: #sss
      while True:
        sl=[random.randint(2,9),random.randint(2,9),random.randint(2,9)]
        sl.sort()
        if sl[0]+sl[1]>sl[2]:
          break
      random.shuffle(sl)
      wl=[float('nan'),float('nan'),float('nan')]
    elif a1==1: #wsw
      w1=random.randint(20,160)
      w2=math.radians(random.randint(20,180-w1-20))
      w1=math.radians(w1)
      wl=[w1,w2,float('nan')]
      random.shuffle(wl)
      sl=[random.randint(2,9),float('nan'),float('nan')]
      random.shuffle(sl)
    elif a1==2: #sws
      w1=math.radians(random.randint(20,160))
      s1,s2=random.randint(2,9),random.randint(2,9)
      sl=[s1,s2]
      sl.sort()
      sl.append(float('nan'))
      if sl[1]/sl[0]*math.sin(w1)>1: 
      #it could be in ssw case unsolvable, just make it sws
        random.shuffle(sl)
        wl=[float('nan'),float('nan'),float('nan')]
        for n1 in range(3):
          if math.isnan(sl[n1]):
            wl[n1]=w1
      else:
        random.shuffle(sl)
        wl=[float('nan'),float('nan'),w1]
        random.shuffle(wl)
    return tuple(sl+wl)
  def sins(self,nw1,nw2,ns1,ns2,w1,w2,s1): #calculate a side with sin satz
    s2=s1/math.sin(w1)*math.sin(w2)
    tempt=f'\\dfrac{{{ns2}}}{{sin\\{nw2}}}=\\dfrac{{{ns1}}}{{sin\\{nw1}}}\\|\\cdot sin\\{nw2}'
    self.lt.append(tempt)
    tempt=f'{ns2}=\\dfrac{{{ns1}\\cdot sin\\{nw2}}}{{sin\\{nw1}}}={str(round(s2,r4))}'
    self.lt.append(tempt)
    return s2
  def sinw(self,nw1,nw2,ns1,ns2,w1,s1,s2):
    sw=math.sin(w1)/s1*s2
    w2=math.asin(sw)
    sw=round(sw,r4)
    tempt='\\dfrac{sin\\'+nw2+'}{'+ns2+'}=\\dfrac{sin\\'+nw1+'}{'+ns1+'}\\|\\cdot '+ns2
    self.lt.append(tempt)
    tempt='sin\\'+nw2+'=\\dfrac{sin\\'+nw1+'\\cdot '+ns2+'}{'+ns1+'}='+str(sw)
    self.lt.append(tempt)
    tempt='\\'+nw2+'='+str(round(math.degrees(w2),r4))
    self.lt.append(tempt)
    return w2
  def coss(self,nw,ns1,ns2,ns3,w,s1,s2):
    sq=(s1**2+s2**2-2*s1*s2*math.cos(w))
    s3=round(sq**(1/2),r4)
    tempt=ns3+'^2='+ns1+'^2+'+ns2+'^2-2'+ns1+ns2+'\\cdot cos\\'+nw
    self.lt.append(tempt)
    tempt=ns3+'='+str(s3)
    self.lt.append(tempt)
    return s3
  def cosw(self,nw,ns1,ns2,ns3,s1,s2,s3):
    cw=(s1**2+s2**2-s3**2)/(2*s1*s2)
    w=math.acos(cw)
    cw=round(cw,r4)
    tempt='cos\\'+nw+'=\\dfrac{'+ns1+'^2+'+ns2+'^2-'+ns3+'^2}{2'+ns1+ns2+'}='+str(cw)
    self.lt.append(tempt)
    tempt='\\'+nw+'='+str(round(math.degrees(w),r4))
    self.lt.append(tempt)
    return w
  def summe(self,n1,w1,w2):
    w3=math.pi-w1-w2
    if n1==1:
      tempt='\\alpha=180-\\beta-\\gamma='
    elif n1==2:
      tempt='\\beta=180-\\alpha-\\gamma='
    elif n1==3:
      tempt='\\gamma=180-\\alpha-\\beta='
    tempt+=str(round(math.degrees(w3),r4))
    self.lt.append(tempt)
    return w3
  def calculate(self):
    a,b,c,alphade,betade,gammade=self.v1
    alpha=math.radians(alphade)
    beta=math.radians(betade)
    gamma=math.radians(gammade)
    if self.ns+self.nw>3:
      self.fehler=4
    elif self.ns==3:
      if a+b>c and b+c>a and a+c>b:
        alpha=self.cosw('alpha','b','c','a',b,c,a,)
        beta=self.sinw('alpha','beta','a','b',alpha,a,b)
        gamma=self.summe(3,alpha,beta)
      else:
        self.fehler=3
    elif self.ns==2 and self.nw==1:
      if math.isnan(self.v1[0])^math.isnan(self.v1[3]) and math.isnan(self.v1[1])^math.isnan(self.v1[4]):
        if math.isnan(a):#sws
          a=self.coss('alpha','b','c','a',alpha,b,c)
          beta=self.sinw('alpha','beta','a','b',alpha,a,b)
          gamma=self.summe(3,alpha,beta)
        elif math.isnan(b):
          b=self.coss('beta','a','c','b',beta,a,c)
          alpha=self.sinw('beta','alpha','b','a',beta,b,a)
          gamma=self.summe(3,alpha,beta)
        elif math.isnan(c):
          c=self.coss('gamma','a','b','c',gamma,a,b)
          beta=self.sinw('gamma','beta','c','b',gamma,c,b)
          alpha=self.summe(1,beta,gamma)
      else:
        try:
          if math.isnan(a):
            if math.isnan(beta):
              beta=self.sinw('gamma','beta','c','b',gamma,c,b)
            else:
              gamma=self.sinw('beta','gamma','b','c',beta,b,c)
            alpha=self.summe(1,beta,gamma)
            a=self.sins('beta','alpha','b','a',beta,alpha,b)
          elif math.isnan(b):
            if math.isnan(alpha):
              alpha=self.sinw('gamma','alpha','c','a',gamma,c,a)
            else:
              gamma=self.sinw('alpha','gamma','a','c',alpha,a,c)
            beta=self.summe(2,alpha,gamma)
            b=self.sins('alpha','beta','a','b',alpha,beta,a)
          elif math.isnan(c):
            if math.isnan(beta):
              beta=self.sinw('alpha','beta','a','b',alpha,a,b)
            else:
              alpha=self.sinw('beta','alpha','b','a',beta,b,a)
            gamma=self.summe(3,alpha,beta)
            c=self.sins('alpha','gamma','a','c',alpha,gamma,a)
        except ValueError:
          self.fehler=3
    elif self.ns==1 and self.nw==2:
      if math.isnan(alpha):
        alpha=self.summe(1,beta,gamma)
      elif math.isnan(beta):
        beta=self.summe(2,alpha,gamma)
      elif math.isnan(gamma):
        gamma=self.summe(3,alpha,beta)
      if min(alpha,beta,gamma)<=0:
        self.fehler=7
      else:
        if not math.isnan(a):
          b=self.sins('alpha','beta','a','b',alpha,beta,a)
          c=self.sins('alpha','gamma','a','c',alpha,gamma,a)
        elif not math.isnan(b):
          a=self.sins('beta','alpha','b','a',beta,alpha,b)
          c=self.sins('beta','gamma','b','c',beta,gamma,b)
        elif not math.isnan(c):
          b=self.sins('gamma','beta','c','b',gamma,beta,gamma)
          a=self.sins('gamma','alpha','c','a',gamma,alpha,gamma)
    return self.fehler,[a,b,c,alpha,beta,gamma],self.lt
class Application():
  def __init__(self, master):
    self.master = master
    root.geometry('800x800+300+100') #size and initial position
    root.title('Trigonometrie')
    root.option_add('*Font', '30')
    self.v1=[]
    self.fehler=0
    self.lt=[]
    self.step1=0
    self.solved=False
    self.tosolve=False
    self.fmessage=['Please give at least 3 values',
    'Please make sure the inputs are numbers.(Write decimal as point)',
    'Please give at least 1 side length',
    'You cannot build a triangle with the 3 given number',
    'I only need 3 values',
    'All numbers must be positive',
    'Each angle in a triangle must be smaller than 180',
    'The sum of the two given angles must be smaller than 180']
    
    self.f1=Frame(root)
    self.la=Label(self.f1, text="a:").grid(row=0)
    self.ea=Entry(self.f1,width=10)
    self.ea.grid(row=0,column=1)
    self.lb=Label(self.f1, text="b:").grid(row=0,column=2)
    self.eb=Entry(self.f1,width=10)
    self.eb.grid(row=0,column=3)
    self.lc=Label(self.f1, text="c:").grid(row=0,column=4)
    self.ec=Entry(self.f1,width=10)
    self.ec.grid(row=0,column=5)
    self.lal=Label(self.f1, text="Alpha:").grid(row=1)
    self.eal=Entry(self.f1,width=10)
    self.eal.grid(row=1,column=1)
    self.lbe=Label(self.f1, text="Beta:").grid(row=1,column=2)
    self.ebe=Entry(self.f1,width=10)
    self.ebe.grid(row=1,column=3)
    self.lga=Label(self.f1, text="Gamma:").grid(row=1,column=4)
    self.ega=Entry(self.f1,width=10)
    self.ega.grid(row=1,column=5)
    self.f1.pack()
    self.le=[self.ea,self.eb,self.ec,self.eal,self.ebe,self.ega]#list of entry
    self.f2=Frame(root)
    self.b1=Button(self.f2,text='Generate a test',command=self.generate)
    self.b1.grid(row=0)
    self.b2=Button(self.f2,text='Show me the answer',command=self.anwser)
    self.b2.grid(row=0,column=2)
    self.b3=Button(self.f2,text='Reset',command=self.reset)
    self.b3.grid(row=0,column=3)
    self.f2.pack()
    self.lf=Label(root,text='')
    self.lf.pack()
    self.fig = matplotlib.figure.Figure(figsize=(6,8), dpi=100)
    self.wx = self.fig.add_subplot(111)
    self.canvas = FigureCanvasTkAgg(self.fig)
    self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    self.wx.get_xaxis().set_visible(False)
    self.wx.get_yaxis().set_visible(False)
  def generate(self):
    if not self.tosolve:
      trigo1=Trigo()
      self.v1=trigo1.generate()
      self.show()
      self.tosolve=True
  def latex1(self,lt): #a list of text
    for n1 in range(len(lt)):
      tmptext = "$"+lt[n1]+"$"
      self.wx.text(0.1, 0.9-n1/8, tmptext, fontsize = 20) #position-n1
    self.canvas.draw()
    self.wx.clear()
  def reset(self):
    self.ns=self.nw=0
    self.v1=[]
    self.lt=[]
    self.solved=self.tosolve=False
    self.step1=0
    self.lf.config(text = '')
    self.show()
  def show(self):
    self.latex1(self.lt[:self.step1])
    if not self.v1:
      for e1 in self.le:
        e1.delete(0,END)
    elif self.step1==len(self.lt):
      if self.step1:
        self.lf.config(text = 'Finished')
      for n1 in range(len(self.le)):
        if not len(self.le[n1].get()) and not math.isnan(self.v1[n1]):
          # second condition is used to generate homework
          if n1<3: #side
            self.le[n1].insert(0,round(self.v1[n1],2))
          else:
            self.le[n1].insert(0,round(math.degrees(self.v1[n1])))
  def anwser(self):
    if not self.solved:
      self.v1=[]
      self.ns=self.nw=0
      for n1 in range(len(self.le)):
        str1=self.le[n1].get()
        if not len(str1):
          self.v1.append(float('nan'))
        else:
          try:num1=float(str1)
          except ValueError:
            self.fehler=1
            break
          if num1<=0: self.fehler=5 # negative number
          self.v1.append(num1)
          if n1<3:self.ns+=1
          else:
            self.nw+=1
            if num1>=180: self.fehler=6 #angle is bigger than 180
      if self.fehler:
        self.lf.config(text =self.fmessage[self.fehler])
        self.fehler=0
      elif self.ns+self.nw<3:
        self.lf.config(text =self.fmessage[0])
      elif self.ns==0:
        self.lf.config(text =self.fmessage[2])
      else:
        trigo1=Trigo(self.v1,self.ns,self.nw)
        self.fehler,self.v1,self.lt=trigo1.calculate()
        if self.fehler:
          self.lf.config(text = self.fmessage[self.fehler])
          self.fehler=0
        else:
          self.solved=True
          self.lf.config(text = 'calculation: (continue clicking)')
    if self.step1<len(self.lt):
      self.step1+=1
      self.show()
if __name__ == '__main__':
  root = Tk()
  app = Application(root)
  def keyp(event):
    app.anwser()
  root.bind("<Return>",keyp)
  root.mainloop()
#improvement: change the number of Gleichungen with input