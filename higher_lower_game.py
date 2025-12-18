import random
from game_data import data
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


score = 0

people1 = ""
people2 = ""
def sortear():
    global people1,people2
    people2 = random.choice(data)
    people1 = people2
    people2 = random.choice(data)
    if people1 == people2:
        people2 = random.choice(data)

sortear()

def check_answer(a,b,guess):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"
def start():
    global score, data
    print(logo)
    print(f"Who has more Followers on Instagram?\n")
    print(f"Compare A: {people1.get("name")}, a {people1.get("profession")}, from {people1.get("country")}.")
    print(f"{vs}")
    print(f"Against B: {people2.get("name")}, a {people2.get("profession")}, from {people2.get("country")}.")
    people_choice = input("Who has more Followers? Type 'A' or 'B': ").lower().strip()
    if people_choice in ["a","b"]:
        followers_people1 = people1.get("followers")
        followers_people2 = people2.get("followers")
        is_correct = check_answer(a=followers_people1,b=followers_people2,guess=people_choice)
        print("\n"*40)
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
            sortear()
            start()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            score = 0
            sortear()
            start()
        

start()