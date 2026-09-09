import streamlit as st
import random

def main():
  st.title("Hangman Game")
  words = ["Dog","Fish","Donkey"]

  if "choice" not in st.session_state:
    st.session_state.choice = random.choice(words).lower()
    st.session_state.guesses = list(len(st.session_state.choice)*"_")
    st.session_state.attempts = 5
  
  user_guess = st.text_input("Enter a character:").lower()

  if st.button("Play"):
    
    if len(user_guess) == 1:
      if user_guess in st.session_state.choice:
        pos = st.session_state.choice.find(user_guess)
        st.session_state.guesses[pos] = user_guess
  
        st.write(" ".join(st.session_state.guesses))
        if list(st.session_state.choice) == st.session_state.guesses:
          if st.success(f"Congratulations, you won the game with {5 - st.session_state.attempts} attempts left"):
             
            if st.button("Play Again!"):
                for key in st.session_state.keys():
                    del st.session_state[key]
  
                st.rerun()
      else:
        st.session_state.attempts -= 1
        if st.session_state.attempts == 0:
          st.error("Game Over!")
          
          for key in st.session_state.keys():
                del st.session_state[key]
          st.rerun()
        
        else:
          st.write(f"You have {st.session_state.attempts} attempts left.")
    else:
      st.write("This is not how to play the game!!")

 

if __name__ == "__main__":
  main()
