import random
def gcd(a, b):
  if b == 0:return a
  return gcd(b, a % b)
def fw(z1,n1,op='',f1='',po=''): #operator, position
  if n1==1 and not op:
    return str(z1)
  elif po=='o': #position is oben
    return '\\dfrac{'+str(z1)+op+str(f1)+'}{'+str(n1)+'}'
  elif po=='u': #unten
    return '\\dfrac{'+str(z1)+'}{'+str(n1)+op+str(f1)+'}'
  elif not po and f1!=1:
    return '\\dfrac{'+str(z1)+op+str(f1)+'}{'+str(n1)+op+str(f1)+'}'
  elif not po and f1==1:
    return '\\dfrac{'+str(z1)+'}{'+str(n1)+'}'
class Bru():
  def __init__(self,z1,n1,op='',f1=''):
    self.z1=z1
    self.n1=n1
    self.op=op
    self.f1=f1
  def dru(self):
    return fw(self.z1,self.n1)
  def kz(self):
    if gcd(self.z1,self.n1)==1:
      return [self.z1,self.n1,fw(self.z1,self.n1),fw(self.z1,self.n1)]
    else:
      fk=int(gcd(self.z1,self.n1))
      z2=int(self.z1/fk)
      n2=int(self.n1/fk)
      return [z2,n2,fw(self.z1,self.n1,'/',fk),fw(z2,n2)]
class BruR():#bruch Rechnen
  def __init__(self,bb=[]):
    self.lt=[]
    self.bb=bb #bruch 1 und 2
    if not bb[0] and not bb[1] and not bb[2] and not bb[3] and bb[4]=='+-*/':
      while True:
        chance1=[4,4,4,8,2,8,2,8,4,8,1,12] #chance list
        numbers=list(range(1,13))
        self.bb=random.choices(numbers, weights=chance1,k=4)
        lv=['+','-','*','/']
        tempv=random.choices(lv)
        self.bb.append(tempv[0])
        if (not self.bb[1]==self.bb[3]==1 
        and not self.bb[0]==self.bb[1]
        and not self.bb[2]==self.bb[3]): break 
    else:
      for n1 in bb:
        if n1==0:
          self.lt.append('Bitte die Eingabe vollständig geben'+
          ' oder alle frei lassen (Reset)')
          break
      #both number are not fraction, zähler ist gleich nenner
    # self.v1=[]
    # self.vr=[1,random.choice([-1,1])] #vorzeichen rechnen
    # self.v1.append('') #empty for the first fraction, change later
    # for n1 in range(1,2):
    #   if self.vr[n1]<0: self.v1.append('-')
    #   else: self.v1.append('+')
  def rechnen(self):
    if not self.lt:
      if self.bb[4]=='+' or self.bb[4]=='-':
        self.pm()
      elif self.bb[4]=='*' or self.bb[4]=='/':
        self.md()
    return self.lt
  def pm(self):
    z1,n1,z2,n2,op=self.bb #shorter to write
    v1='' #vorzeichen, vielleicht später
    self.lt.append('$'+v1+fw(z1,n1)+op+fw(z2,n2)+'$')
    if gcd(z1,n1)>1 or gcd(z2,n2)>1 and n1!=n2:
      self.lt.append('Kurzen wenn es möglich ist')
      z1,n1,m11,m12=Bru(z1,n1).kz() 
      #kurzen returns 2 steps, or just repeat it
      z2,n2,m21,m22=Bru(z2,n2).kz()
      self.lt.append('$'+v1+m11+op+m21+'$')
      self.lt.append('$'+v1+m12+op+m22+'$')
    if n1!=n2:
      self.lt.append('Die 2 Zähler sind unterschiedlich, muss man erweitern.')
      n3=int(n1*n2/gcd(n1,n2))
      f1=int(n3/n1) #faktor
      f2=int(n3/n2)
      self.lt.append('Der gemeinsame Zähler ist '+str(n3))
      self.lt.append('$'+v1+fw(z1,n1,'*',f1)+op+fw(z2,n2,'*',f2)+'$')
      n1=n1*f1 #neue nenner, zähler, from here, n1=n2
      z1=z1*f1
      z2=z2*f2
      self.lt.append('$'+v1+fw(z1,n1)+op+fw(z2,n1)+'$')
    if op=='+':zz=z1+z2
    else:zz=z1-z2
    self.lt.append('Die Nenner bleibt und die Zähler addieren sich')
    self.lt.append('$'+v1+fw(z1,n1,op,z2,'o')+'$') # add zähler together
    self.lt.append('$'+v1+fw(zz,n1)+'$')
    if gcd(zz,n1)>1:
      #f3=gcd(zz,n1)
      self.lt.append('Kurzen wenn es möglich ist')
      zz,n1,m1,m2=Bru(zz,n1).kz()
      self.lt.append('$='+m1+'$')
      self.lt.append('$='+m2+'$')
  def md(self):
    z1,n1,z2,n2,op=self.bb #shorter to write
    v1=''
    if op=='/':
      self.lt.append('$'+v1+fw(z1,n1)+op+fw(z2,n2)+'$')
      self.lt.append('Durch ein Bruch ist gleich mal das Kehrwert')
      tempn=n2
      n2=z2
      z2=tempn
    self.lt.append('$'+v1+fw(z1,n1)+'*'+fw(z2,n2)+'$')
    if gcd(z1,n1)>1 or gcd(z2,n2)>1:
      self.lt.append('Kurzen wenn es möglich ist')
      z1,n1,m11,m12=Bru(z1,n1).kz() #message
      z2,n2,m21,m22=Bru(z2,n2).kz()
      self.lt.append('$'+v1+m11+'*'+m21+'$')
      self.lt.append('$'+v1+m12+'*'+m22+'$')
    if gcd(z1,n2)>1:
      self.lt.append('Kurzen wenn es möglich ist')
      f1=int(gcd(z1,n2))
      self.lt.append('$'+v1+fw(z1,n1,'/',f1,'o')+'*'+fw(z2,n2,'/',f1,'u')+'$')
      z1=int(z1/f1)
      n2=int(n2/f1)
      self.lt.append('$'+v1+fw(z1,n1)+'*'+fw(z2,n2)+'$')
    if gcd(z2,n1)>1:
      self.lt.append('Kurzen wenn es möglich ist')
      f1=int(gcd(z2,n1))
      self.lt.append('$'+v1+fw(z1,n1,'/',f1,'u')+'*'+fw(z2,n2,'/',f1,'o')+'$')
      z2=int(z2/f1)
      n1=int(n1/f1)
      self.lt.append('$'+v1+fw(z1,n1)+'*'+fw(z2,n2)+'$')
    self.lt.append('Zähler mal Zähler, Nenner mal Nenner')
    self.lt.append('$'+v1+fw(str(z1)+'*'+str(z2),str(n1)+'*'+str(n2))+'$')
    z1=z1*z2
    n1=n1*n2
    self.lt.append('$'+v1+fw(z1,n1)+'$')