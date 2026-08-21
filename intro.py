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


# import random

# def hangman():

#   words = ["banana", "apples", "salmon"]

#   word = random.choice(words)

#   progress = ["_"] * len(word)

#   st.write("WELCOME TO HANGMAN")

#   while True:

#     st.write("\nWord:", " ".join(progress))

#     guess = st.text_input("Guess a letter: ").lower()

#     if guess in word:

#       for i in range(len(word)):
#           if word[i] == guess:
#             progress[i] = guess
            
#       st.write("Correct")

#     else:
#       st.write("Wrong guess")

#     if "_" not in progress:
#       st.write("\nCongratulations!")
#       st.write("The word was:", word)
#       st.write("You Win")
#       break

# hangman()

def character_Func():
  user_Character = st.text_input("Enter a word:")
  counter = 0

  list_Characters = []

  for char in user_Character:
    if counter % 2 == 0:
        list_Characters.append(char)
    counter += 1

  return list_Characters

character_Func()


