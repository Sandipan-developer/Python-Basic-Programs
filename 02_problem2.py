import random

def game():
    print("You are playing a game...")
    score=random.randint(1,45)
    print("Your score is ",score)

    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    if(score>hiscore):
        with open ("hiscore.txt","w") as f:
            f.write(str(score))

game()
    