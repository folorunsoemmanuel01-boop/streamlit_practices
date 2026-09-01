import streamlit as st

def main():
   st.title("Introduction to Streamlit")

   name = st.text_input("Enter your name:")
   st.write(f"Hello,{name}")

if __name__=="__main__":
   main()



# def usersInput():

#     st.title("Enter Numbers")

#     if "userList" not in st.session_state:
#         st.session_state["userList"] = []

#     userInput = st.text_input("Enter a number:")

#     if st.button("Add Number"):

#         if userInput.isdigit():
#             st.session_state[userList].append(int(userInput))
#             st.success("Number added!")

#         elif userInput == "":
#             st.warning("Please enter a number")

#         else:
#             st.error("Invalid Character")

#     if st.button("Done"):
#         st.write("Your Final List:")
#         st.write(st.session_state.userList)


# usersInput()
   

# import random
# import streamlit as st


# def hangman():
#     st.title("Hangman Game")

#     # difficulty = st.radio(
#     #    "Choose difficulty:", 
#     #    ["Easy", "Medium", "Hard"]
#     # ) 

#     difficulty = st.selectbox(
#        "Choose difficulty:",
#        ["Easy", "Medium", "Hard"]
#     )

#    #CHOOSE WORDS AND ATTEMPTS
#     if difficulty == "Easy":
#       st.write("You selected Easy")
#       words = ["cat", "dog", "sun"]
#       max_attempts = 10
       
#     elif difficulty == "Medium":
#       st.write("You selected Medium")
#       words = ["python","program", "saloon", "salmon"]
#       max_attempts = 7
       
#     else:
#       st.write("You selected Hard")
#       words = ["algorithm", "programming", "language", "javascript", "aieee"]
#       max_attempts = 5

#    # RESET GAME WHEN DIFFIULTY CHANGES
#     if "difficulty" not in st.session_state:
#         st.session_state["difficulty"] = difficulty

#     if st.session_state["difficulty"] != difficulty:
#         st.session_state["difficulty"] = difficulty
#         st.session_state["word"] = random.choice(words)
#         st.session_state["guessed"] = []
#         st.session_state["attempts"] = max_attempts

#    #START GAME

#     if "word" not in st.session_state:
#         st.session_state["word"] = random.choice(words)

#     if "guessed" not in st.session_state:
#         st.session_state["guessed"] = []

#     if "attempts" not in st.session_state:
#         st.session_state["attempts"] = max_attempts

#     word = st.session_state["word"]
#     guessed = st.session_state["guessed"]
#     attempts = st.session_state["attempts"]

#     st.write(f"Attempts left: {attempts}")

#    #DISPLAY  
#    display_word = ""

#     for character in word:

#     guess = st.text_input("Enter a character")

#     if guess.lower() == "done":
#        st.write(("Game stopped."))
#        st.stop()

#     if guess.isalpha() and len(guess) == 1:

#         if guess in guessed:
#            st.warning("You've guessed that letter")
           
#         if guess not in guessed:
#             guessed.append(guess)

#         if guess in word:
#             st.write(f"The position is {word.find(guess)}")
#         else:
#             st.write(f"No! {guess} is not in the word")
           
#             st.session_state["attempts"] -= 1

#         display_word = ""

#         for character in word:
#             if character in guessed:
#                 display_word += character + ""
#             else:
#                 display_word += "_"

#         st.write("Word:", display_word)

#         if all(character in guessed for character in word):
#             st.success(f"You won! The word was {word}")

#             if st.button("Play Again"):

#                 new_word = random.choice(words)

#                 while new_word == st.session_state["word"]:
#                     new_word = random.choice(words)

#                 st.session_state["word"] = new_word
#                 st.session_state["guessed"] = []
#                 st.session_state["attempts"] = max_attempts
            
#                 st.rerun()
 
#         elif st.session_state["attempts"] <= 0:
           
#             st.error(f"GAME OVER! The word was {word}")

#             if st.button("Play Again"):
               
#                new_word = random.choice(words)

#             while new_word == st.session_state["word"]:
#                 new_word = random.choice(words)

#             st.session_state["word"] = new_word
#             st.session_state["guessed"] = []
           
#             st.session_state["attempts"] = max_attempts

#             st.rerun()


#     elif guess:
#         st.write("Invalid character")


# hangman()

# for number in range(1,6):
#    st.write(f"\nMultiplication Table for {number}")

#    for multiplier in range(1,16):
#       st.write(f"{number} X {multiplier} = {number * multiplier}")
   

# for i in range(1,11):
#    st.write(f"2 * {i} = {2*i}")


# import random

# def hangman():

#    words = ["banana", "apples", "salmon"]

#    word = random.choice(words)

#    progress = ["_"] * len(word)

#    st.write("WELCOME TO HANGMAN")

#    while True:

#      st.write("\nWord:", " ".join(progress))

#      guess = st.text_input("Guess a letter: ").lower()

#      if guess in word:

#        for i in range(len(word)):
#            if word[i] == guess:
#              progress[i] = guess
            
#        st.write("Correct")

#      else:
#        st.write("Wrong guess")

#      if "_" not in progress:
#        st.write("\nCongratulations!")
#        st.write("The word was:", word)
#        st.write("You Win")
#        break

# hangman()

# def character_Func():
#    user_Character = st.text_input("Enter a word:")
#    counter = 0

#    list_Characters = []

#    for char in user_Character:
#      if counter % 2 == 0:
#          list_Characters.append(char)
#      counter += 1

#    st.write(list_Characters)

# character_Func()

# Students = {'Student_1' : {'name' : 'Zidane',
#                             'age' : 23,
#                             'class' : 'SS3'},
#              'Student_2' : {'name' : 'Messi',
#                             'age' : 19,
#                             'class' : 'La Masia 3'},
#              'Student_3' : {'name' : 'Ronaldinho',
#                             'age' : 34,
#                             'class' : 'La Masia G'}}

# names = []
# age = []

# for student in Students:
#    names.append(Students[student]["name"])
#    age.append(Students[student]["age"])

# st.write(names)
# st.write(age)

# def character_Func():
#     user_Character = st.text_input("Enter a word:")
#     counter = 0

#     list_Characters = []

#     for char in user_Character:
#       if counter % 2 != 0:
#           list_Characters.append(char)
#       counter += 1

#     st.write(list_Characters)

# character_Func()


import random
import streamlit as st


def guessing_number():

    st.title("GUESS THE NUMBER GAME")

    # Get player's name
    name = st.text_input("Enter your name:", key="guess_name")

    if name:
        st.write(f"Hola, {name}!")

    # Create the secret number
    if "target_number" not in st.session_state:
        st.session_state["target_number"] = random.randint(1, 20)

    # Create attempts
    if "attempts" not in st.session_state:
        st.session_state["attempts"] = 10

    # Create score sheet
    if "score_sheet" not in st.session_state:
        st.session_state["score_sheet"] = {}

    # Create game status
    if "game_over" not in st.session_state:
        st.session_state["game_over"] = False

    # If game has ended
    if st.session_state["game_over"]:
        st.write("Game has ended.")

        if st.button("Start New Game"):
            st.session_state["target_number"] = random.randint(1, 20)
            st.session_state["attempts"] = 10
            st.session_state["game_over"] = False
            st.rerun()

        return

    # Get current values
    target_number = st.session_state["target_number"]
    attempts = st.session_state["attempts"]

    st.write(f"Attempts left: {attempts}")

    # User enters guess
    guess = st.number_input(
        "Guess a number between 1 and 20:",
        min_value=1,
        max_value=20,
        step=1,
        key="user_guess"
    )

    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        guess_button = st.button("Guess")

    with col2:
        end_button = st.button("END GAME")

    # End game
    if end_button:
        st.session_state["game_over"] = True
        st.write("Game stopped.")
        st.rerun()

    # Guess
    if guess_button:

        if guess == target_number:

            st.success(
                f"🎉 Correct, {name}! The number was {target_number}."
            )

            # Calculate score
            score = attempts * 10

            if name:
                st.session_state["score_sheet"][name] = score

            st.write(f"Your score: {score}")

            # Play again
            if st.button("Play Again"):

                st.session_state["target_number"] = random.randint(1, 20)

                # Make sure new number is different
                while st.session_state["target_number"] == target_number:
                    st.session_state["target_number"] = random.randint(1, 20)

                st.session_state["attempts"] = 10
                st.rerun()

        else:

            st.session_state["attempts"] -= 1

            if guess < target_number:
                st.warning("Too low! Try again.")

            else:
                st.warning("Too high! Try again.")

            # Check if attempts are finished
            if st.session_state["attempts"] <= 0:

                st.error(
                    f"GAME OVER! The number was {target_number}."
                )

                if st.button("Play Again"):

                    st.session_state["target_number"] = random.randint(1, 20)

                    while st.session_state["target_number"] == target_number:
                        st.session_state["target_number"] = random.randint(1, 20)

                    st.session_state["attempts"] = 10
                    st.rerun()

    # Score sheet
    if st.session_state["score_sheet"]:

        st.subheader("Score Sheet")

        for player, score in st.session_state["score_sheet"].items():
            st.write(f"{player}: {score}")


guessing_number()
  

