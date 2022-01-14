import random 
actions = ['rock','paper','scissors']


def rock_paper():
    while True:
        welcome= input("Hello are you ready to play? y/n: ")
        if welcome == 'y':
            player_name = input("Enter your name to begin: ")
            print(f"Hello {player_name} Lets play Rock,Paper,Scissors!")
            player_choice = input("Choose rock paper or scissors: ").lower()
            random_output = random.choice(actions).lower()
            print (f"Random output is: {random_output}")
            for choice in actions:
                if player_choice == random_output:
                    print("TIE!")
                elif player_choice == 'rock' and random_output == 'paper' or player_choice == 'paper' and random_output == 'scissors':
                    print('Computer wins!')
                elif player_choice == 'paper' and random_output == 'rock' or player_choice == 'scissors' and random_output == 'paper':  
                    print('player wins')
                else:
                    print("You lose!")
        elif welcome == 'n':
            print('Come back when you are ready to play!')
        else:
            print('Thats not a valid response')
rock_paper()