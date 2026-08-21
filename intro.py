import streamlit as st

# def main():
#   st.title("Introduction to Streamlit")

#   name = st.text_input("Enter your name:")
#   st.write(f"Hello,{name}")

# if __name__=="__main__":
#   main()

# import random

# def hangman():
#   st.title("Hangman Game")
  
#   words = ["python","game"]
#   word = random.choice(words)

#   guess = st.text_input("Enter a character")
  
#   if guess.isalpha() and len(guess) == 1:
#       st.write(guess)
    
#       if guess in word:
#         st.write(f"The position of the guess is {word.find(guess)}")
#         st.write(f"Yes, The character {guess} is in {word}") 
#       else:
#         st.write("No")
#   else:
#       st.write("Invalid character")

# hangman()

# for i in range(1,11):
#   st.write(f"2 * {i} = {2*i}")

import random
import time

def guess_number():
  randomNumber = random.randint(1,20)
  st.write("WELCOME to Guess The Number GAME")
  name = st.text_input("Enter your name:")
  st.write(f"Hola!, {name}")

  attempts = 10
  play = True

  score_sheet = {}

  while play:
    guess_number = int(st.text_input("Enter a number"))
    if guess_number > randomNumber:
      attempts -= 1
      time.sleep(1)
      st.write(f"You have {attempts} attempts left")
      st.write("Too High")

    elif guess_number < randomNumber:
      attempts -= 1
      time.sleep(1)
      st.write(f"You have {attempts} attempts left")
      st.write("Too Low")

    else:
      score_sheet[name] = 'completed'
      time.sleep(1)
      st.write(score_sheet)
      st.write(f"Congratulations, {name} You got the number)

      st.write("\n")
      decision = text_input("Do you want to continue? Yes or No")
      if decision.lower == "yes":
        attempts = 10
        name = text_input("Enter your name")
        st.write(f"Hola, {name}")
        randomNumber = random.randint(1,20)
        
      else:
        play = False
        time.sleep(1)
        score_sheet[name] = 'completed'
        st.write("Thank u 4 playing")
        st.write(score_sheet)

      if attempts == 0
          st.write(f"You have {attempts} atempts left")
          score_sheet[name] = 'failed'
          st.write(score_sheet)

guess_number()
