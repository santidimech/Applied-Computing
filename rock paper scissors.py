import time
import random
    #define play game
name = input("What is your name? ")
def play_game():
    #ask for players name
    

    time.sleep(0.5)

    # Ask for number of rounds
    while True:
        rounds = int(input(f"Okay, {name}, how many rounds do you want to play between 3 and 10? "))
        
        time.sleep(1)
        
        if rounds < 3 or rounds > 10:
            print("Please choose between 3 and 10 rounds.")
        else:
            print(f"Okay, {rounds} rounds it is! I hope you're ready!")
            break
        
    # Set scores
    Wins = 0
    Loses = 0
    Draws = 0

    # Game loop - goes through each round until number of rounds has ended
    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        
        time.sleep(1)
        
        #state scores
        print("Currently, the scores are")
        print(f"Wins: {Wins}")
        print(f"Loses: {Loses}")
        print(f"Draws: {Draws}")

        # Ask for the input of the player and set it to a value between 1 and 3
        
        while True:
            player_input = input(f"Okay, {name}, what is your selection? (Rock, Paper or Scissors): ").strip().capitalize()

            if player_input == "Rock":
                player_choice = 1
                break
            
            elif player_input == "Paper":
                player_choice = 2
                break
            
            elif player_input == "Scissors":
                player_choice = 3
                break
            
            else:
                print("Try again, please choose between Rock, Paper, or Scissors.")
                player_choice = None

        # Countdown animation before the shoot - not needed just cool
        time.sleep(1)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.5)
        print("Shoot!")
        time.sleep(0.5)

        # Make the computer decide their response based off a random interger
        computerOutput = random.randint(1, 3)

        # Convert computer's choice from interger  to word
        if computerOutput == 1:
            computerChoice = "Rock"
        elif computerOutput == 2:
            computerChoice = "Paper"
        else:
            computerChoice = "Scissors"
            
        #state the computers selection
            
        print(f"The computer chose: {computerChoice}")

        time.sleep(1)

        # Determine outcome
        
        # Reminder: rock = 1, paper = 2, scissors = 3 rock beats paper, paper beats scissors, scissors beats rock (\) is used to continue line so it doesnt recognise line break (neat)
        if player_choice == computerOutput:
            print("It is a draw!")
            Draws += 1
        elif (player_choice == 1 and computerOutput == 3) or \
             (player_choice == 2 and computerOutput == 1) or \
             (player_choice == 3 and computerOutput == 2):
            print("You win this round!")
            Wins += 1
        else:
            print("You lose this round.")
            Loses += 1

        time.sleep(1)
        
        #state scores
        
        print(f"Currently, the scores are {Wins} win(s), {Draws} draw(s), and {Loses} defeat(s)")

        # Check if the player is losing more than winning and drawing combined and include a comment to make it seem more human
        
        if Wins > Loses + Draws:
            print("You're doing great! Keep it up!")
        elif Loses > Wins + Draws:
            print("It's not looking good, you're losing!")
        elif Draws > Wins + Loses:
            print("Not good, but not bad either!")

    # Final results after all rounds
    print("\n--- Game Over ---")
    print(f"Wins: {Wins}")
    print(f"Loses: {Loses}")
    print(f"Draws: {Draws}")

    # Final winner determination
    if Wins > Loses and Wins > Draws:
        print(f"Congratulations, {name}, you won the game!")
    elif Loses > Wins and Loses > Draws:
        print(f"Sorry, {name}, you lost the game.")
    else:
        print("The game ended in a draw!")

        # Redemption option if there's a tie
        if Wins == Loses:
            while True:
                redemption = input("Since you haven't beaten me, do you want redemption (yes/no)? ").strip().lower()

                if redemption == "yes":
                    print("Alright, redemption loading, good luck!")
                    time.sleep(1)
                    play_game()  # Restart the game
                    break  # Exit the loop after restarting the game
                elif redemption == "no":
                    print("All good, I hope to verse you another time to finally settle it")
                    break
                else:
                    print("Select a valid response")

def ask_ready():
    while True:
        ready = input("Are you ready to play Rock, Paper, Scissors? (yes/no): ").strip().lower()
    
        if ready == "yes":
            time.sleep(1)
            print("Great! Let's go!")
            play_game()
            break
            
        
        if ready == "no":
            time.sleep(1)
            print("No worries, come back when you're ready!")
            break
        
        else:
            time.sleep(0.5)
            print ("Select an appropriate response")
            time.sleep(0.5)

# Trigger the readiness check before starting the game
ask_ready()
