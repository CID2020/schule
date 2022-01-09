#import pyperclip
import random
def gcd(a, b):
  if b == 0:return a
  return gcd(b, a % b)
def pm():
  a1=1 if bool(random.getrandbits(1)) else -1
  return a1
def vorf(n1): #vorzeichen vor Faktor
  if n1>=0:return '+'+vor1(n1)
  else: return vor1(n1)
def vorz(n1):
  if n1>=0:return '+'+str(n1)
  else: return str(n1)
def vor1(n1): # das 1x problem
  if n1==1:return ''
  elif n1==-1:return '-'
  else: return str(n1)
def dru(x1,y1,z1): #print the equation
  str1=vor1(x1)+'x'+vorf(y1)+'y='+str(z1)+'\n'
  return str1
def add1(x1,y1,z1,x2,y2,z2):
  str1=(vor1(x1)+'x'+vorf(y1)+'y'+vorf(x2)+'x'+vorf(y2)+'y='
  +str(z1)+vorz(z2)+'\n')
  return str1
def zuAdd(n1,n2,buch,z1,z2): #zusammenfassen nach addition, buchstaben
  str1=vor1(n1+n2)+buch+'='+str(z1+z2)+' |/('+str(n1+n2)+')\n'
  return str1
def einsetz(buch,n1,x1,y1,z1):
  if buch=='x':
    str1=str(x1)+'*('+str(n1)+')'+vorf(y1)+'y='+str(z1)+'\n'
  elif buch=='y':
    str1=vor1(x1)+'x'+vorz(y1)+'*('+str(n1)+')='+str(z1)+'\n'
  return str1
def zuEin(buch,n1,m1,z1): #zusammenfassen nach einsetzen, m-mal ergebniss
  if buch=='x':
    str1=str(m1)+vorf(n1)+'y='+str(z1)+' |-('+str(m1)+')\n'
  elif buch=='y':
    str1=str(n1)+'x'+vorz(m1)+'='+str(z1)+' |-('+str(m1)+')\n'
  return str1
def vorl(buch,n1,z1): #vorletzte Schritt
  if buch=='x':buch='y'
  elif buch=='y':buch='x'
  return vor1(n1)+buch+'='+str(z1)+' |/('+str(n1)+')\n'
class GleiR():
  def __init__(self,g22=[]):
    if not g22:
      while True: #g22[xi1,yi1,xi]
        chance1=[4,4,4,8,2,8,2,8,4,8] #chance list
        numbers=list(range(1,11))
        g22=random.choices(numbers, weights=chance1,k=8)
        for k1 in range(len(g22)):
          g22[k1]=g22[k1]*pm()
        g22.append(g22[0]*g22[4]+g22[1]*g22[5])
        g22.append(g22[2]*g22[6]+g22[3]*g22[7])
        if (True): break #fit the condition, otherwise generate another
      self.g22=[g22[0],g22[1],g22[-2],g22[2],g22[3],g22[-1]] 
      #return only index [x1,y1,x2,y2,z1,z2]
    else: self.g22=g22
    self.guide=''
  def faktor(self): #find out the factor, which will bei multiplied
    x1,y1,z1,x2,y2,z2=self.g22
    self.guide+='(1)'+dru(x1,y1,z1)
    self.guide+='(2)'+dru(x2,y2,z2)
    if x1==-x2 or y1==-y2:
      return 1,1
    elif x1==x2 or y1==y2:
      return 1,-1
    elif not x1%x2:
      if x1*x2>0:return 1,-x1//x2
      elif x1*x2<0:return 1,-x1//x2
    elif not x2%x1:
      if x1*x2>0:return -x2//x1,1
      elif x1*x2<0:return -x2//x1,1
    elif not y1%y2:
      if y1*y2>0:return 1,-y1//y2
      elif y1*y2<0:return 1,-y1//y2
    elif not y2%y1:
      if y1*y2>0:return -y2//y1,1
      elif y1*y2<0:return -y2//y1,1
    else:#worst case
      gdx=gcd(x1,x2) #greatest common divider
      lmx=x1*x2/gdx #least common multiple
      gdy=gcd(y1,y2)
      lmy=y1*y2/gdy
      if lmx>lmy>1:
        if x1*x2<0:return x2//gdx,x1//gdx
        elif x1*x2>0:return -x2//gdx,x1//gdx
      else:
        if y1*y2<0:return y2//gdy,y1//gdy
        elif y1*y2>0:return -y2//gdy,y1//gdy
  def einsetzen(self,buch,n0):
    x1,y1,z1,x2,y2,z2=self.g22
    self.guide+=buch+' in (1) einsetzen\n'
    self.guide+=einsetz(buch,n0,x1,y1,z1)
    if buch=='x':
      tm=x1*n0
      self.guide+=zuEin('x',y1,tm,z1)
      tz=z1-tm #temp z
      self.guide+=vorl('x',y1,tz)
      te=tz//y1 #temp ergebnis
      self.guide+='y='+str(te)
    elif buch=='y':
      tm=y1*n0 #mal temp
      self.guide+=zuEin('y',x1,tm,z1)
      tz=z1-tm #temp z
      self.guide+=vorl('y',x1,tz)
      te=tz//x1 #temp ergebnis
      self.guide+='x='+str(te)
  def addieren(self,x1,y1,z1,x2,y2,z2):
    self.guide+=(add1(x1,y1,z1,x2,y2,z2))
    if x1+x2==0:
      self.guide+=str(x1)+'x und '+str(x2)+'x sind aufgehoben\n'
      self.guide+=zuAdd(y1,y2,'y',z1,z2)
      y0=(z1+z2)//(y1+y2)
      self.guide+='y='+str(y0)+'\n'
      self.einsetzen('y',y0)
    elif y1+y2==0:
      self.guide+=str(y1)+'y und '+str(y2)+'y sind aufgehoben\n'
      self.guide+=zuAdd(x1,x2,'x',z1,z2)
      x0=(z1+z2)//(x1+x2)
      self.guide+='x='+str(x0)+'\n'
      self.einsetzen('x',x0)
  def calc(self):
    x1,y1,z1,x2,y2,z2=self.g22
    f1=self.faktor()
    if f1[0]==f1[1]==1:
      self.guide+=('(1)+(2)\n')
      self.addieren(x1,y1,z1,x2,y2,z2)
    elif f1[0]==1:
      self.guide+='(2)|*'+str(f1[1])+'\n'
      x3=x2*f1[1]
      y3=y2*f1[1]
      z3=z2*f1[1]
      self.guide+='(3)'+dru(x3,y3,z3)
      self.guide+='(1)+(3)'
      self.addieren(x1,y1,z1,x3,y3,z3)
    elif f1[1]==1:
      self.guide+='(1)|*'+str(f1[0])+'\n'
      x3=x1*f1[0]
      y3=y1*f1[0]
      z3=z1*f1[0]
      self.guide+='(3)'+dru(x3,y3,z3)
      self.guide+='(2)+(3)\n'
      self.addieren(x2,y2,z2,x3,y3,z3)
a1=GleiR([1,-1,10,6,-3,42])
a1.calc()
print(a1.guide)
#pyperclip.copy(a1.guide)
