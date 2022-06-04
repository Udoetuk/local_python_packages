import random
possible_options = ["R", "P", "S"]

def start_game():
    ready =  int(input("Ready to play the Rock-Paper-Scissors game? Enter 1, otherwise enter 2:"))
    if ready == 2:
        print("Game exited")
        pass

    
    while ready < 2: 
        print ("You would have to select among the following options inorder to play the game; R for rock, P for paper, S for scissors ")
        user = input('Choose from the list of options R,P,S: ')
        user_input = user.upper()  

        def play():
                CPU_choice = random.choice(possible_options)
                print("CPU's random choice is", CPU_choice)


                def play1():
                    if user_input == "R" and CPU_choice == "P":
                        print ("Player (Rock) : CPU (Paper)")
                        print("The winner is CPU")
        
                    elif user_input == "R" and CPU_choice == "S":
                        print("Player (Rock) : CPU (Scissors)")
                        print("The winner is Player")
        
                    elif user_input == "P" and CPU_choice == "R":
                        print("Player (Paper) : CPU (Rock)")
                        print("The winner is Player")
        
                    elif user_input == "P" and CPU_choice == "S":
                        print("Player (Paper) : CPU (Scissors)")   
                        print("The winner is CPU")
        
                    elif user_input == "S" and CPU_choice == "R":
                        print("Player (Scissors) : CPU (Rock)")   
                        print("The winner is CPU")
        
                    elif user_input == "S" and CPU_choice =="P":
                        print("Player (Scissors) : CPU (Paper)")
                        print("The winner is Player") 
        
                if user_input == CPU_choice :
                    print ("Its a tie. Try again")
                    start_game()
                else :
                    play1()



        if user_input in possible_options:
            print ("Turn played")
            play()
            break
            
        else:
            print ("error")

start_game()