'''replace a normal variable with term, init with a *args
+- problem, klammern auflösen, zusammenfassen,
from written term to list'''
import numpy as np
import random

from numpy.typing import _128Bit
def pm():
    if bool(random.getrandbits(1)): return 1
    else: return -1
def r19():
    numbers=list(range(1,8))
    chance1 = [x+4 for x in numbers]
    chance1.reverse()
    a=random.choices(numbers, weights=chance1,k=30)
    a=[x*pm() for x in a]
    return a
def gen2(x1,y1,v1,v2,rlr): #generate 1 Gleichung
  r1=r19() #a1x+b1y+c1=0
  a1=r1.pop()
  b1=r1.pop()
  c1=-a1*x1-b1*y1
  if not rlr: return Glei1([a1,v1,b1,v2],[-c1,''])
  else:
    l1=[a1,v1,b1,v2,c1,'']
    ir=random.randint(0,2) #index random
    l2=[l1.pop(ir*2),l1.pop(ir*2)]
    if bool(random.getrandbits(1)): return Glei1(l2,l1)
    else: return Glei1(l1,l2)
def gen3(x,y,z): #generate 1 Gleichung with 3 variable
  r1=r19() #a1x+b1y+c1=0
  a,b,c=r1.pop(),r1.pop(),r1.pop()
  d=a*x+b*y+c*z
  return Glei1([a,'x',b,'y',c,'z'],[d,''])
def gen22(rv=False,rlr=False):
  r1=r19()
  x1,y1=r1.pop(),r1.pop()
  if rv:
    v1=abc.pop(random.randint(0,25))
    v2=abc.pop(random.randint(0,24))
  else:
    v1='x'
    v2='y'
  g1=gen2(x1,y1,v1,v2,rlr)
  g2=gen2(x1,y1,v1,v2,rlr)
  return Glei22(g1,g2)
def gen33():
  r1=r19()
  x,y,z=r1.pop(),r1.pop(),r1.pop()
  g1=gen3(x,y,z)
  g2=gen3(x,y,z)
  g3=gen3(x,y,z)
  return Glei33(g1,g2,g3)
def gcd(a, b):
  if b == 0:return a
  return gcd(b, a % b)
sp='     '
abc=list('abcdefghijklmnopqrstuvwxyz')
def bu(s1):
  k1=False
  if '(' and ')' in s1:
    s2=s1.split('(', 1)[1].split(')')[0]
    s1=s1.replace(f'({s2})','z')
    t1=Term(bu(s2))
    k1=True
  l1=[]
  vz=True #erwarte ein Variable
  i=len(s1)-1
  while i>-1:
    if vz:
      if s1[i].isalpha():
        l1=[s1[i]]+l1
        i-=1
        if i==-1: l1=[1]+l1 #start with a letter
      elif s1[i].isdigit(): l1=['']+l1
      vz=False
    else:
      i2=i+1 #save position of the digit
      while s1[i].isdigit() and i>-1: i-=1
      if i2==i+1:
        if s1[i]=='+': l1=[1]+l1
        elif s1[i]=='-': l1=[-1]+l1
      elif i>0: # not at begining
        if s1[i]=='+': l1=[int(s1[i+1:i2])]+l1
        elif s1[i]=='-': l1=[int(s1[i:i2])]+l1
      else: l1=[int(s1[0:i2])]+l1
      i-=1
      vz=True
  if k1:
    l1[l1.index('z')]=t1
  return l1
class Term():
  def __init__(self,l1):
    if type(l1)==list:
      self.l1=l1
      if not l1: self.l1=[0,'']
    elif type(l1)==str: self.l1=bu(l1)
  def str1(self):
    s1=''
    for i in range(0,len(self.l1),2):
      if self.l1[i]==1:
        if i>0: s1+='+'
        if not self.l1[i+1]: s1+='1' #wenn 1 alleine
      elif self.l1[i]==-1:
        s1+='-'
        if not self.l1[i+1]: s1+='1' #wenn 1 alleine
      elif self.l1[i]>0: 
        if i==0: s1+=str(self.l1[i])
        else: s1+='+'+str(self.l1[i])
      else: s1+=str(self.l1[i])
      if type(self.l1[i+1])==str: s1+=self.l1[i+1]
      else: s1+=f'({str(self.l1[i+1])})'
    return s1
  def __repr__(self):
    return self.str1()
  def __add__(self,other): #plus oder minus term
    return Term(self.l1+other.l1)
  def __sub__(self,other):
    l1=other.l1.copy() #should not change the oritinal other
    for i in range(0,len(l1),2): l1[i]*=-1
    return self+Term(l1) #Term(self.l1+other.l1)
  def __mul__(self,f1):
    l1=self.l1.copy() #should not change self.l1 when calculate others
    for i in range(0,len(l1),2): l1[i]*=f1
    return Term(l1)
  def __truediv__(self,f1):
    l1=self.l1.copy()
    for i in range(0,len(l1),2):
      l1[i]=int(round(l1[i]/f1))
    return Term(l1)
  def kla(self): #klammern lösen
    l1=self.l1.copy()
    for i in range(len(self.l1)-2,-1,-2): #until -1 but not include -1
      if type(l1[i+1])==Term:
        t1=l1[i+1]*l1[i]
        l1.pop(i)
        l1.pop(i)
        l1[i:i]=t1.l1
    return Term(l1)
  def zus(self): #zusammenfassen
    l1=self.l1.copy()
    i=len(l1)-1
    while i>0: #not duplicate, minus 2. dup: minus dup*2
      if l1.count(l1[i])>1:
        pos=[] #all index position
        for i2 in range(1,len(l1),2):
          if l1[i2]==l1[i]: pos.append(i2)
        l1[pos[0]-1]=sum([l1[i-1] for i in pos]) 
        #vor dem gekürzte Variable
        for i3 in reversed(pos[1:]):
          l1.pop(i3)
          l1.pop(i3-1)
        i-=len(pos)*2-2
      i-=2
    i=len(l1)-2 # Term with factor 0 löschen
    while i>=0:
      if l1[i]==0:
        l1.pop(i+1)
        l1.pop(i)
      i-=2
    return Term(l1)
  def sort1(self):
    l2=[]
    for i in range(1,len(self.l1),2): #find out variables
      l2.append(self.l1[i])
    l2.sort()
    for i in range(len(l2)-1,-1,-1):
      l2.insert(i,self.l1[self.l1.index(l2[i])-1])
    #find 'x' index, -1, return the faktor to l2
    return Term(l2)
  def isv(self):
    if len(self.l1)==2 and self.l1[1] and self.l1[0]==1:
      return self.l1[1] #one variable, factor is 1, return the var
    else: return False
  def is_v(self):
    if len(self.l1)==2 and self.l1[1] and self.l1[0]==-1:
      return self.l1[1]
    else: return False
  def has1v(self): #has a variable with factor 1
    for i in range(0,len(self.l1),2):
      if self.l1[i]==1 and self.l1[i+1]:
        t1=self-Term([1,self.l1[i+1]])
        t1=t1.zus()
        return t1 #return 3y+x+5, return 3y+5
    return False
  def has_1v(self): #has a variable with factor -1
    for i in range(0,len(self.l1),2):
      if self.l1[i]==-1 and self.l1[i+1]:
        t1=self-Term([-1,self.l1[i+1]])
        t1=t1.zus()
        return t1
    return False
  def hasv(self): #has a variable
    l1=[]
    for i in range(1,len(self.l1),2):
      if self.l1[i]: l1+=self.l1[i-1:i+1]
    if l1: return Term(l1)
    else: return False
  def hasz(self):
    if self.l1.count('')>0:
      i1=self.l1.index('')
      return Term(self.l1[i1-1:i1+1])
    else: return False
  def einsetz(self,v,t):
    l1=self.l1.copy()
    if l1.count(v)>0:
      i1=l1.index(v)
      l1[i1]=t
    return Term(l1)
class Glei1():
  def __init__(self,tl,tr): #list on the left/right
    if type(tl)==Term:
      self.tl=tl
      self.tr=tr
    elif type(tl)==str or type(tl)==list:
      self.tl=Term(tl)
      self.tr=Term(tr)
  def str1(self):
    return self.tl.str1()+'='+self.tr.str1()
  def __repr__(self):
    return self.str1()
  def __mul__(self,f1):
    tl1=self.tl*f1
    tr1=self.tr*f1
    return Glei1(tl1,tr1)
  def __sub__(self,t1):
    tl1=self.tl-t1
    tr1=self.tr-t1
    return Glei1(tl1,tr1)
  def __add__(self,other):
    tl=self.tl+other.tl
    tr=self.tr+other.tr
    return Glei1(tl,tr)
  def zus(self):
    tl=self.tl.zus()
    tr=self.tr.zus()
    return Glei1(tl,tr)
  def kla(self):
    tl1=self.tl.kla()
    tr1=self.tr.kla()
    return Glei1(tl1,tr1)
  def vlösen(self,gn): #nach var lösen, gleichung number
    gd=''
    g3=None
    if self.tl.isv() or self.tr.isv():
      stu=1
      gd+=f'{gn} wird eingesetzt\n'
      g3=self*1
    elif self.tl.is_v() or self.tr.is_v():
      stu=2
      gd+=(f'{gn} | *(-1)\n')
      g3=self*(-1)
    elif self.tl.has1v() or self.tr.has1v():
      stu=3
      t1=self.tl.has1v()
      if not t1:
        t1=self.tr.has1v()
      gd+=f'{gn}  | -{t1.str1()}\n'.replace('--','+')
      g3=self-t1
      gd+=g3.str1()+'\n'
      g3=g3.zus()
    elif self.tl.has_1v() or self.tr.has_1v():
      stu=4
      t1=self.tl.has_1v()
      if not t1: t1=self.tr.has_1v()
      gd+=f'{gn}  | -{t1.str1()}\n'.replace('--','+')
      g3=self-t1
      gd+=g3.str1()+'\n'
      g3=g3.zus()
      gd+=g3.str1()+'  | *(-1)\n'
      g3=g3*(-1)
    else: stu=5
    if g3 and stu>1: gd+=g3.str1()+sp+'(3)\n'
    return [stu,g3,gd]
  def einsetz(self,g1):
    if g1.tl.isv(): #which side is variable or Term
      v=g1.tl.l1[1]
      t1=g1.tr
    else:
      v=g1.tr.l1[1]
      t1=g1.tl
    tl=self.tl.einsetz(v,t1)
    tr=self.tr.einsetz(v,t1)
    return Glei1(tl,tr)
  def vzt(self,gn=0): #variable and zahl trennen, gleichung number
    gd=''
    if len(self.tl.l1)==2 and not self.tl.l1[1]:
      self=Glei1(self.tr,self.tl) # left term is only a number
      gd+='Links und Rechts wechseln\n'
    else:
      tz=self.tl.hasz() #term with variable
      if tz:
        gd+=f'{self.str1()}  | -{tz.str1()}\n'.replace('--','+')
        self=self-tz
        gd+=self.str1()+'\n'
        self=self.zus()
      tv=self.tr.hasv() #term with variable
      if tv:
        #gd+='*Die Variable nach links.\n'
        gd+=f'{self.str1()}  | -{tv.str1()}\n'.replace('--','+')
        self=self-tv
        gd+=self.str1()+'\n'
        self=self.zus()
    self.tl=self.tl.sort1()
    if gd: #nothing is needed to write, if nothing was changed
      if gn: gd+=self.str1()+sp+f'({gn})\n'
      else: gd+=self.str1()+'\n'
    return [self,gd]
  def df(self): #durch faktor rechnen
    if self.tl.l1[1]: # var is on the left
      return Glei1(self.tl/self.tl.l1[0],self.tr/self.tl.l1[0])
    else: return Glei1(self.tr/self.tr.l1[0],self.tl/self.tr.l1[0])
  def lösen(self):
    gd=''
    gd+=self.str1()+'\n'
    self=self.kla()
    gd+=self.str1()+'\n'
    g2=self.zus()
    rt1=g2.vzt() #return [gleichung, guide]
    gd+=rt1[1]
    g2=rt1[0].df()
    gd+=g2.str1()+'\n'
    return [g2,gd]

class Glei22():
  def __init__(self,s1,s2):
    if type(s1)==str:
      self.g1=Glei1(*s1.split('='))
      self.g2=Glei1(*s2.split('='))
    elif type(s1)==Glei1:
      self.g1=s1
      self.g2=s2
    self.gd=''
  def lösen(self,ad=False): #only use additionsverfahren
    self.gd+=self.g1.str1()+sp+'(1)\n'
    self.gd+=self.g2.str1()+sp+'(2)\n'
    rt1=self.g1.vlösen('(1)') #nach variable lösen und vergleich
    rt2=self.g2.vlösen('(2)')
    if rt1[0]==rt2[0]==5 or ad:
      g3=self.add1()
    elif rt1[0]<=rt2[0]:
      self.gd+=rt1[2]
      if rt1[0]==1: self.gd+='(1) in (2) einsetzen\n' #direkt einsetzen
      else: self.gd+='(3) in (2) einsetzen\n'
      g3=self.g2.einsetz(rt1[1])
    else:
      self.gd+=rt2[2]
      if rt2[0]==1: self.gd+='(2) in (1) einsetzen\n'
      else: self.gd+='(3) in (1) einsetzen\n'
      g3=self.g1.einsetz(rt2[1])
    lö1=g3.lösen()
    self.gd+=lö1[1]
    #zurück einsetzen
    if rt1[0]==rt2[0]==5 or ad: #gelöst mit einsetzen
      self.gd+='in (1) zurückeinsetzen\n'
      g4=self.g1.einsetz(lö1[0])
    else:
      self.gd+='in (3) zurückeinsetzen\n'
      if rt1[0]<=rt2[0]:
        g4=rt1[1].einsetz(lö1[0])
      else: g4=rt2[1].einsetz(lö1[0])
    lö2=g4.lösen()
    self.gd+=lö2[1]
    return [self.rd(),lö1[0],lö2[0]]
  def rd(self): #remove duplicate
    l1=self.gd.split('\n')
    for i in range(len(l1)-1,0,-1):
      if l1[i]==l1[i-1]: l1.pop(i)
    return '\n'.join(l1)
  def faktor(self): #find out the factor, which will bei multiplied
    x1,y1=self.g1.tl.l1[0],self.g1.tl.l1[2]
    x2,y2=self.g2.tl.l1[0],self.g2.tl.l1[2]
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
      lmx=abs(x1*x2/gdx) #least common multiple
      gdy=gcd(y1,y2)
      lmy=abs(y1*y2/gdy)
      if lmy>lmx>1:
        return x2//gdx,-x1//gdx
        # if x1*x2<0:return x2//gdx,x1//gdx
        # elif x1*x2>0:return -x2//gdx,x1//gdx
      else:
        return y2//gdy,-y1//gdy
        # if y1*y2<0:return y2//gdy,y1//gdy
        # elif y1*y2>0:return -y2//gdy,y1//gdy
  def add1(self):
    rt1=self.g1.vzt(1)
    rt2=self.g2.vzt(2)
    self.gd+=rt1[1]+rt2[1]
    self.g1=rt1[0]
    self.g2=rt2[0]
    f1=self.faktor()
    if f1[0]==f1[1]==1:
      self.gd+=('(1)+(2)\n')
      g3=self.g1+self.g2
    elif f1[0]==1:
      self.gd+=self.g2.str1()+' | * '+str(f1[1])+'\n'
      g2=self.g2*f1[1]
      self.gd+=f'{g2.str1()}'+sp+'(3)\n'
      self.gd+='(1) + (3)\n'
      g3=self.g1+g2
    elif f1[1]==1:
      self.gd+=self.g1.str1()+' | * '+str(f1[0])+'\n'
      g1=self.g1*f1[0]
      self.gd+=f'{g1.str1()}'+sp+'(3)\n'
      self.gd+='(2) + (3)\n'
      g3=g1+self.g2
    else:
      self.gd+='(1) | * '+str(f1[0])+'\n'
      g1=self.g1*f1[0]
      self.gd+=f'{g1.str1()}'+sp+'(3)\n'
      self.gd+='(2) | * '+str(f1[1])+'\n'
      g2=self.g2*f1[1]
      self.gd+=f'{g2.str1()}'+sp+'(4)\n'
      self.gd+='(3) + (4)\n'
      g3=g1+g2
    return g3
class Glei33():
  def __init__(self,s1,s2,s3):
    if type(s1)==str:
      self.g1=Glei1(*s1.split('='))
      self.g2=Glei1(*s2.split('='))
      self.g3=Glei1(*s3.split('='))
    elif type(s1)==Glei1:
      self.g1=s1
      self.g2=s2
      self.g3=s3
    self.gd=''
    self.g=[self.g1,self.g2,self.g3]
  def faktor(self):
    lt=[0,2,4]
    a1=np.zeros((3,3),dtype='int8')
    for i1 in range(3):
      for i2 in range(3):
        a1[i1][i2]=self.g[i2].tl.l1[lt[i1]]
    # x1,y1,z1=self.g1.tl.l1[0],self.g1.tl.l1[2],self.g1.tl.l1[4]
    # x2,y2,z2=self.g2.tl.l1[0],self.g2.tl.l1[2],self.g2.tl.l1[4]
    # x3,y3,z3=self.g3.tl.l1[0],self.g3.tl.l1[2],self.g3.tl.l1[4]
    # a2=np.array([[x1,x2,x3],[y1,y2,y3],[z1,z2,z3]])
    agcd=np.zeros((3,3),dtype='int8')
    f1=np.zeros((3,3,2),dtype='int8')
    #at pos x1, saves factor um x1 und x3 zu löschen
    f2=np.zeros((3,3),dtype='int8')
    #product of 2 factors
    f3=np.zeros((3,3),dtype='int8')
    #at pos x2, saves product of factor, um x1 zu löschen
    #if the product is the least, should use x1,x2 and x1,x3
    #um x1 zu löschen
    for i1 in range(3):
      for i2 in range(3):
        agcd[i1][i2]=gcd(a1[i1][i2],a1[i1][i2-1])
        f1[i1][i2][0]=a1[i1][i2]/agcd[i1][i2]
        f1[i1][i2][1]=a1[i1][i2-1]/agcd[i1][i2]
        f2[i1][i2]=f1[i1][i2][0]*f1[i1][i2][1]
    for i1 in range(3):
      for i2 in range(3):
        f3[i1][i2]=abs(f2[i1][i2-1]*f2[i1][i2])
    pos=np.where(f3==np.amin(f3))
    px,py=pos[0][0],pos[1][0]
    return py,f1[px][py],f1[px][py-1]
  def lösen(self):
    for i in range(3):
      self.gd+=self.g[i].str1()+sp+f'({abc[i]})\n'
    rt=self.faktor()
    i=rt[0]
    ip1=i+1 if i+1<3 else i-2
    il=i-1
    ab='abc'
    g4=self.g[il]*rt[1][0]+self.g[i]*(-rt[1][1])
    g5=self.g[ip1]*rt[2][0]+self.g[il]*(-rt[2][1])
    self.gd+=f'({ab[il]})*({rt[1][0]})+({ab[i]})*({-rt[1][1]})=(1)\n'
    self.gd+=f'({ab[ip1]})*({rt[2][0]})+({ab[il]})*({(-rt[2][1])})=(2)\n'
    # if rt[0]==2:
    #   g4=self.g2*rt[1][0]+self.g3*(-rt[1][1])
    #   g5=self.g1*rt[2][0]+self.g2*(-rt[2][1])
    #   self.gd+=f'(2)*'
    # elif rt[0]==1:
    #   g4=self.g1*rt[1][0]+self.g2*(-rt[1][1])
    #   g5=self.g3*rt[2][0]+self.g1*(-rt[2][1])
    # elif rt[0]==0:
    #   g4=self.g3*rt[1][0]+self.g1*(-rt[1][1])
    #   g5=self.g2*rt[2][0]+self.g3*(-rt[2][1])
    # self.gd+=f'(a)*{f1[0]}+(b)*{f1[1]}\n'
    # self.gd+=f'(a)*{f1[2]}+(c)*{f1[3]}\n'
    # g4=self.g1*f1[0]+self.g2*f1[1]
    # g5=self.g1*f1[2]+self.g3*f1[3]
    g4=g4.zus()
    g5=g5.zus()
    # self.gd+=g4.str1()+sp+'(4)\n'
    # self.gd+=g5.str1()+sp+'(5)\n'
    g22=Glei22(g4,g5)
    rt=g22.lösen(True)
    self.gd+=rt[0]
    g6=self.g1.einsetz(rt[1])
    g7=g6.einsetz(rt[2])
    lö3=g7.lösen()
    self.gd+=lö3[1]
    return self.gd

if __name__=='__main__':
  # g1=Glei1(*'6y+8=-2x'.split('='))
  # g2=Glei1(*'4x-3y=2'.split('='))
  # gg=gen22()
  # ins1=gg.lösen()
  # print(ins1)
  g33_1=gen33()
  ins1=g33_1.lösen()
  print(ins1)