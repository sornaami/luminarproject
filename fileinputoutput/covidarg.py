f=open("complete.csv","r")
covid={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    date=data[0]
    state=data[1]
    confirmed=data[4]
    death=data[5]
    cured=data[6]
    if state not in covid:
        covid[state]={"date":date,"state":state,"confirmed":confirmed,"death":death,"cured":cured}
    else:
        pass
for k,v in covid.items():
    print(k,",",v)

def getcoviddetails(**args):
    print(args)
    cstate=args["state"]
    prope=args["prope"]
    print(covid[cstate][prope])
getcoviddetails(state="Kerala",prope="cured")


#getDetails("state name=kerala,prop=recovered")