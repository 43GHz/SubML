class student:
    elist = []
    def __init__(self, id):
        self.id = id

    def errorlist(self, list):
        self.elist.append(list)
        
def borrow(min,sub):
    if len(min) == 1:
            return 0
    else:       #add false borrow, false decrement
        if len(min)!=len(sub):#not in all cases length of min=sub,so add 0 for reainng degits
            for i in range (0,len(min)-len(sub)):
                sub.insert(i,0)
        for x in range(len(min)):
            if sub[x]>min[x]:#   ?!not all time minuend will be equal to subracsssssstend
                return x

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
        
def basicsub(s,correct,ans):
    right_ans = digits(correct)
    std_ans = digits(ans)
    s1 = len(right_ans)
    s2 = len(std_ans)
    if s2 > s1 or ans > correct:
        print("Basic Concept Fault")
        s.elist('BasicError')

    
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
    #l2 = list(map(int, str(s)))
    #l3 = list(map(int, str(a)))

    # printing result  
    #print ("The list from number is " + str(r1)) 
    #check = input('enter 5: ')
    #if int(check)==res[1]:
        #print("correct")
    #else:
        #print("incorrect")


def Detect_error(s,d1,d2,d3):
    print(f'({d1},{d2},{d3})')
    dd1=str(abs(int(d1)))
    dd2=str(abs(int(d2)))
    dd3=str(abs(int(d3)))
    l1 = digits(dd1)
    l2 = digits(dd2)
    l3 = digits(dd3)
    print(l1)
    print(l2)
    b1 = borrow(l1,l2)
    if b1 != None:
        s.errorlist("Borrow error")

    print(f"Borrow at: {b1}")
    print(f"Student's error list: {s.elist}")
flag = False
while not flag: #main block
    id = input('enter student id: ')
    s=student(id)
    num1=int(input("enter the Minuend: "))#a=minuend,b=subtrahend
    num2=int(input("enter the Subtrahend: "))
    correct = num1-num2
    num3=int(input("enter the answer: "))
    if num3 == correct:
        print("Your answer is Correct")
        flag = True
    else:
        print("error detected")
        basicsub(s,correct,num3)
        n=neg(num1,num2,num3)#pass as integer
        Detect_error(s,str(num1),str(num2),str(num3))

import csv
with open("stdrec.csv",'a') as f:#during 1st time ='w'
    w=csv.writer(f)
   # w.writerow(["id","minuend","subtrathend","student answer","actual answer","errors"])#"should be incuded whie writing 1st time"
    w.writerow([id,num1,num2,num3,correct,s.elist])