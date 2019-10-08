#%%
#%%
import random
questions = {
            "What year is the Indonesia's independence day?" : {
                "Answer": "A.1945,B.1969,C.1887,D.1998",
                "RightAnswer" : "A"
            },
            "what car brand use its symbol a horse?" : {
                "Answer" : "A.Lamborghini,B.Ford,C.Ferrari,D.Dodge",
                "RightAnswer" : "C"
            }, 
            "Who is the first Indonesia's President?" : {
                "Answer" : "A.Soeharto,B.Obama,C.Kim jong un,D.Soekarno",
                "RightAnswer" : "D"
            },
            "What is the name of the 4th planet in our solar system?" : {
                "Answer" : "A.Mars,B.Earth,C.Jupiter,D.Pluto",
                "RightAnswer" : "A"
            }
    }
l = list(questions.items())
random.shuffle(l)
questions = dict(l)

def main():
    print("WELCOME TO WHO WANTS TO BE A MILLIONAIRE!!\n")
    money = 100
    for question,data in questions.items():
        print(question)
        print(data["Answer"])
        print()
        hel = input("Do you need help?(Y)/(N)").upper()
        if hel == "Y":
            print("1.50/50  2.ask audience")
            lifeline(data)
        ans = input("Enter your answer:").upper()
        if ans == data["RightAnswer"]:
            print("Correct!, you got $",money)
            money += 100
        else:
            print("Wrong Answer!,you only got $",money)
            break
    print("CONGRATULATIONS YOU GOT ALL CORRECT!,YOU GOT BONUS $100.YOU WIN $",money)

def lifeline(q):
    choice = input()
    if choice == "1":
        print(q["RightAnswer"],random.choice(["A","B","C","D"]))
    else:
        print("The audience answers ",random.choice(["A","B","C","D"]))
    
    




