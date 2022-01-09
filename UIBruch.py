from matplotlib import pyplot as plt
#from kivy.garden.matplotlib import FigureCanvasKivyAgg
from backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from cBruch1 import BruR
Builder.load_file('bruch.kv')
class Layout1(Widget):
  llatex=ObjectProperty(None)
  lguide=ObjectProperty(None)
  #z1=ObjectProperty(None)
  drawn=False
  ltp=[] #latex text to print
  bb=[0,0,0,0,'+-*/'] #bruch
  def funkz1(self,var1):
    self.bb[0]=int(var1)
  def funkn1(self,var1):
    self.bb[1]=int(var1)
  def funkz2(self,var1):
    self.bb[2]=int(var1)
  def funkn2(self,var1):
    self.bb[3]=int(var1)
  def funkop(self,var1):
    self.bb[4]=var1
  def generate(self):
    br1=BruR(self.bb)
    self.lt=br1.rechnen()
    print(self.lt)
    self.show()
  def answer(self):
    if hasattr(self,'lt'):
      if self.lt:
        self.show()
  def show(self):
    if self.drawn:
      plt.close(self.plot.figure)
      self.llatex.remove_widget(self.plot)
    plt.plot(figsize=(4,3))
    plt.axis('off')
    self.plot = FigureCanvasKivyAgg(plt.gcf())
    self.llatex.add_widget(self.plot)
    if self.lt[0][0]==self.lt[0][-1]=='$': #it is a function
      self.ltp.append(self.lt.pop(0))
      if len(self.ltp)>5:
        self.ltp.pop(0)
    else:self.lguide.text=self.lt.pop(0)
    for n1 in range(len(self.ltp)):
      plt.gcf().text(0.1,0.85-0.18*n1,self.ltp[n1],fontsize=22)
    self.drawn=True
  def reset(self):
    self.ltp=[]
    self.lt=['Noch mal']
    self.ids.z1.text='0'
    self.ids.z2.text='0'
    self.ids.n1.text='0'
    self.ids.n2.text='0'
    self.ids.op.text='+-*/'
    self.show()
  def test1(self):
    print(self.ids.z1.text)
    print(self.bb)
class Tapp(App):
  ln=[]
  for n1 in range(1,16):
    ln.append(str(n1)) #list of number
  lv=['+','-','*','/']
  fs0=40
  fs1=34
  fs2=28
  cl1=(0, 0, 0, 1)
  def build(self):
    return Layout1()
if __name__ == '__main__':
  Tapp().run()