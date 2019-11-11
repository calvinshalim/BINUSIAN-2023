#%%
import json
import random
pokemons = {}

def loadjson(): #this is to load the pokemon json file that has all the pokemon data
    with open("pokemon project.json") as f:
        x = json.load(f)
        for pokemonname, data in x["pokemon"].items() :
            moves = []
            for movedata in data["moves"]: #to get all of the pokemon data for ex.power, health, speed, etc.
                moves.append(move(movedata["name"],movedata["power"]))
            pokemons[pokemonname]=pokemon(pokemonname,data["health"],data["types"],moves,data["speed"])
        
class pokemon(object): #this is to turn the data form json into an object
    def __init__(self,name,health,types,moves,speed):
        self.name = name
        self.health = health
        self.types = types
        self.moves = moves
        self.speed = speed
            
    def attack(self,target,move): #a function to initiate extra damage or reduced damage that depends on pokemon type
        modifier = 1
        if target.types == "Fire":
            if self.types == "Grass":
                modifier = 0.50 #damage will be reduced by 50% of it's original damage
            elif self.types == "Water":
                modifier = 1.25
        elif target.types == "Water":
            if self.types == "Fire":
                modifier = 1.25 #damage will be amplified for 25% from it's original damage
            elif self.types == "Grass":
                modifier = 0.50
        elif target.types == "Grass":
            if self.types == "Fire":
                modifier = 1.25
            elif self.types == "Water":
                modifier = 0.50
                
        target.health -= move.power*modifier #to reduced the pokemon health
        print("\n",self.name,"USED",move.movename,"\n",target.name,"HEALTH REDUCED",move.power*modifier,"\n")

class move():
    def __init__(self,movename,movepower):
        self.movename = movename
        self.power = movepower

def battle(mypoke,enemypoke):
    winner = ""
    while True:
        for index,move in enumerate(mypoke.moves): #print all of the pokemon's attack
            print(index + 1, move.movename,move.power)
        print("\n",mypoke.name,"Health >>",mypoke.health)
        print("\n",enemypoke.name,"Health >>",enemypoke.health)
        atkchoice = int(input("Select move >> ")) #choose what attack you want.
        chosenmove = mypoke.moves[atkchoice-1]
        enemymove = random.choice(enemypoke.moves) #input random to enemy's attack
        firstmove = None
        secondmove = None
        if mypoke.speed >= enemypoke.speed: #which get the first move depends on the speed of each pokemon
            firstmove = (mypoke,chosenmove)
            secondmove = (enemypoke,enemymove)
        else:
            firstmove = (enemypoke,enemymove)
            secondmove = (mypoke,chosenmove)
            
        firstmove[0].attack(secondmove[0],firstmove[1])#if the pokemon who moves second has 0 hp, it can't attack  again
        if secondmove[0].health <= 0:
            winner = firstmove[0].name
            break
        secondmove[0].attack(firstmove[0],secondmove[1]) #if the pokemon who moves first has 0 hp, it can't attack anymore
        if firstmove[0].health <= 0:
            winner = secondmove[0].name
            break
    print("\n",winner,"IS THE WINNER!") #to tell you who is the winner      
                
def main():
    f = open('pokemonart.txt', 'r') #i make  this just so it's a little bit coolery
    file_contents = f.read()
    print("  ",file_contents)
    print("\n","="*8,"WELCOME TO POKEMON BATTLE","="*8)
    print("\n              PICK YOUR POKEMON!")
    
    temp = {}
    for index,poke in enumerate(pokemons.keys()): #print all the listing pokemon
        print(index + 1,poke)    
        temp[index+1] = poke
    pick = int(input("Enter number >> ")) #pick a pokemon by entering the number
    pickpoke = pokemons[temp[pick]]
    enemypoke = pokemons[random.choice(list(pokemons.keys()))] #to randomly pick enemy's pokemon
    battle(pickpoke, enemypoke) #to call in the battle function
    


loadjson() # load the json file
main() #call the game function
