import numpy as np
def gcd(a, b):
  if b == 0:return a
  return gcd(b, a % b)
a0=[[4,5,8], [2, 8, 5], [7, 1, 3]]
a1=np.array(a0)
#np.random.randint(1,9 ,size=(3,3))
agcd=np.zeros((3,3),dtype='int8')
f1=np.zeros((3,3,2),dtype='int8')
f2=np.zeros((3,3))
f3=np.zeros((3,3))
for i1 in range(3):
  for i2 in range(3):
    agcd[i1][i2]=gcd(a1[i1][i2],a1[i1][i2-1])
    f1[i1][i2][0]=a1[i1][i2]/agcd[i1][i2]
    f1[i1][i2][1]=a1[i1][i2-1]/agcd[i1][i2]
    f2[i1][i2]=f1[i1][i2][0]*f1[i1][i2][1]
for i1 in range(3):
  for i2 in range(3):
    f3[i1][i2]=f2[i1][i2-1]*f2[i1][i2]
    #f1[i1][i2-1]=alm[i1][i2]*alm[i1][i2-1]
    #in f[3] saves lm 1-3 and 2-3
print(a1)
print(f1)
print(f3)
pos=np.where(f3==np.amin(f3))
px,py=pos[0][0],pos[1][0]
print([px,py])
print(f1[px][py])
print(f1[px][py-1])