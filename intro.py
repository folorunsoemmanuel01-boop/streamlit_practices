import streamlit as st

# def main():
#   st.title("Introduction to Streamlit")

#   name = st.text_input("Enter your name:")
#   st.write(f"Hello,{name}")

# if __name__=="__main__":
#   main()

import random

def hangman():
  st.title("Hangman Game")
  
  words = ["python","game"]
  word = random.choice(words)

  play = 0

  while play < 3:
    guess = st.text_input("Enter a character")
    if guess.isalpha() and len(guess) == 1:
        st.write(guess)
        if guess in word:
          st.write(f"The position of the guess is {word.find(guess)}")
          st.write(f"Yes, The character {guess} is in {word}") 
        else:
          st.write("No")
    else:
      st.write("Invalid character")

hangman()
