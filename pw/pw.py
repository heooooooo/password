import time
def doixung(s):
    s0=''
    for i in range (len(s)-1,-1,-1):
        s0+=s[i]
    if s==s0:
        return True
    else:
        return False
def xoaso(s):
    s0=''
    for i in s:
        if i in '1234567890':
            s0+=i
    return s0
def timmax(s,k):
    max=s[0]
    for i in range(len(s)-k+1):
        if s[i]>max:
            max=s[i]
            cs=i
    return cs

f=open('pw/pw.inp')
g=open('pw/pw.out','w')
k=int(f.readline())
s=f.readline()
s1=xoaso(s)
res=s1[timmax(s1,k):]
print(res,file=g)
if doixung(res):
    print('YES',file=g)
else:
    print('NO',file=g)

f.close()
g.close()
print(time.process_time())
