from f_Vektor import Vec, pol2cart
import pygame as pg
import math

pg.font.init()
font1 = pg.font.SysFont("comicsansms", 20)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

class geo():
  def __init__(self,screen, bottom, length):
    self.screen=screen
    self.bottom=bottom
    self.length=length
    self.resolution = Vec(length,length)
    self.tshift=Vec(5,5) #text gap
    self.ePunkte=[] #save point on the ellipse
    self.rpunkt=bottom//6 #radius of a point
  def dist(self,v1,v2):
    return ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)**(1/2)
  def strecke(self,v1,v2):
    pg.draw.line(self.screen, (255,255,0), v1,v2)
  def gerade(self,v1,v2):
    x1,y1,x2,y2=v1[0],v1[1],v2[0],v2[1]
    if int(x1)==int(x2):
      pg.draw.line(self.screen, (255,255,0), Vec(x1,0), Vec(x1,self.length))
    else:
      steig=(y2-y1)/(x2-x1)
      pg.draw.line(self.screen,(255,255,0),Vec(0,y1-steig*x1),Vec(self.length,steig*(self.length-x1)+y1))
  def mittelsenkrecht(self,v1,v2):
    x1,y1,x2,y2=v1[0],v1[1],v2[0],v2[1]
    if int(x1)==int(x2):
      return Vec(0,y1/2+y2/2), Vec(self.length,y1/2+y2/2)
    elif int(y1)==int(y2):
      return Vec(x1/2+x2/2,0), Vec(x1/2+x2/2,self.length)
    else:
      xm,ym=x1/2+x2/2,y1/2+y2/2
      steig=(x1-x2)/(y2-y1)
    return Vec(0,ym-steig*xm), Vec(self.length,steig*(self.length-xm)+ym)
  def schnitt(self,v1,v2,v3,v4):
    x1,y1,x2,y2=v1[0],v1[1],v2[0],v2[1]
    x3,y3,x4,y4=v3[0],v3[1],v4[0],v4[1]
    xs=((x4-x3)*(x2*y1-x1*y2)-(x2-x1)*(x4*y3-x3*y4))/((y4-y3)*(x2-x1)-(y2-y1)*(x4-x3))
    ys=((y1-y2)*(x4*y3-x3*y4)-(y3-y4)*(x2*y1-x1*y2))/((y4-y3)*(x2-x1)-(y2-y1)*(x4-x3))
    return Vec(xs,ys)
class ellipse(geo):
  def __init__(self,screen, bottom, length):
    super().__init__(screen, bottom, length)
    self.f2 = self.resolution / 2 #f2 is the center
    self.radius = min(self.resolution * 0.4) #radius of the big circle
    self.f1=self.f2-Vec(self.radius*0.5,0)
    self.nSegment=36
    self.rotateAngle=0
    self.step1=-1 #so that at start nothing is displayed
    self.roPoint = pol2cart(self.radius, math.pi) + self.f2
    self.ms=Vec(0,0) #mittel senkrecht
    self.guide=[
      'Einen beliebigen Punkt E auf dem Kreislinie festlegen',#step 0
      'Die Strecke EF1 ziehen', #1
      'Die Strecke EF2 ziehen', #2
      'Ein Kreis um E mit r=EF2 ziehen',#3
      'Ein Kreis um F2 mit r=EF2 ziehen',#4
      'Die 2 Kreisen schneiden sich auf 2 Punkte',
      'Eine Gerade durch die 2 Schnittpunkte ziehen (Mittelsenkrechte)',
      'schneidet die Strecke EF2 auf S',
      'Diese Vorfahren wiederholen']
  def forward(self):
    if self.step1>6:
      self.step1=-1
      self.rotateAngle += math.pi/self.nSegment*2
      self.roPoint = pol2cart(self.radius, self.rotateAngle+math.pi) + self.f2
    else:
      self.step1+=1
  def backward(self):
    if self.step1<0 and self.rotateAngle>0:
      self.step1=7
      self.rotateAngle -= math.pi/self.nSegment*2
      self.roPoint = pol2cart(self.radius, self.rotateAngle+math.pi) + self.f2
    else:
      self.step1-=1
      if self.step1==6:
        self.ePunkte.pop()
  def draw(self):
    pg.draw.circle(self.screen,pg.Color("darkseagreen4"), self.f2, self.radius, 3)
    pg.draw.circle(self.screen,pg.Color("white"), self.f2, self.rpunkt) #f2
    self.screen.blit(font1.render('F2',True,ORANGE),self.f2+self.tshift)
    pg.draw.circle(self.screen,pg.Color("white"), self.f1, self.rpunkt) #f1
    self.screen.blit(font1.render('F1',True,ORANGE),self.f1+self.tshift)
    if self.ePunkte:
      for p in self.ePunkte:
        pg.draw.circle(self.screen,pg.Color("red"), p, self.rpunkt)
    if self.step1>-1:
      pg.draw.circle(
        self.screen,pg.Color("darkseagreen4"), self.roPoint, self.rpunkt)
      self.screen.blit(font1.render('E',True,ORANGE),self.roPoint+self.tshift)
    if self.step1>0:
      self.strecke(self.roPoint,self.f1)
    if self.step1>1:
      self.strecke(self.roPoint,self.f2)
    self.r1=self.dist(self.roPoint,self.f1)
    if self.step1>2:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.roPoint,self.r1,2)
    if self.step1>3:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.f1,self.r1,2)
    if self.step1>4:
      self.cs1=self.roPoint.rotate2D(self.f1,math.pi/3)  #circle schnittpunkt
      pg.draw.circle(self.screen,pg.Color("blue"), self.cs1, self.rpunkt)
      self.cs1=self.roPoint.rotate2D(self.f1,-math.pi/3)
      pg.draw.circle(self.screen,pg.Color("blue"), self.cs1, self.rpunkt)
    if self.step1>5:
      self.ms=self.mittelsenkrecht(self.roPoint,self.f1)
      self.strecke(self.ms[0],self.ms[1])
    if self.step1>6:
      epunkt=self.schnitt(self.ms[0],self.ms[1],self.roPoint,self.f2)
      if len(self.ePunkte)<1:
        self.ePunkte.append(epunkt)
      elif self.ePunkte[-1]!=epunkt:
        self.ePunkte.append(epunkt)
        pg.draw.circle(self.screen,pg.Color("red"), epunkt, self.rpunkt)
      self.screen.blit(font1.render('S',True,ORANGE),epunkt+self.tshift)
    if self.step1>-1 or self.rotateAngle!=0: 
        #the text is only at the start not displayed 
      self.screen.blit(font1.render(
        self.guide[self.step1],True,ORANGE),(self.bottom/2,self.length-self.bottom))
    pg.display.flip()
      #pg.image.save(self.screen,dir1+name1+str(nameIndex)+'.png')
      #nameIndex+=1
class hyperbel(geo):
  def __init__(self,screen, bottom, length):
    super().__init__(screen, bottom, length)
    self.f2 = self.resolution / 2 #f2 is the center
    self.radius = min(self.resolution * 0.15) #radius of the big circle
    self.f1=Vec(length*0.25,length*0.5)
    self.nSegment=36
    self.rotateAngle=[0]
    self.rotateAngleMinus=[]
    self.rai=0 #rotate angle index
    for n1 in range(1,self.nSegment):
      w1=2*math.pi/self.nSegment*n1
      kw=math.acos(self.radius/(self.f2[0]-self.f1[0])) #critical angle
      if w1<kw:
        self.rotateAngle.append(w1)
        self.rotateAngleMinus.append(-w1)
      else:
        break
    self.rotateAngle.extend(self.rotateAngleMinus)
    del(self.rotateAngleMinus)
    self.step1=-1 #so that at start nothing is displayed
    self.roPoint = pol2cart(self.radius, 0) + self.f1
    self.ms=Vec(0,0) #mittel senkrecht
    self.guide=[
      'Einen beliebigen Punkt E auf dem Kreislinie festlegen',#step 0
      'Die Gerade EF1 ziehen', #1
      'Die Strecke EF2 ziehen', #2
      'Ein Kreis um E mit r=EF2 ziehen',#3
      'Ein Kreis um F2 mit r=EF2 ziehen',#4
      'Die 2 Kreisen schneiden sich auf 2 Punkte',
      'Eine Gerade durch die 2 Schnittpunkte ziehen (Mittelsenkrechte)',
      'schneidet die Gerade EF1 auf S',
      'Diese Vorfahren wiederholen']
  def forward(self):
    if self.step1>6:
      self.step1=-1
      if self.rai<len(self.rotateAngle)-1:
        self.rai+=1
      self.roPoint=pol2cart(self.radius,self.rotateAngle[self.rai])+self.f1
    else:
      self.step1+=1
  def backward(self):
    if self.step1<0:
      self.step1=7
      if self.rai>0:
        self.rai-=1
      self.roPoint=pol2cart(self.radius,self.rotateAngle[self.rai])+self.f1
    else:
      self.step1-=1
      if self.step1==6:
        self.ePunkte.pop()
  def draw(self):
    pg.draw.circle(self.screen,pg.Color("darkseagreen4"), self.f1, self.radius, 3)
    pg.draw.circle(self.screen,pg.Color("white"), self.f2, self.rpunkt) #f2
    self.screen.blit(font1.render('F2',True,ORANGE),self.f2+self.tshift)
    pg.draw.circle(self.screen,pg.Color("white"), self.f1, self.rpunkt) #f1
    self.screen.blit(font1.render('F1',True,ORANGE),self.f1+self.tshift)
    if self.ePunkte:
      for p in self.ePunkte:
        pg.draw.circle(self.screen,pg.Color("red"), p, self.rpunkt)
    if self.step1>-1:
      pg.draw.circle(
        self.screen,pg.Color("darkseagreen4"), self.roPoint, self.rpunkt)
      self.screen.blit(font1.render('E',True,ORANGE),self.roPoint+self.tshift)
    if self.step1>0:
      self.gerade(self.roPoint,self.f1)
    if self.step1>1:
      self.strecke(self.roPoint,self.f2)
    r1=self.dist(self.roPoint,self.f2)
    if self.step1>2:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.roPoint,r1,2)
    if self.step1>3:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.f2,r1,2)
    if self.step1>4:
      self.cs1=self.roPoint.rotate2D(self.f2,math.pi/3)  #circle schnittpunkt
      pg.draw.circle(self.screen,pg.Color("blue"), self.cs1, self.rpunkt)
      self.cs1=self.roPoint.rotate2D(self.f2,-math.pi/3)
      pg.draw.circle(self.screen,pg.Color("blue"), self.cs1, self.rpunkt)
    if self.step1>5:
      self.ms=self.mittelsenkrecht(self.roPoint,self.f2)
      self.strecke(self.ms[0],self.ms[1])
    if self.step1>6:
      epunkt=self.schnitt(self.ms[0],self.ms[1],self.roPoint,self.f1)
      if len(self.ePunkte)<1:
        self.ePunkte.append(epunkt)
      elif self.ePunkte[-1]!=epunkt:
        self.ePunkte.append(epunkt)
        pg.draw.circle(self.screen,pg.Color("red"), epunkt, self.rpunkt)
      self.screen.blit(font1.render('S',True,ORANGE),epunkt+self.tshift)
    if self.step1>-1 or self.rai!=0: 
        #the text is only at the start not displayed 
      self.screen.blit(font1.render(
        self.guide[self.step1],True,ORANGE),(self.bottom/2,self.length-self.bottom))
    pg.display.flip()
class parabel(geo):
  def __init__(self,screen, bottom, length):
    super().__init__(screen, bottom, length)
    self.f1=Vec(length*0.4,length*0.5)
    self.l=length*0.2
    self.strecke(Vec(self.l,0),Vec(self.l,length))
    self.nSegment=6 #how many pieces divided to
    self.i1=0 #index of moving point
    self.d=length/2/self.nSegment #distance between each two selected point
    self.d1=[0]
    self.d1Minus=[]
    for n1 in range(1,self.nSegment):
      self.d1.append(length/2/self.nSegment*n1)
      self.d1Minus.append(-length/2/self.nSegment*n1)
    self.d1.extend(self.d1Minus)
    del(self.d1Minus)
    self.d1=[n1+length/2 for n1 in self.d1]
    self.step1=-1 #so that at start nothing is displayed
    self.roPoint=Vec(self.l,self.d1[self.i1])
    self.guide=['Einen beliebigen Punkt B auf l festlegen',
    'Ein Kreis um B mit r ziehen',
    'Es schneidet die Gerade auf B1 und B2',
    'Ein Kreis um B1 mit 2r ziehen',
    'Ein Kreis um B2 mit 2r ziehen',
    'Die zwei Kreisen schneiden sich auf 2 Punkte',
    'Eine Gerade durch die 2 Punkte ziehen (Eine Senkrechte durch B)',
    'Die Strecke BF ziehen',
    'Ein Kreis um B mit r=BF ziehen',
    'Ein Kreis um F mit r=BF ziehen',
    'Die zwei Kreisen schneiden sich auf 2 Punkte',
    'Eine Gerade durch die 2 Punkte ziehen (Mittelsenkrecht von BF)',
    'Die Mittelsenkrechte und die Senkrechte schneiden sich auf S (gesucht)']
  def forward(self):
    if self.step1>len(self.guide)-2:
      self.step1=-1
      if self.i1<len(self.d1)-1:
        self.i1+=1
      self.roPoint=Vec(self.l,self.d1[self.i1])
    else:
      self.step1+=1
  def backward(self):
    if self.step1<0:
      self.step1=len(self.guide)-1
      if self.i1>0:
        self.i1-=1
      self.roPoint=Vec(self.l,self.d1[self.i1])
    else:
      self.step1-=1
      if self.step1==len(self.guide)-2:
        self.ePunkte.pop()
  def draw(self):
    pg.draw.circle(self.screen,pg.Color("white"), self.f1, self.rpunkt) #f1
    self.screen.blit(font1.render('F',True,ORANGE),self.f1+self.tshift)
    self.strecke(Vec(self.l,0),Vec(self.l,self.length))
    if self.ePunkte:
      for p in self.ePunkte:
        pg.draw.circle(self.screen,pg.Color("red"), p, self.rpunkt)
    if self.step1>-1:
      pg.draw.circle(
        self.screen,pg.Color("darkseagreen4"), self.roPoint, self.rpunkt)
      self.screen.blit(font1.render('E',True,ORANGE),self.roPoint+self.tshift)
    roUp=self.roPoint-Vec(0,self.d)
    roDown=self.roPoint+Vec(0,self.d)
    roL=self.roPoint-Vec(self.d*3**(1/2),0)
    roR=self.roPoint+Vec(self.d*3**(1/2),0)
    if self.step1<7:
      if self.step1>0:
        pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.roPoint,self.d,2)
      if self.step1>1:
        pg.draw.circle(self.screen,pg.Color("blue"),roUp,self.rpunkt)
        pg.draw.circle(self.screen,pg.Color("blue"),roDown,self.rpunkt)
      if self.step1>2:
        pg.draw.circle(self.screen,pg.Color("darkseagreen4"),roUp,2*self.d,2)
      if self.step1>3:
        pg.draw.circle(self.screen,pg.Color("darkseagreen4"),roDown,2*self.d,2)
      if self.step1>4:
        pg.draw.circle(self.screen,pg.Color("blue"),roL,self.rpunkt)
        pg.draw.circle(self.screen,pg.Color("blue"),roR,self.rpunkt)
    if self.step1>5:
      self.gerade(roL,roR) #horizontal line
    if self.step1>6:
      self.strecke(self.roPoint,self.f1)
    r1=self.dist(self.roPoint,self.f1)
    if self.step1>7:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.roPoint,r1,2)
    if self.step1>8:
      pg.draw.circle(self.screen,pg.Color("darkseagreen4"),self.f1,r1,2)
    if self.step1>9:
      cs1=self.roPoint.rotate2D(self.f1,math.pi/3)  #circle schnittpunkt
      pg.draw.circle(self.screen,pg.Color("blue"),cs1, self.rpunkt)
      cs2=self.roPoint.rotate2D(self.f1,-math.pi/3)
      pg.draw.circle(self.screen,pg.Color("blue"),cs2, self.rpunkt)
    if self.step1>10:
      self.gerade(cs1,cs2) #mittelsenkrecht
    if self.step1>11:
      epunkt=self.schnitt(cs1,cs2,roL,roR)
      if len(self.ePunkte)<1:
        self.ePunkte.append(epunkt)
      elif self.ePunkte[-1]!=epunkt:
        self.ePunkte.append(epunkt)
        pg.draw.circle(self.screen,pg.Color("red"), epunkt, self.rpunkt)
      self.screen.blit(font1.render('S',True,ORANGE),epunkt+self.tshift)
    if self.step1>-1 or self.i1!=0: 
        #the text is only at the start not displayed 
      self.screen.blit(font1.render(
        self.guide[self.step1],True,ORANGE),(self.bottom/2,self.length-self.bottom))
    pg.display.flip()
      #pg.image.save(self.screen,dir1+name1+str(nameIndex)+'.png')
      #nameIndex+=1