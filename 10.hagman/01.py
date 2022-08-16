from multiprocessing.connection import answer_challenge
import random

def hangman(word):
    wrong_guess = 0
    stages = ["",
              "______  ",
              "|       ",
              "|    |  ",
              "|    O  ",
              "|   /|\ ",
              "|   / \ "]
    rletters = list(word)
    board = ["_"] * len (word)
    win = False 
    print("Welcome to Hanbman")
    
    while wrong_guess < len(stages) - 1 :
        print("\n")
        msg = "1chara enter :"
        char = input(msg)
        if char in rletters:
            character_index = rletters.index(char)
            board[character_index] = char
            rletters[character_index] = "$"
        else :
            wrong_guess += 1
        
        print(" ".join(board))
        print("\n".join(stages[0:wrong_guess + 1]))
        
        if "_" not in board :
            print("youre Win!!")
            print(" ".join(board))
            win = True
            break
    if not win :
        print("\n".join(stages[0:wrong_guess + 1]))
        print("youre lose!! correct is {}".format(word))

ans = ["cat" , "dog" , "tometo" , "banana"]
print(random.choice(ans))

hangman(random.choice(ans))


