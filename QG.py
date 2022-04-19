import pyperclip
import random
def pm():
  if bool(random.getrandbits(1)): return 1
  else: return -1
def rp(str1): #replace +- and 1x
  str1=str1.replace('+-','-')
  #str1=str1.replace('1x','x')
  str1=str1.replace('√1','1')
  str1=str1.replace('√4','2')
  str1=str1.replace('√9','3')
  return str1
def lb():
  return '\n\n\n\n\n'
def qg1():
  str1=''
  for i in range(12):
    str1+=f'{i+1}²=\n\n'
  return str1
def qg1m():
  str1=''
  for i in range(12):
    str1+=f'({-i-1})²=\n\n'
  return str1
def qg2():
  str1=''
  for i in range(10):
    str1+=f'x²={i*i}\n'
    str1+='x=\n\n'
  return str1
def qg2m():
  str1=''
  for i in range(10):
    str1+=f'x²={-i*i}\n'
    str1+='x=\n\n'
  return str1
def qg3():
  str1=''
  for i in range(10):
    if bool(random.getrandbits(1)):
      strt='x²='+str(random.randint(-10, 10))
    else:
      n1=random.randint(-10, 10)
      if bool(random.getrandbits(1)):
        strt='x²+'+str(n1*n1)+'=0'
      else: strt='x²-'+str(n1*n1)+'=0'
    str1+=str(i+1)+')\t'+strt+lb()
  return str1
def qg40():
  str1=''
  for i in range(10):
    n2=random.randint(-10, 10)
    str1+=str(i+1)+f')\tx(x+{n2})=0{lb()}'
  return str1.replace('+-','-')
def qg41():
  str1=''
  for i in range(10):
    n1,n2=random.randint(-10, 10),random.randint(-10, 10)
    str1+=str(i)+f')\t(x+{n1})(x+{n2})=0{lb()}'
  return str1.replace('+-','-')
def qg42():
  str1=''
  for i in range(10):
    n2=random.randint(-10, 10)
    str1+=str(i+1)+f')\tx²+{n2}x=0{lb()}'
  return rp(str1)
def qg43():
  str1=''
  for i in range(10):
    n2=random.randint(-10, 10)
    n1=random.randint(-10, 10)
    str1+=str(i+1)+f')\t{n1}x²+{n2}x=0{lb()}'
  return rp(str1)
def qg44():
  str1=''
  for i in range(10):
    str1+=f'{i+1})\t'
    if bool(random.getrandbits(1)):
      strt=f'x²={random.randint(-10, 10)}x'
    else:
      n1=random.randint(-10, 10)
      if n1>=0: strt='x²+'+str(n1)+'x=0'
      else: strt='x²'+str(n1)+'x=0'
    if bool(random.getrandbits(1)):
      strt='-'+strt
    str1+=strt
    str1+=lb()
  return rp(str1)
def qg5():
  str1=str2=''
  for i in range(10):
    n1=random.randint(-10, 10)
    n2=random.randint(1, 10)
    if random.randint(0,10)>7:
      n2*=(-1)
    #str1+=f'{i+1})\t(x+{n1})²={n2}{lb()}'
    str1+=f'{i+1})\t(x+{n1})²+{-n2}=0{lb()}'
    if n2<0: str2+=f'{i+1})n.l.\n'
    else: str2+=f'{i+1})x={-n1}±√{n2}\n'
  return rp(str1+str2)
def qg51():
  str1=str2=''
  for i in range(10):
    n1=random.randint(-10, 10)
    n2=random.randint(1, 10)
    if random.randint(0,10)>7:
      n2*=(-1)
    str1+=f'{i+1})\tx²+{2*n1}x+{n1**2}={n2}{lb()}'
    #str1+=f'{i+1})\tx²+{2*n1}x+{n1**2-n2}=0{lb()}'
    if n2<0: str2+=f'{i+1})n.l.\n'
    else: str2+=f'{i+1})x={-n1}±√{n2}\n'
  return rp(str1+str2)
def qg61():
  str1=str2=''
  for i in range(10):
    n1=random.randint(-10, 10) #lösung
    n2=random.randint(-10, 10)
    str1+=f'{i+1})\tx²+{-n1-n2}x+{n1*n2}=0{lb()}'
    #str1+=f'{i+1})\tx²+{2*n1}x+{n1**2-n2}=0{lb()}'
    str2+=f'{i+1})x={n1} oder {n2}\n'
  return rp(str1+str2)
pyperclip.copy(qg61())