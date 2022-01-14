import random 
actions = ['rock','paper','scissors']


def rock_paper():   
    while True:
        welcome= input("Play a game with me would ya? (yes or no) or would you like to see the rules ( enter see rules): ")
        player_choice = input("Choose your weapon:rock paper or scissors or 'quit' to stop: ").lower()
        
        if welcome == 'yes':
            
            player_name = input("What should l call you?: ")
            print(f"Hello {player_name} Lets play Rock,Paper,Scissors!")
            
            random_output = random.choice(actions).lower()
            if player_choice == 'quit':
                print("Come back when you not scared!!")
                break
            elif player_choice == 'rock' and random_output == 'paper':
                print(f"You lousy choice of {player_choice} got destroy by {random_output}")
                print("Loserr, try again!")
            elif player_choice == 'paper' and random_output == 'scissors':
                print(f"You lousy choice of {player_choice} got destroy by {random_output}")
                print("Loserr, try again!")
            elif player_choice == 'scissors' and random_output == 'rock':
                print(f"You chose {player_choice} and the computer chose {random_output}")
                print("Loserr, try again!")
            elif random_output == 'rock' and player_choice == 'paper': 
                print(f"Surprisinly you chose {player_choice} and wrecked {random_output}")
                print("It's your lucky day")
            elif random_output == 'paper' and player_choice == 'scissors': 
                print(f"You chose {player_choice} and the computer chose {random_output}")
                print("It's your lucky day")
            elif random_output == 'scissors' and player_choice == 'rock':
                print(f"You chose {player_choice} and the computer chose {random_output}")
                print("It's your lucky day")
            else:
                print(f"You chose {player_choice} and the computer chose {random_output}")
                print("Its a tie")


        elif welcome == 'no':
            print('Come back when you not scared!!!')
            break
        elif welcome == 'see rules':
            print("""Choose between the three weapons below: """
            """ \nRock, \nPaper, \nScissors\n"""
            """Be warned rock smashes scissors, paper smothers rock and scissors chops up paper""")
        else:
            print('Thats not a valid response.')


rock_paper()
