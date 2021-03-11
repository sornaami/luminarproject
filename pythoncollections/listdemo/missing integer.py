#print least +ve missing integer

#[-1,0,2,3,4]=-->1
lst=[-1,0,2,3,4]
cnt=1
for i in range(0,len(lst)):
    if(cnt in lst):
        pass
    else:
        print(cnt,"is the least +ve missing integer")
        break
    cnt+=1
#[-1,,0,1,,2,3]->4