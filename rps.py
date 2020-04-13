# Print the Game Instruction to the User/Player
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n")
while True:
    # Tell User to enter either Rock, Paper, Scissor
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n")
    user_choice = input("User turn: > ")
    print("User has choosen : " + user_choice + "\n")
    ans = input("Do you want to play again ? (Y/N) > ")
    if (ans == 'n' or ans == 'N') :
        break
print("\nThanks for playing Rock Paper Scissor Game \n")
