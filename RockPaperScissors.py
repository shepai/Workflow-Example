import random #import the random library and it's functions

def checkWin(player,bot): #check win function which will output and return who wins
    if player==bot: #if they are the same it is a draw
        print("draw")
    else:
        wins=[["p","r"],["r","s"],["s","p"]] #th possible win solutions
        if [player,bot] in wins: #check if the player and bot are a possible win
            print("Player wins")
            return "p"
        else: #it cant be a draw so it must be a bot win
            print("Bot wins")
            return "b"
choices=["r","p","s"] #the choices are presented in a list for simplicity
print("Welcome to RPS")
userinput=""
playerpoints=0
botpoints=0
while userinput!="q": #loop till the user enters q for quit
    userinput=input("p for play, q for quit: ") #gather input from the user
    if userinput=="p":
        #play
        c=input("r for rock, p for paper, and s for scissors: ")
        if c in choices:
            bot=(random.choice(choices))#get bot response
            print("Bot choice:",bot)
            winner=checkWin(c,bot)#check win
            if winner=="p":
                playerpoints+=1 #increase points if player wins
            elif winner=="b":
                botpoints+=1 #increase points if bot wins
        else:
            print("Invalid choice")
    elif userinput!="q": #if the input is not known 
        print("Please enter p or q")
    print("Player:",playerpoints)
    print("Bot:",botpoints)
