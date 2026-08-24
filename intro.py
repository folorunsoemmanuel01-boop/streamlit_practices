import streamlit as st

def main():
   st.title("Introduction to Streamlit")

   name = st.text_input("Enter your name:")
   st.write(f"Hello,{name}")

if __name__=="__main__":
   main()

import random
import streamlit as st


def new_game():
    words = ["python", "game", "banana", "computer", "programming"]
    st.session_state["word"] = random.choice(words)
    st.session_state["guessed"] = []
    st.session_state["game_over"] = False


def hangman():
    st.title("Hangman Game")

    # Start the first game
    if "word" not in st.session_state:
        new_game()

    word = st.session_state["word"]
    guessed = st.session_state["guessed"]

    # Show the current word
    display_word = ""

    for character in word:
        if character in guessed:
            display_word += character + " "
        else:
            display_word += "_ "

    st.write("Word:", display_word)

    # If the player has won
    if all(character in guessed for character in word):
        st.success(f"🎉 You won! The word was {word}")

        if st.button("Play Again"):
            new_game()
            st.rerun()

        return

    # Get a guess
    guess = st.text_input("Enter a character")

    if guess:

        if not guess.isalpha() or len(guess) != 1:
            st.error("Please enter ONE alphabet character.")

        elif guess in guessed:
            st.warning("You already guessed that character!")

        else:
            guessed.append(guess)

            if guess in word:
                st.success(f"Yes! '{guess}' is in the word.")
            else:
                st.error(f"No! '{guess}' is not in the word.")

            st.rerun()


hangman()

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


  

