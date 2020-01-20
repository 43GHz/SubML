from threading import Thread
import socket
import sys
import csv
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
allconn=[]
alladdr=[]
allsts=[]
iddat=0
mindat=0
subdat=0
ansdat=0

class student:
    elist = []
    def __init__(self, id):
        self.id = id
    def errorlist(self, list):
        self.elist.append(list)

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
                if b!='':
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
    id=iddat
    ob=student(id)
    n=neg(mindat,subdat,ansdat)
    Detect_error(ob,str(mindat),str(subdat),str(ansdat))
    writefile(iddat,mindat,subdat,ansdat,mindat-subdat,ob.elist)


def borrow(s,min,sub,ans):
    if len(min) == 1:
            return 0
    else:
        bindex=[]
        m=convert(min)
        a=convert(ans)
        count=0      
        for x in range(len(min)):
            if sub[x]>min[x] or (sub[x]==min[x] and sub[x+1]>min[x+1]):
                print(f"Borrow at: {x}")
                bindex.insert(count,x)
                count+=1
        e1(s,min,sub,ans,bindex)
        e2(s,min,sub,ans,bindex)
        e3(s,min,sub,ans,bindex)
        e4(s,min,sub,ans,bindex)
        e5(s,min,sub,ans,bindex)
        e6(s,min,sub,ans,bindex)
        e7(s,min,sub,ans,bindex)
        e8(s,min,sub,ans)           #e9 nested in e8
        #e10(s,min,sub,ans,bindex)
        e11(s,min,sub,ans,bindex)
        e12(s,min,sub,ans,bindex)
        #e13
        e14(s,min,sub,ans,bindex)
        #e15(s,min,sub,ans,bindex)

                                        
def e1(s,min,sub,ans,bindex):
    size=len(bindex)            #starting of 419
    while(size>0):
        x=bindex[size-1]
        if(min[x]==1 and sub[x]!=1 and ans[x] == 0):
            s.errorlist("e1")
        size-=1

def e2(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        if(min[x]==1 and ans[x]== sub[x] and sub[x]!=1):
            s.errorlist("e2")
        size-=1

def e3(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        if(min[x]==sub[x]==1 and ans[x]==0):
            s.errorlist("e3")
        size-=1

def e4(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        if(ans[x]== 1 and sub[x]==1 and min[x]==1):
            s.errorlist("e4")
        size-=1

def e5(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1] 
        t1=min
        t2=int(min[x-1])
        t3=t2-1
        t4=int(sub[x-1])
        t5=int(ans[x-1])
        if(t5 == (t3+t4)):
            s.errorlist("e5")
        size-=1

def e6(s,min,sub,ans,bindex):
    tempmin = convert(min)
    tempsub = convert(sub)
    tempans = digits(tempmin - tempsub)
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]    
        t1=int(min[x-1])
        t2=int(sub[x-1])
        t3=t1-t2 + 1
        if(t3<10):
            tempans[x-1] = t3
        else:
            tempans[x-1] = 0
            tempans[x-2] = int(tempans[x-2])+1
        if(tempans == ans):
            s.errorlist("e6")
        size-=1

def e7(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        t1=int(min[x-1])
        t2=int(sub[x-1])
        t3=t1-t2 + 1
        if(t3 == 10):
            if((ans[x-1] == 1) and (ans[x] == 0)):
                s.errorlist("e7")
        size-=1

def e8(s,min,sub,ans):
    t1= convert(min) + convert(sub)
    t2= digits(t1)
    if(ans == t2):
        s.errorlist("e8")
    elif(ans == digits(t1-10)):
        s.errorlist("e9")
'''
def e10(s,min,sub,ans):
    pass
'''
def e11(s,min,sub,ans,bindex):              #end of page 419
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]           
        t1=int(min[x])+10
        t2=int(sub[x])
        t3=t1-t2
        t4=int(min[0])-1
        t5=t4-int(sub[0])
        if(t3==ans[x] and t5==ans[0]):
            s.errorlist("e11")
        size-=1

def e12(s,min,sub,ans,bindex):              #starting page 420
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]                  
        t1=int(ans[x])
        t2=int(min[x-1])-int(ans[x-1])
        if(t1 == t2):
            s.errorlist("e12")
        size-=1
'''
def e13(s,min,sub,ans,bindex):
    pass
'''
def e14(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        t1=int(min[x-1])
        count=0
        if(t1==0):
            while(min[x-1]==0):
                count+=1
                x-=1
        t2=int(min[x-count])
        t3=int(sub[x-count])
        t4=int(ans[x-count])
        if(t4 == (t2-t3)):
            s.errorlist("e14")
        size-=1
            
'''
def e15(s,min,sub,ans,bindex):
    size=len(bindex)
    while(size>0):
        x=bindex[size-1]
        t1=int(min[x-1])
        if(t1==0):
            t2=int(min[x-2])
            t3=(t2-1)-(sub[x-2])
            if(t2==t3):
                s.errorlist("e15")
                
        size-=1
'''

def neg(minu,sub,ans):#arguments as interger,return 1 if error detected,0 if no error
    ans=abs(ans)
    if ans==abs(minu-sub) or ans==abs(minu+sub):
        if minu<0 and sub<0:#both numbers-ve-subtract =neg1
            s.errorlist("neg1")
        elif minu<0 and sub>0:#minu<sub-add-result -ve=neg2
            s.errorlist("neg2")
        elif minu>0 and sub<0:
            s.errorlist("neg3")#minu>sub-add-result +ve=neg3
        return 1
    else:
        return 0
         
'''
def correctAns():
    #compare user input with calculated ans
    #if userinput doesnt math call errDetect()
    
    pass
def errDetect()
    flag=False #change flag value only when error is identified
    while(flag)
'''

def digits(num):# printing number  
                # using map() 
                # to convert number to list of integers 
    l1 = list(map(int, str(num)))
    return l1 

def convert(list): 
      
    # Converting integer list to string list 
    # and joining the list using join() 
    res = int("".join(map(str, list))) 
      
    return res 
     

def Detect_error(s,d1,d2,d3):
    print(f'({d1},{d2},{d3})')
    dd1=str(abs(int(d1)))
    dd2=str(abs(int(d2)))
    dd3=str(abs(int(d3)))
    l1 = digits(dd1)
    l2 = digits(dd2)
    l3 = digits(dd3)
    if len(l1)>len(l2):
            for i in range (len(l1)-len(l2)):
                l2.insert(i,0)
    if len(l1)>len(l3):
            for i in range (len(l1)-len(l3)):
                l3.insert(i,0)
    print(l1)
    print(l2)
    print(l3)
    #e8(s,l1,l2,l3)
    borrow(s,l1,l2,l3)
    print(f"Student's error list: {s.elist}")


def writefile(id,num1,num2,num3,correct,elst):
    with open("stdrec.csv",'a') as f:#during 1st time ='w'
        w=csv.writer(f)
       # w.writerow(["id","minuend","subtrathend","student answer","actual answer","errors"])#"should be incuded whie writing 1st time"
        w.writerow([id,num1,num2,num3,correct,elst])

t=Thread(target=lstn)
t.daemon=True
t.start()
checkthr=Thread(target=checkconn)
checkthr.daemon=True
checkthr.start()
