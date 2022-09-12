


def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)


zero=False

numtoper1=['','یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه']
numtoper10=['ده','یازده','دوازده','سیزده','چهارده','پانزده','شانزده','هیفده','هیجده','نوزده',]
numtoper90=['بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود']
numtoper100=['صد','دویست','سیصد','چهارصد','پانصد','ششصد','هفتصد','هشتصد','نهصد']
bignum_name=['هزار','ملیون','ملیارد','بیلیون','بیلیارد','تریلیون','تریلیارد']

def lower_t_100(num1):
    global zero
    if num1==0:
        zero=True
        return ''
    
    elif 10>num1>0:
        return numtoper1[num1]
    elif 20>num1>9:
        return numtoper10[num1-10]
    elif 100>num1>19:
        null_zero=list(str(num1))
        null_zero=[int(x) for x in null_zero]
        if null_zero[0]>1 and null_zero[1]>0:
            dahgan=numtoper90[null_zero[0]-2]
            yekan=numtoper1[null_zero[1]]
            return ("{} و {}".format(dahgan,yekan))
        elif null_zero[0]>1 and null_zero[1]==0:
            dahgan=numtoper90[null_zero[0]-2]
            return ("{}".format(dahgan))
    
def biger_t_99(numtoper):
    global zero
    if numtoper==0:
        zero=True
        return ''
    elif 10>numtoper>0:
        return numtoper100[numtoper-1]




def finall(num):
    null_zero=list(str(num))
    null_zero=[int(x) for x in null_zero]
    
    if len(null_zero)<3:
        return lower_t_100(num)
    elif null_zero[0]>0 and null_zero[1]==0 and null_zero[2]==0:
        return numtoper100[null_zero[0]-1]

    elif len(null_zero)>2:
        
        sadgan=biger_t_99(null_zero[0])
        del null_zero[0]
        low=lower_t_100(convert(null_zero))
        return ("{} و {}".format(sadgan,low))
    

def get_first(numer):

    num=list(str(numer))
    is_mom=False
    for i in num:
        if i =='.':
            is_mom=True

    if is_mom ==True:
        num[num.index('.'):len(num)]=[]
    aller=[]
    reverall=[]



    # print(int(len(num)/3))
    num1=num[0:len(num)%3]


    n1=[int(x) for x in num1]
    
    if len(n1)>0:
        reverall.append(convert(n1))
    
    ln=len(num)
    li=len(num)-3
    

    
    for itn in reverall:
        aller.append(itn)
        # print(aller)
    list_revers=[]
    for t3 in range(0,int(len(num)/3)):
        
        lid=num[li:ln]
        n1=[int(x) for x in lid]
        if len(n1)>0:
            list_revers.append(convert(n1))
            
        ln=ln-3
        li=li-3
    list_revers.reverse()
    for ad in list_revers:
        aller.append(ad)


    lival=[]
    shval=""
    for a in range(0,len(aller)):
        lival.append(finall(aller[a]))
        
    if len(lival)==1:
        shval="{}".format(lival[0])
        
    else:
        big_all=bignum_name[0:len(lival)-1]
        big_all.reverse()
        
        
        
        
        for item in range(0,len(lival)):
            
            if zero==True:
                bgn=big_all[0]
                shval=' '+lival[item]+' '+bgn
                return shval
            elif item<=len(big_all)-1 :
                bgn=big_all[item]+' و ' 
            
            if item==len(lival)-1:
                bgn=''

            shval+=' '+lival[item]+' '+bgn
    return shval
while True:
    s=input('enter num: ')
    print(get_first(int(s)))






        


            
        


# while True:

#     iner=input('enter num:')
#     print(finall(int(iner)))       
# for i in range(1,1000000000):
    
    
#     print(get_first(int(i)))

