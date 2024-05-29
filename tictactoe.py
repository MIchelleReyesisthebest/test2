from array import *
import numpy as np


def winGame(newboard):

    if (newboard[0][0] ==  "X" and newboard[1][1] == "X" and newboard[2][2] == "X") or (newboard[0][0] ==  "O" and newboard[1][1] == "O" and newboard[2][2] == "O"):
        print("You won")
        return True
    elif (newboard[0][0] ==  "X" and newboard[1][0] == "X" and newboard[2][0] == "X") or (newboard[0][0] ==  "O" and newboard[1][0] == "O" and newboard[2][0] == "O"):
        print("You won")
        return True 
    elif (newboard[0][2] ==  "X" and newboard[1][1] == "X" and newboard[2][0] == "X") or (newboard[0][2] ==  "O" and newboard[1][1] == "O" and newboard[2][0] == "O"):
        print("You won")
        return True 
    elif (newboard[0][1] ==  "X" and newboard[1][1] == "X" and newboard[2][1] == "X") or (newboard[0][1] ==  "O" and newboard[1][1] == "O" and newboard[2][1] == "O"):
        print("You won")
        return True 
    elif (newboard[0][2] ==  "X" and newboard[1][2] == "X" and newboard[2][2] == "X") or (newboard[0][2] ==  "O" and newboard[1][2] == "O" and newboard[2][2] == "O"):
        print("You won")
        return True 
    elif (newboard[0][0] ==  "X" and newboard[0][1] == "X" and newboard[0][2] == "X") or (newboard[0][0] ==  "O" and newboard[0][1] == "O" and newboard[0][2] == "O"):
        print("You won")
        return True 
    elif (newboard[1][0] ==  "X" and newboard[1][1] == "X" and newboard[1][2] == "X") or (newboard[1][0] ==  "O" and newboard[1][1] == "O" and newboard[1][2] == "O"):
        print("You won")
        return True 
    elif (newboard[2][0] ==  "X" and newboard[2][1] == "X" and newboard[2][2] == "X") or (newboard[2][0] ==  "O" and newboard[2][1] == "O" and newboard[2][2] == "O"):
        print("You won")
        return True 
    


def changeboard(x,changeWord, board):
    x = int(x)
    for i in board:
        for j in i:
            if x == 1:
                board[0][0] = changeWord
            elif x == 2:
                board[0][1] = changeWord 
            elif x == 3:
                board[0][2]= changeWord
            elif x == 4:
                board[1][0] = changeWord
            elif x ==5:
                board[1][1] = changeWord
            elif x == 6:
                board[1][2] = changeWord
            elif x == 7:
                board[2][0] = changeWord
            elif x == 8:
                board[2][1] = changeWord
            elif x == 9:
                board[2][2]= changeWord               


print("Hello! Welcome to my Game!")
print("There are two players: X or O")
print("However, you only have nine attempts!")
print("May the odds be ever in your favor")
print()

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print the initial board
for i in board:
    for j in i:
        print(j, end=' ')
    print()
game_Over=False
number = 0

while number < 9 and not game_Over: 
    user_char = input("Please enter position number following a space (ex: 1 X): ")
    print(f"User input",user_char)
   
    substring_one= user_char[0:1]
    substring_two=user_char[2:3]
    print()
    changeboard(substring_one, substring_two, board)
     # Print the updated board
    for i in board:
        for j in i:
            print(j, end=' ')
        print()
    game_Over=winGame(board)
    #looks at the updated 
    number+=1
    print("Attempt: ", number)

if number >= 9:
    print()
    print()
    print("Sorry out of attempts")


    
     
     

