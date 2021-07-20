Turns=int(input("How many Games You want to play in this series ???"))
player1count = 0
player2count = 0
for i in range(1 ,Turns+1):
    print(" ===============   Round" ,i,  "Starts    ===============")
    p1 = input("Its Player 1 turn :")
    print ("\033[A                                          ")
    print("Player 1 Input is locked up ...............")
    p2 = input("Its Player 2 turn :")

    if(p1 == "stone" and p2 == "scissor" or p1 == "scissor" and p2 == "paper" or p1 == "paper" and p2 == "stone"):
        print("(:-) ===============    Player 1 wins the  battle    =============== :-)")

        player1count += 1

    elif(p1 == "scissor" and p2 == "stone" or p1 == "paper" and p2 == "scissor" or p1 == "stone" and p2 == "paper"):
        print(":-) ===============   Player 2 wins the battle   =============== :-)")
        player2count += 1

    elif(p1 == p2):
        print(" ===============   Its DRAW ,","NO points in this Round",i,"   ===============")

    else:
        print(" ===============   Invalid INPUT   ===============")

    if(player1count==(player2count+2)):
        print("Player 1 wins the tournament with max. wins.................................")
        break
    elif(player2count==(player1count+2)):
        print("player 2 wins the tournament with max. wins.................................")
        break

print("==================    SCOREBOARD     ==================")
if(player1count > player2count):
    print("===============    CONGRATULATIONS,Player 1 won SERIES with " ,player1count,":",player2count,"    ===============")

elif(player2count > player1count):
    print("===============    CONGRATULATIONS,Player 2 won SERIES with " ,player2count,":",player1count,"    ===============")

elif(player1count == player2count):
    print("===============    ITS TIE    ===============")
