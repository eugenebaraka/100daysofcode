
print('''
      __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')
print("Welcome to Treasure Island")
to_go = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if to_go == "right":
    print("Game Over!")
elif to_go == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if lake == "swim":
        print("Game Over!")
    elif lake == "wait":
        door = input("Which door do you want to open? Type 'red', 'blue', or 'yellow'\n").lower()
        if door == "red" or door == 'blue':
            print("Game Over!")
        elif door == 'yellow':
            print("You win!!")
        else:
            print("Oops!! Wrong choice")
    else:
        print("Oops!! Wrong choice")
else:
    print("Oops!! Wrong choice")

