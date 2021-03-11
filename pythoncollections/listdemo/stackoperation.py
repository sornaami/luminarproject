#data structures


#different tpes of datastructures



#two different tpes of datastructures

#1.linear datastructure

    #array={10,20,30,40} elements stored in consecutive memory location
    #stack
    #queue

#2.nonlinear datstructure

    #elements not stored in consecutive memory location
    #linkedlist
    #node [data 10,next (adress of next node b)]---->[data20,next adress of nextnode c]---->[30 data,next]
    #       a                                           b                                      c
    #binarysearch tree
           #[20,18,17,19,25,23,24]
             #tree(root,left,right)
    #graph

    #stack operation
       #push -inserting element in stack
       #pop=deleting elementing from stack
        #LIFO

#
size=int(input("enter size"))
stk=[]
top=0

def push(element):
    global top
    if(top>(size))
    print("stack full")
    else:
       stk.append(element)
       top+=1
def pop():
    print("inside pop")

def display():
    print("inside display")
n=1
while(n!=0):
    option=int(input("enter operation 1)push 2)pop 3)display")
    if(option==1):
        element=