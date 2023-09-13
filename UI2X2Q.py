from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import font
import random

class Application():
    def __init__(self, root):
        self.root = root
        self.how=True #how is the file selected
        self.vollName=''
        root.geometry('400x300+300+100') #size and initial position
        root.title('2X2 Gleichungen')
        root.option_add('*Font', '30')
        self.aufgabe=self.lösung=''
        self.abc=list('abcdefghijklmnopqrstuvwxyz')

        self.verfahren=("Gleichsetzung","Einsetzung","Addition")
        self.ver1 = StringVar(root)
        self.ver1.set(self.verfahren[0])
        self.d1=OptionMenu(root, self.ver1, *self.verfahren)
        self.d1.pack()
        self.b1=Button(root,text='Generate',command=self.generate)
        self.b1.pack()
        self.b2=Button(root,text='Save',command=self.save)
        self.b2.pack()
        self.scr1 = Scrollbar(root)
        self.scr1.pack(side="right", fill="y")
        self.t1 = Text(root, yscrollcommand=self.scr1.set)
        self.t1.pack(side="left", fill="both")
        self.scr1.config(command=self.t1.yview)
    def pm(self): #random +1 oder -1
        return 1 if random.getrandbits(1) else -1
    def r19(self): # generate random number 1-9, the chance to generate smaller number is bigger
        numbers=list(range(1,8))
        chance1 = [x+4 for x in numbers]
        chance1.reverse()
        a=random.choices(numbers, weights=chance1,k=30)
        a=[x*self.pm() for x in a]
        return a # Normally you would generate only one random number once, it is written like this only because in the next function 'gleichung', it is shorter to write
    def lr(self, str1): # switch left and right
        lr1=str1.split('=')
        str2=lr1[1]+'='+lr1[0]
        return str2
    def gleichung(self, type1='Gleichsetzung'):
        r1=self.r19() #a1x+b1y=c1
        x1, y1=r1.pop(), r1.pop()
        a1=[r1.pop(),r1.pop()]
        if type1=='Gleichsetzung': b1=[1,1]#[pm(),pm()]
        elif type1=='Einsetzung': b1=[r1.pop(),1]
        else: b1=[r1.pop(),r1.pop()]
        c1, g1=[],[]
        for i1 in range(2):
            r2=1#random.randint(1,3) # if the equation zuerst umgestellt werden muss
            if r2==1:
                c1.append(a1[i1]*x1+b1[i1]*y1)
                g1.append(str(a1[i1])+'x+'+str(b1[i1])+'y='+str(c1[i1]))
            elif r2==2:
                c1.append(b1[i1]*y1-a1[i1]*x1)
                g1.append(str(a1[i1])+'x+'+str(c1[i1])+'='+str(b1[i1])+'y')
            else:
                c1.append(a1[i1]*x1-b1[i1]*y1)
                g1.append(str(b1[i1])+'y+'+str(c1[i1])+'='+str(a1[i1])+'x')
            for i1 in range(len(g1)):
                if bool(random.getrandbits(1)) and type1!='Addition':
                    g1[i1]=self.lr(g1[i1]) # switch left and right side of the equation
                g1[i1]=g1[i1].replace('+-','-').replace('1x','x').replace('1(','(').replace('1y','y')
            l1='x='+str(x1)+', y='+str(y1)
        return(g1,l1)
    def generate(self):
        self.t1.delete("1.0","end")
        self.aufgabe=self.lösung=''
        for i1 in range(10):
            g1,l1=self.gleichung(self.ver1.get())
            self.aufgabe+=self.abc[i1]+') '+g1[0]+'\n   '+g1[1]+'\n\n'
            self.lösung+=self.abc[i1]+') '+l1+'\n'
        self.t1.insert('end', self.aufgabe)
        self.t1.insert('end', self.lösung)
        #print(self.aufgabe,self.lösung)
    def save(self):
        style = ttk.Style(self.root)
        default_font2 = font.nametofont("TkIconFont")
        default_font2.configure(size=16)
        self.vollName=fd.asksaveasfilename(
            filetypes=(
                ("Text files", "*.txt"),
                ("Prolog files", "*.pl *.pro"),
                ("All files", "*.*"),))
        try:
            with open(self.vollName, "w") as f:
                f.write(self.aufgabe+self.lösung)
        except FileNotFoundError: pass
        except TypeError: pass
if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
#improvement: change the number of Gleichungen with input