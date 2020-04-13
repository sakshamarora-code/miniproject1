# Print the Game Instruction to the User/Player
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n")
while True:
    ans = input("Do you want to play again ? (Y/N) > ")
    if (ans == 'n' or ans == 'N') :
        break
print("\nThanks for playing Rock Paper Scissor Game \n")
