import random

psrlist = ["PAPER","SCISSORS","ROCK"]
psrval = random.randint(0,2)

print (psrval)

while True:
    psrval = random.randint(0, 2)
    my_pick = input("Paper, Scissors, ROCK!").upper()
    print(psrlist[psrval])
    if my_pick == "PAPER":
       if psrlist[psrval] == "PAPER":
           print("Ah man, try again!")
       elif psrlist[psrval] == "SCISSORS":
           print("Snippy-Snip! You lose!")
       elif psrlist[psrval] == "ROCK":
           print("Paper covers rock! You win!")
    elif my_pick == "SCISSORS":
        if psrlist[psrval] == "PAPER":
            print("Snippy-Snip! You win!")
        elif psrlist[psrval] == "SCISSORS":
            print("Ah man, try again!")
        elif psrlist[psrval] == "ROCK":
            print("Haha, SMASH! You lose!")
    elif my_pick == "ROCK":
        if psrlist[psrval] == "PAPER":
            print("Paper covers rock! You lose!")
        elif psrlist[psrval] == "SCISSORS":
            print("Haha, SMASH! You win!")
        elif psrlist[psrval] == "ROCK":
            print("Ah man, try again!")