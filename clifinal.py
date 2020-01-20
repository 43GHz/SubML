import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
flag = False
idno=''
minu=''
subt=''
ans=''
try:
    s.connect(('172.20.10.4',6969))
except:
    print('Server unavailable')
    flag='True'

class student:
    elist = []
    def __init__(self, id):
        self.id = id

    def errorlist(self, list):
        self.elist.append(list)

while not flag: #main block
    id = input('enter student id: ')
    st=student(id)
    num1=int(input("enter the Minuend: "))#a=minuend,b=subtrahend
    num2=int(input("enter the Subtrahend: "))
    correct = num1-num2
    num3=int(input("enter the answer: "))
    if num3 == correct:
        print("Your answer is Correct")
        flag = True
    else:
        print("error detected")
    idno=str(id)+'/'
    minu=str(num1)+'/'
    subt=str(num2)+'/'
    ans=str(num3)+'/'
    data=idno+minu+subt+ans
    s.send(bytes(data,'utf-8'))
    minu=''
    subt=''
    ans=''
