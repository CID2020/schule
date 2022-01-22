from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt #Alignment
import sys
import matplotlib.pyplot as plt
import numpy as np
def doof(a,b,c):
    if a==1:
        astr='x²'
    else:
        astr=str(a)+'x²'
    if b==1:
        bstr='+x'
    elif b==0:
        bstr=''
    elif b>0:
        bstr='+'+str(b)+'x'
    else:
        bstr=str(b)+'x'
    if c==0:
        cstr=''
    elif c>0:
        cstr='+'+str(c)
    else:
        cstr=str(c)
    return 'y='+astr+bstr+cstr
def plot1(a,b,c,von,bis,punkte,checked1):
    fig=plt.figure(figsize=(16, 12))
    ax = plt.subplot()
    ax.tick_params(which='major', width=3, length=20, labelsize=24,pad=15,
                direction='in')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(4)
    if checked1:
        plt.gca().set_aspect('equal', adjustable='box')
    plt.ylabel('y',fontsize=26,fontweight='bold',labelpad=10)#
    plt.xlabel('x',fontsize=26,fontweight='bold',labelpad=10)
    x=np.linspace(von,bis,punkte)
    y=a*x**2+b*x+c
    if min(y)>=0 and a>0:
        ax.set_ylim(0, max(y))
    if max(y)<=0 and a<0:
        ax.set_ylim(min(y), 0)
    ax.axhline(linewidth=4, color="k")
    lines=plt.plot(x, y,'k',linewidth=3)
    plt.show()
a,b,c=1,0,0
mittel=-b/a/2
von=round(mittel)-5
bis=round(mittel)+5
punkte=100
funktion0=doof(a,b,c)

class QLabelBuddy(QDialog) :
    def __init__(self):
        super().__init__()
        self.initLO0()
    def initLoTop(self):
        lGleichung = QLabel('y=ax²+bx+c')
        self.fLineEdit = QLineEdit(self)
        self.fLineEdit.setText(funktion0)
        loTop=QHBoxLayout()
        loTop.addWidget(lGleichung)
        loTop.addWidget(self.fLineEdit)
        loTop.setSpacing(100)
        return loTop

    def initLoML(self):
        loL=QVBoxLayout()
        lPara=QLabel('Parameters:',self)
        loL.addWidget(lPara)
        loPara=QFormLayout()
        self.aLineEdit = QLineEdit(self)
        self.aLineEdit.setText(str(a))
        loPara.addRow('a',self.aLineEdit)
        self.bLineEdit = QLineEdit(self)
        self.bLineEdit.setText(str(b))
        loPara.addRow('b',self.bLineEdit)
        self.cLineEdit = QLineEdit(self)
        self.cLineEdit.setText(str(c))
        loPara.addRow('c',self.cLineEdit)
        loL.addLayout(loPara)
        lZeichnung=QLabel('Zeichnung:')
        loL.addWidget(lZeichnung)
        loZeichnung=QFormLayout()
        self.leVon = QLineEdit(self)
        self.leVon.setText(str(von))
        loZeichnung.addRow('Von',self.leVon)
        self.leBis = QLineEdit(self)
        self.leBis.setText(str(bis))
        loZeichnung.addRow('Bis',self.leBis)
        self.lePunkt = QLineEdit(self)
        self.lePunkt.setText(str(punkte))
        loZeichnung.addRow('Punkte',self.lePunkt)
        loL.addLayout(loZeichnung)
        loL.setAlignment(Qt.AlignTop)
        loL.setSpacing(20)
        return loL
    def initLoMR(self):
        loMR=QVBoxLayout()
        lScheitel=QLabel('Scheitelpunkt:',self)
        loMR.addWidget(lScheitel)
        loScheitel=QFormLayout()
        self.leX0 = QLineEdit(self)
        loScheitel.addRow('x0',self.leX0)
        self.leY0 = QLineEdit(self)
        loScheitel.addRow('y0',self.leY0)
        loMR.addLayout(loScheitel)
        lNullstelle=QLabel('Nullstelle:',self)
        loMR.addWidget(lNullstelle)
        loNull=QFormLayout()
        self.leX1 = QLineEdit(self)
        loNull.addRow('x1',self.leX1)
        self.leX2 = QLineEdit(self)
        loNull.addRow('x2',self.leX2)
        loMR.addLayout(loNull)
        self.checkxy=QCheckBox("Zeichne x und y mit gleicher Skala",self)
        loMR.addWidget(self.checkxy)
        loMR.setAlignment(Qt.AlignTop)
        loMR.setSpacing(20)
        return loMR

    def initLoM(self): 
        loMid=QHBoxLayout()
        loMid.addLayout(self.initLoML())
        loMid.addLayout(self.initLoMR())
        loMid.setSpacing(20)
        return loMid
        
    def initLoDown(self):
        loD=QHBoxLayout()
        self.btBereit = QPushButton('&Bereit')
        self.btDruck = QPushButton('&Druck')
        loD.addWidget(self.btBereit)
        loD.addWidget(self.btDruck)
        loD.setSpacing(20)
        return loD

    def initLO0(self):
        self.setWindowTitle('Quadratische Gleichung')
        #self.setGeometry(50,50,500,500)
        lo0=QVBoxLayout()
        lo0.addLayout(self.initLoTop())
        lo0.addLayout(self.initLoM())
        lo0.addLayout(self.initLoDown())
        lo0.setSpacing(20)
        self.setLayout(lo0)
        self.btBereit.clicked.connect(self.bereit)
        self.btDruck.clicked.connect(self.druck)
    def bereit(self):
        bereitFlag=True
        try:
            a=int(self.aLineEdit.text())
            b=int(self.bLineEdit.text())
            c=int(self.cLineEdit.text())
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Fehler")
            msg.setText("Bitte eine ganze Zahl für a,b,c eingeben")
            x = msg.exec_()  # this will show our messagebo
            bereitFlag=False
        try:
            1/a
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setWindowTitle("Fehler")
            msg.setText("a darf nicht gleich 0 sein")
            x = msg.exec_()  # this will show our messagebo
            bereitFlag=False
        if bereitFlag:
            x0=round(-b/a/2*1000)/1000
            von=x0-5
            bis=x0+5
            y0=round((a*x0*x0+b*x0+c)*1000)/1000
            self.fLineEdit.setText(doof(a,b,c))
            self.leVon.setText(str(von))
            self.leBis.setText(str(bis))
            self.lePunkt.setText(str(punkte))
            self.leX0.setText(str(x0))
            self.leY0.setText(str(y0))
            if b*b>4*a*c:
                x1=(-b+(b*b-4*a*c)**(1/2))/2/a
                x1=round(x1*1000)/1000
                x2=(-b-(b*b-4*a*c)**(1/2))/2/a
                x2=round(x2*1000)/1000
                self.leX1.setText(str(x1))
                self.leX2.setText(str(x2))
            elif b*b==4*a*c:
                self.leX1.setText(str(x0))
                self.leX2.setText('X')
            else:
                self.leX1.setText('X')
                self.leX2.setText('X')
    def druck(self):
        druckFlag=True
        try:
            a=int(self.aLineEdit.text())
            b=int(self.bLineEdit.text())
            c=int(self.cLineEdit.text())
            von=float(self.leVon.text())
            bis=float(self.leBis.text())
            punkte=int(self.lePunkt.text())
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Fehler")
            msg.setText("Bitte eine ganze Zahl für a,b,c,punkte eingeben")
            x = msg.exec_()  # this will show our messagebo
            druckFlag=False
        if druckFlag:
            plot1(a,b,c,von,bis,punkte,self.checkxy.isChecked())

if __name__ == '__main__':
    font1 = QFont('Times', 18)
    app = QApplication(sys.argv)
    app.setFont(font1)
    app.setStyleSheet("QLabel{font-size: 18pt;}""QCheckBox{font-size: 16pt;}"
    "QPushButton{font-size: 18pt;}""QLineEdit{font-size: 18pt;}")
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())