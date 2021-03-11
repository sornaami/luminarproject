f=open("tweet","r")
tweets={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    data[0]=user
    data[1]=tweets
    if user not in tweets:
        tweets[user] = {"user": user, "tweets": tweets}
    else:
        pass
    for k, v in tweets.items():
        print(k, ",", v)