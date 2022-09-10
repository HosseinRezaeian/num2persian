
from ast import Num
from operator import index


h=input('enter:')
num=list(str(h))
is_mom=False
for i in num:
    if i =='.':
        is_mom=True

if is_mom ==True:
    num[num.index('.'):len(num)]=[]
print(num)
print('t3')
print(int(len(num)/3))
num1=num[0:len(num)%3]
print('num1')
print(num1)
ref=len(num)
li=len(num)-3
for t3 in range(0,int(len(num)/3)):
    print('this lid')
    lid=num[li:ref]
    print(lid)
    ref=ref-3
    li=li-3
    


