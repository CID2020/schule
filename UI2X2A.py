from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from c2X2A import *
Builder.load_file('kv2X2A.kv')
class Layout1(Widget):
  def lö1(self):
    g1=Glei1(*self.g1.text.split('='))
    g2=Glei1(*self.g2.text.split('='))
    gg=Glei22(g1,g2)
    ins1=gg.lösen()
    self.output1.text=ins1[0]
  def lösen(self):
    try: self.lö1()
    except: self.output1.text='Fehler!'
  def reset(self):
    self.g1.text=self.g2.text=self.output1.text=''
  def gen(self):
    g22=gen22()
    self.g1.text=g22.g1.str1()
    self.g2.text=g22.g2.str1()
    self.output1.text=''
  def test1(self):
    self.output1.text='test2'
class Tapp(App):
  fs1=28 #font size
  fs2=28
  def build(self):
    return Layout1()
if __name__ == '__main__':
  Tapp().run()