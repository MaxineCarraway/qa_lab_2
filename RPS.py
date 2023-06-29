import random
wins = 0
losses = 0
draw = 0

def RPS():  
    
# main game
        while True:
            print("{} wins, {} losses, {} draw {}".format(wins, losses, draw))
            print("Ready Player 1 - Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit")
            player1 = input("> ").upper
    
            if player1 == "Q":
            print("Thanks for playing!")
            break
#computer generated choice: 
    
Computer_choice = random.choice['R', 'S' 'P']
    
print("Player 1 chooses: ", player1)
    print("Player 2 chooses: "), Computer_choice

# Determine the outcome of the game         
    if player1 == Computer_choice:             
        print("It's a tie!")             
        draw += 1         
    elif (             
        (player1 == 'R' and Computer_choice == 'S')             
        or (player1 == 'P' and Computer_choice == 'R')             
        or (player1 == 'S' and Computer_choice == 'P')):             
        print('You win!')             
        wins += 1         
    else:             
        print('You lose!')             
        losses += 1 
    
RPS()

