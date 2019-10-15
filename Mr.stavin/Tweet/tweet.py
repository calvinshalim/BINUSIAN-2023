#%%
import json
filename = "tweet.json"
tweets = []

def openfile(filename):
    with open(filename) as f:
        return json.loads(f.read())


def savefile(outputfile,datajson):
    with open(outputfile, "w") as f:
        json.dumps(datajson,f)
        
def tweet(username,tweet):
    tweets.append({"text" : tweet,"username" : username})
    savefile("tweetsave.json",tweets)
    
tweets = openfile("tweetsave.json")
choice =["a" , "b"]
while True:
    print("a.input tweet\n b.print tweet")
    alph = input(">> ")
    if alph in choice:
        if alph == "a":
            username = input("Username: ")
            text = input("Tweet: ")
            tweet(username, text)
        if alph == "b":
            for tweet in tweets["tweets"]:
                print(f'{tweet["username"]}:', tweet["text"].replace("\n", " "))
        else:
            continue