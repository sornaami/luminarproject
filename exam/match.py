f=open("ipl.txt","r")
team={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    no=data[0]
    name=data[1]
    matches=data[2]
    win=data[3]
    loss=data[4]
    pts=data[5]
    if name not in team:
        team[name]={"no":no,"name":name,"matches":matches,"win":win,"loss":loss,"pts":pts}
    else:
        pass
    for k,v in team.items():
        print(k,",",v)
def getteamdetails(**args):
    team_name=args["name"]
    prope=args["prope"]
    if(name in team):
        print(team[team_name][prope])
    else:
        print("no team found")

getteamdetails(name="MI",prope="win")





