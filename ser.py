from threading import Thread
import socket
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
allconn=[]
alladdr=[]
allsts=[]
iddat=0
mindat=0
subdat=0
ansdat=0
def lstn():
    s.bind(('',6969))
    s.listen()
    while True:
        conn,addr=s.accept()
        s.setblocking(1)
        allconn.append(conn)
        alladdr.append(addr)
        allsts.append(0)
        print('conn made')
        print(alladdr)

def checkconn():
    while True:   
        for i in allconn:
            if allsts[flag]==0:
                clithr=Thread(target=cliconn,args=(i,))
                clithr.daemon=True
                clithr.start()
                allsts[flag]=1
                flag=flag+1
            else:
                flag=flag+1
        flag=0

def cliconn(conn):
    try:
        while True:
            j=repr(conn.recv(1024))
            if j!='':
                a=list(j)
                a.pop(0)
                a.pop()
                a.pop(0)
                b=''.join(a)
                print(b)
                norm(b)
    except ConnectionResetError:
        print('A client has left')

def norm(a):
    temp=list(a)
    idtemp=''
    mintemp=''
    subtemp=''
    anstemp=''
    jk=0
    for i in temp:
        if i=='/':
            jk=jk+1
            break
        else:
            idtemp=idtemp+i
            jk=jk+1
    for i in temp[jk::]:
        if i=='/':
            jk=jk+1
            break
        else:
            mintemp=mintemp+i
            jk=jk+1
    for i in temp[jk::]:
        if i=='/':
            jk=jk+1
            break
        else:
            subtemp=subtemp+i
            jk=jk+1
    for i in temp[jk::]:
        if i=='/':
            jk=jk+1
            break
        else:
            anstemp=anstemp+i
            jk=jk+1

    iddat=int(idtemp)
    mindat=int(mintemp)
    subdat=int(subtemp)
    ansdat=int(anstemp)
    print(iddat)
    print(mindat)
    print(subdat)
    print(ansdat)

class student:
    elist = []
    def __init__(self, id):
        self.id = id
    def errorlist(self, list):
        self.elist.append(list)   
def borrow(min,sub,ans,a):
    an=[]
    count=0
    for i in range (0,len(sub)):
        if a==4:
            if min[i]==0:
                min[i]=9
        if a==3 and i!=len(sub)-1:
            if min[i+1]<sub[i+1]:
                sub[i+1]-=1
            else:
                min[i+1]+=-1
        if min[i]<sub[i]: # line 5
            if a!=8:
                min[i]+=10
                an.append(min[i]-sub[i])
            if min[i+1]>sub[i+1]:
                if a==2:
                    min[i+1]-=1
                if a==5:
                    sub[i+1]-=1
                if a==8:
                    if min[i+1]==0:
                        an.append(sub[i+1])
                        min[i+2]+=10
                    else:
                        an.append(min[i]-sub[i])
                        min[i+1]-=1
        else:
            an.append(min[i]-sub[i])
        count+=1
    for i in range(0,len(min)-len(sub)):
        an.append(min[i+count])
    count=0
    for i in range(0,len(ans)):
        if an[i]==ans[i]:
            count+=1
    if count==len(ans):
        s.errorlist(a)
def neg(minu,sub,ans):#arguments as interger,return 1 if error detected,0 if no error
    ans=abs(ans)
    if ans==abs(minu-sub) or ans==abs(minu+sub):
        if minu<0 and sub<0:#both numbers-ve-subtract =neg1
            s.errorlist(8)
        elif minu<0 and sub>0:#minu<sub-add-result -ve=neg2
            s.errorlist(9)
        elif minu>0 and sub<0:
            s.errorlist(10)#minu>sub-add-result +ve=neg3
        return 1
    else:
        return 0
        
def error1(m,s,a):
    temp=0
    for i in range(0,len(s)):
        if m[i]<s[i]:
            if(m[i]==0):
                temp=s[i]
            if temp==a[i]: 
                s.errorlist(1)
def error6(min,sub,ans):
    a=True
    count=0
    for i in range(0,len(sub)):
        if (len(sub)-1)!=i:
                if len(sub)>i:
                    if min[i]<sub[i] and a:
                        min[i]+=10
                        min[i+1]-=1
                        a=False
                if min[i]-sub[i]==ans[i] or min[i]-sub[i]*-1==ans[i]:
                        count+=1
               # print(min[i]-sub[i])
    if count==len(ans):
        s.errorlist(6)
def error7(min,sub,ans):
    count=0
    for i in range(0,len(sub)):
        if len(sub)-1!=i:
            if min[i]==0:
                 min.remove(0)
            if len(sub)>i:
                if min[i]<sub[i]:
                    min[i]+=10
                    min[i+1]-=1
                if min[i]-sub[i]==ans[i]:
                    count+=1
            elif min[i]==ans[i]:
                count+=1
    if count==len(ans):
        s.errorlist(7)
        
def digits(num):# printing number  
                # using map() 
                # to convert number to list of integers 
    l1 = list(map(int, str(num)))
    return l1 

def Detect_error(s,d1,d2,d3):
    print(f'({d1},{d2},{d3})')
    dd1=str(abs(int(d1)))
    dd2=str(abs(int(d2)))
    dd3=str(abs(int(d3)))
    l1 = digits(dd1)
    l2 = digits(dd2)
    l3 = digits(dd3)
    l1=l1[::-1]
    l2=l2[::-1]
    l3=l3[::-1]
    print(l1)
    print(l2)
    for i in range(0,len(l3)):
        if i>=len(l2):
            l2.append(0)
    for i in range(2,5):
        borrow(l1,l2,l3,i)
    error6(l1,l2,l3)
    error1(l1,l2,l3)
    error7(l1,l2,l3)
    neg(l1[i],l2[i],l3[i])
    print(f"Student's error list: {s.elist}")

t=Thread(target=lstn)
t.daemon=True
t.start()
checkthr=Thread(target=checkconn)
checkthr.daemon=True
checkthr.start()
