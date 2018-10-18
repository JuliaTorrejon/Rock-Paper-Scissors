from random import randint

first_player  = input("First Player: Rock/Paper/Scissors? ").lower()

valid = {
    "rock":     1, 
    "paper":    2,
    "scissors": 3
    }

if first_player in valid:
    player_two_int = randint(1,3)
    display_int = str(player_two_int)

    #print ("Second Player: " + display_int) 

    second_player = list(valid.keys())[list(valid.values()).index(player_two_int)]
    print ("Second player: " + second_player)
    #second_player = input("Second Player: Rock/Paper/Scissors? ").lower()
    if second_player in valid:
        print ("Both answers valid")
        if (first_player == "rock") and (second_player == "scissors"):
            print ("First player wins, rock beats scissors")
        elif (first_player == "paper") and (second_player == "rock"):
            print ("First player wins, paper beats rock")
        elif (first_player == "scissors") and (second_player == "paper"):
            print ("First player wins, scissors beats paper")
        elif (second_player == "scissors") and (first_player == "paper"):
            print ("Second player wins, scissors beats paper")
        elif (second_player == "paper") and (first_player == "rock"):
            print ("Second player wins, paper beats rock")
        elif (second_player == "rock") and (first_player == "scissors"):
            print ("Second player wins, rock beats scissors")
        #elif (first_player == "rock") and (second_player == "rock"):
            #print ("It's a draw")
        #elif (first_player == "paper") and (second_player == "paper"):
            #print ("It's a draw")
        #elif (first_player == "scissors") and (second_player == "scissors"):
            #print ("It's a draw")
        else:
            print ("It's a draw")
            
    else:
        print ("Try again")
else:
    print ("Try again")

