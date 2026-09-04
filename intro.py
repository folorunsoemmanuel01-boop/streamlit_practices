import random
import streamlit as st


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
        words = [
            "algorithm",
            "programming",
            "language",
            "javascript",
            "onomatopoeia"
        ]
        max_attempts = 10

    # INITIALIZE DIFFICULTY
    if "difficulty" not in st.session_state:
        st.session_state["difficulty"] = difficulty

    # RESET WHEN DIFFICULTY CHANGES
    if st.session_state["difficulty"] != difficulty:

        st.session_state["difficulty"] = difficulty
        st.session_state["word"] = random.choice(words)
        st.session_state["guessed"] = []
        st.session_state["attempts"] = max_attempts

        # Change input key
        st.session_state["input_number"] = (
            st.session_state.get("input_number", 0) + 1
        )

        st.rerun()

    # START GAME
    if "word" not in st.session_state:
        st.session_state["word"] = random.choice(words)

    if "guessed" not in st.session_state:
        st.session_state["guessed"] = []

    if "attempts" not in st.session_state:
        st.session_state["attempts"] = max_attempts

    if "input_number" not in st.session_state:
        st.session_state["input_number"] = 0

    # PLAY AGAIN FUNCTION
    def play_again():

        # Choose a new word
        new_word = random.choice(words)

        while (
            new_word == st.session_state["word"]
            and len(words) > 1
        ):
            new_word = random.choice(words)

        # Reset word
        st.session_state["word"] = new_word

        # Reset guessed letters
        st.session_state["guessed"] = []

        # Reset attempts according to difficulty
        st.session_state["attempts"] = max_attempts

        # CHANGE INPUT KEY
        # This automatically clears the old text input
        st.session_state["input_number"] += 1

        # Immediately restart
        st.rerun()

    # GET CURRENT GAME DATA
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
        key=f"guess_input_{st.session_state['input_number']}"
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

                st.warning(
                    "You've already guessed that letter."
                )

            else:

                guessed.append(guess)

                if guess in word:

                    st.success(
                        f"Correct! '{guess}' is in the word."
                    )

                    positions = [
                        i
                        for i, character in enumerate(word)
                        if character == guess
                    ]

                    st.write(
                        f"Position(s): {positions}"
                    )

                else:

                    st.error(
                        f"No! '{guess}' is not in the word."
                    )

                    st.session_state["attempts"] -= 1

                st.rerun()

        else:

            st.warning(
                "Please enter ONE alphabet character."
            )

    # CHECK WIN
    if all(character in guessed for character in word):

        st.success(
            f"You won! The word was **{word}**"
        )

        if st.button("Play Again"):
            play_again()

    # CHECK GAME OVER
    elif st.session_state["attempts"] <= 0:

        st.error(
            f"GAME OVER! The word was **{word}**"
        )

        if st.button("Play Again"):
            play_again()


hangman()


# import streamlit as st

# st.title("Choose Your Hobbies")

# football = st.checkbox("Football")
# coding = st.checkbox("Coding")
# gaming = st.checkbox("Gaming")

# if football:
#     st.write("You selected Football ⚽")

# if coding:
#     st.write("You selected Coding 💻")

# if gaming:
#     st.write("You selected Gaming 🎮")
