#import os
import sys
import pygame as pg
from pygame.locals import * #for rect
from pygame_button import Button
from f_Vektor import Vec, pol2cart
from f_kegel import *
from f_para import *
#os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()


class Controller(): #object?
  def __init__(self):
    self.resolution = Vec(length,length)
    self.screen = pg.display.set_mode(self.resolution+Vec(0,bottom))
    #self.screen_rect = self.screen.get_rect()
    self.bw=2*bottom #button width
    self.bh=bottom #button height
    self.gap=bottom/2 #gap between buttons
    self.clock = pg.time.Clock()
    self.stage=1 #1 Start, 2 Ellipse Drawing

    self.play=False #auto play
    self.done = False
    self.zeit1=1
    self.bChoose1 = Button((0,0,self.bw,self.bh),RED,self.goToStage2e,text='Ellipse',**BUTTON_STYLE)
    self.bChoose1.rect.center = (length/2, 100)
    self.bChoose2 = Button(
      (0,0,self.bw,self.bh),RED,self.goToStage2h,text='Hyperbel',**BUTTON_STYLE)
    self.bChoose2.rect.center = (length/2-2*self.bw, 100)
    self.bChoose3 = Button(
      (0,0,self.bw,self.bh),RED,self.goToStage2p,text='Parabel',**BUTTON_STYLE)
    self.bChoose3.rect.center = (length/2+2*self.bw, 100)
    self.bBack = Button((0,length,self.bw,self.bh),
      BLUE,self.goToStage1,text='Back',**BUTTON_STYLE)
    self.bPlay = Button((length/2+self.gap/2,length,self.bw,self.bh),
      BLUE,self.start,text='Play',**BUTTON_STYLE)
    self.bStop = Button(
      (length/2-self.bw-self.gap/2,length,self.bw,self.bh),
      BLUE,self.start,text='Pause',**BUTTON_STYLE)
    self.bForward = Button(
      (length/2+self.bw+self.gap*3/2,length,self.bw,self.bh),
      BLUE,self.forward,text='Forward',**BUTTON_STYLE)
    self.bBackward = Button(
      (length/2-2*self.bw-self.gap*3/2,length,self.bw,self.bh),
      BLUE,self.backward,text='Backward',**BUTTON_STYLE)
  def goToStage2e(self):
    self.stage=2
    self.kegel1=ellipse(self.screen, bottom, length)
  def goToStage2h(self):
    self.stage=2
    self.kegel1=hyperbel(self.screen, bottom, length)
  def goToStage2p(self):
    self.stage=2
    self.kegel1=parabel(self.screen, bottom, length)
  def goToStage1(self):
    self.stage=1
    del self.kegel1
  def start(self):
    if self.play:
      self.play=False
    else:
      self.play=True
  def forward(self):
    self.kegel1.forward()
  def backward(self):
    self.kegel1.backward()
  def event_loop(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.done = True
      if self.stage==1:
        self.bChoose1.check_event(event)
        self.bChoose2.check_event(event)
        self.bChoose3.check_event(event)
      if self.stage==2:
        self.bBack.check_event(event)
        self.bPlay.check_event(event)
        self.bStop.check_event(event)
        self.bForward.check_event(event)
        self.bBackward.check_event(event)
      keys =pg.key.get_pressed()
      if keys[pg.K_RIGHT]:
        self.forward()
      if keys[pg.K_LEFT]:
        self.backward()
      if keys[pg.K_SPACE]:
        self.start()
  def main_loop(self):
    while not self.done:
      self.screen.fill(BLACK)
      self.event_loop()
      if self.stage==1:
        self.bChoose1.update(self.screen)
        self.bChoose2.update(self.screen)
        self.bChoose3.update(self.screen)
      if self.stage==2:
        self.bBack.update(self.screen)
        self.bPlay.update(self.screen)
        self.bStop.update(self.screen)
        self.bForward.update(self.screen)
        self.bBackward.update(self.screen)
        self.kegel1.draw()
        #orient with center instead of upleft corner
      pg.display.update()
      if self.play:
        self.forward()
        self.clock.tick(self.zeit1)
        
if __name__ == "__main__":
  d1 = Controller()
  d1.main_loop()
  pg.quit()
  sys.exit()