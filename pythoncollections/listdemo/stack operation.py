size=int(input("enter size"))
stk=[]
top=0
def push(element):
    global top
    if(top>(size-1)):
        print("stack full")
    else:
        stk.append(element)
        top+=1
def pop():
    global top
    if(top<=0):
        print("empty stack")
    else:
        top=top-1
        print(top)
        print(stk[top],"popped")
def display():
    for i in range(0,top):
        print(stk[i])

n=1
while(n!=0):
    option=int(input("enter operation 1)push 2)pop 3)display"))
    if(option==1):
        element=int(input("enter element to push"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    n=int(input("do u want to continue press 0 for exit and 1 for continue"))

#procedure stk(stk,size,top)

#top->0
#size->3
#case 1:push(element)

  #chk stk is full
  #if(top>size)-->stk is full
  #else->stk[top]-->element
  #top=top+1

#pop()
 #