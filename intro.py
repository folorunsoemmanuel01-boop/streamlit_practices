import streamlit as st

def main():
   st.title("Introduction to Streamlit")

   name = st.text_input("Enter your name:")
   st.write(f"Hello,{name}")

if __name__=="__main__":
   main()

def hangman():
    st.title("Hangman Game")

    # CHOOSE DIFFICULTY
    difficulty = st.selectbox(
        "Choose difficulty:",
        ["Easy", "Medium", "Hard"]
    )

    # CHOOSE WORDS AND ATTEMPTS 
    if difficulty == "Easy":
        st.write("You selected Easy")
        words = ["cat", "dog", "sun"]
        max_attempts = 5

    elif difficulty == "Medium":
        st.write("You selected Medium")
        words = ["python", "program", "saloon", "salmon"]
        max_attempts = 7

    else:
        st.write("You selected Hard")
        words = ["algorithm", "programming", "language", "javascript","onomatopoeia"]
        max_attempts = 10

    # RESET GAME WHEN DIFFICULTY CHANGES
    if "difficulty" not in st.session_state:
        st.session_state["difficulty"] = difficulty

    if st.session_state["difficulty"] != difficulty:
        st.session_state["difficulty"] = difficulty
        st.session_state["word"] = random.choice(words)
        st.session_state["guessed"] = []
        st.session_state["attempts"] = max_attempts

    # START GAME
    if "word" not in st.session_state:
        st.session_state["word"] = random.choice(words)

    if "guessed" not in st.session_state:
        st.session_state["guessed"] = []

    if "attempts" not in st.session_state:
        st.session_state["attempts"] = max_attempts

    word = st.session_state["word"]
    guessed = st.session_state["guessed"]
    attempts = st.session_state["attempts"]

    st.write(f"Attempts left: {attempts}")

    # DISPLAY WORD
    display_word = ""

    for character in word:
        if character in guessed:
            display_word += character
        else:
            display_word += "_"

    st.write("Word:", display_word)

    # INPUT
    guess = st.text_input(
        "Enter a character:",
        key="guess_input"
    )

    # STOP GAME
    if guess.lower() == "done":
        st.write("Game stopped.")
        st.stop()

    # PROCESS GUESS
    if guess:
        if guess.isalpha() and len(guess) == 1:

            guess = guess.lower()

            if guess in guessed:
                st.warning("You've already guessed that letter.")

            else:
                guessed.append(guess)

                if guess in word:
                    st.success(
                        f"Correct! '{guess}' is in the word."
                    )

                    # Show position
                    positions = [
                        i for i, character in enumerate(word)
                        if character == guess
                    ]

                    st.write(f"Position(s): {positions}")

                else:
                    st.error(
                        f"No! '{guess}' is not in the word."
                    )

                    st.session_state["attempts"] -= 1

                st.rerun()

        else:
            st.warning("Please enter ONE alphabet character.")

    # CHECK WIN
    if all(character in guessed for character in word):
        st.success(f"You won! The word was **{word}**")

        if st.button("Play Again"):
            new_word = random.choice(words)

            while new_word == st.session_state["word"] and len(words) > 1:
                new_word = random.choice(words)

            st.session_state["word"] = new_word
            st.session_state["guessed"] = []
            st.session_state["attempts"] = max_attempts
            st.session_state["guess_input"] = ""

            st.rerun()

    # CHECK GAME OVER
    elif st.session_state["attempts"] <= 0:
        st.error(f"GAME OVER! The word was **{word}**")

        if st.button("Play Again"):
            new_word = random.choice(words)

            while new_word == st.session_state["word"] and len(words) > 1:
                new_word = random.choice(words)

            st.session_state["word"] = new_word
            st.session_state["guessed"] = []
            st.session_state["attempts"] = max_attempts
            st.session_state["guess_input"] = ""

            st.rerun()


hangman() 


