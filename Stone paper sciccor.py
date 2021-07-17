Turns=int(input("How many Games You want to play in this series ???"))
player1count = 0
player2count = 0
for i in range(1 ,Turns+1):
    print(" ===============   Round" ,i,  "Starts    ===============")
    firstTurn = input("Its Player 1 turn :")
    print ("\033[A                                          ")
    print("Player 1 Input is locked up ...............")
    secondTurn = input("Its Player 2 turn :")

    if(firstTurn == "stone" and secondTurn == "scissor" or firstTurn == "scissor" and secondTurn == "paper" or firstTurn == "paper" and secondTurn == "stone"):
        print("(:-) ===============    Player 1 wins the  battle    =============== :-)")

        player1count += 1

    elif(firstTurn == "scissor" and secondTurn == "stone" or firstTurn == "paper" and secondTurn == "scissor" or firstTurn == "stone" and secondTurn == "paper"):
        print(":-) ===============   Player 2 wins the battle   =============== :-)")
        player2count += 1

    elif(firstTurn == secondTurn):
        print(" ===============   Its DRAW ,","NO points in this Round",i,"   ===============")

    else:
        print(" ===============   Invalid INPUT   ===============")

    print("---------------    RECORD TILL NOW =>    ---------------")
    print("Player 1 wins",player1count,"Rounds   and  Player 2 wins" ,player2count,"Rounds")
print("==================    SCOREBOARD     ==================")
if(player1count > player2count):
    print("===============    CONGRATULATIONS,Player 1 won SERIES with " ,player1count,":",player2count,"    ===============")

elif(player2count > player1count):
    print("===============    CONGRATULATIONS,Player 2 won SERIES with " ,player2count,":",player1count,"    ===============")

elif(player1count == player2count):
    print("===============    ITS TIE    ===============")

