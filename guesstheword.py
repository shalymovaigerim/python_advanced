# Write a game, where the user has to guess a word
import random
list_of_words=['magazine','telephone','computer']
hints=['something that we buy to read articles and see illustrations','','']
k=random.randint(0,2)
the_word = list_of_words[k]
hint=hints[k]
game_over = False
player_1=[0]
player_2=[0]
n=0
board = list("*" * len(the_word))
while not game_over:
    n=(n%2)+1
    print("")
    print(f"{n} player your turn")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        if user_guess not in the_word:
            print('incorrect')
        if user_guess in board:
            print('Already guessed!')
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
                points=random.randint(1,5)
                if n==1:
                    player_1.append(points)
                else:
                    player_2.append(points)
    else:
        if user_guess == the_word:
            print(f"Correct! Congratulations! Winner is {n} player")
            
            game_over = True
        else:
            print("Incorrect, think again.")
    
   

# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.
