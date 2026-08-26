import random
import streamlit as st


def guess_number():
    st.title("🎯 Guess the Number Game")

    # Create session variables
    if "randomNumber" not in st.session_state:
        st.session_state.randomNumber = random.randint(1, 20)

    if "attempts" not in st.session_state:
        st.session_state.attempts = 10

    if "name" not in st.session_state:
        st.session_state.name = ""

    if "score_sheet" not in st.session_state:
        st.session_state.score_sheet = {}

    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    # Get player's name
    name = st.text_input(
        "Enter your name",
        value=st.session_state.name
    )

    if name:
        st.session_state.name = name
        st.write(f"Hola, {name}! 👋")

    # Number input
    guess = st.number_input(
        "Enter a number between 1 and 20",
        min_value=1,
        max_value=20,
        step=1
    )

    # Guess button
    if st.button("Guess 🎯"):

        if st.session_state.game_over:
            st.warning("The game is over. Click 'Play Again' to start a new game.")

        else:
            randomNumber = st.session_state.randomNumber

            if guess > randomNumber:
                st.session_state.attempts -= 1
                st.warning("⬆️ Too High!")
                st.write(
                    f"You have {st.session_state.attempts} attempts left."
                )

            elif guess < randomNumber:
                st.session_state.attempts -= 1
                st.warning("⬇️ Too Low!")
                st.write(
                    f"You have {st.session_state.attempts} attempts left."
                )

            else:
                st.success(
                    f"🎉 Congratulations {name}! "
                    f"You got the number {randomNumber}!"
                )

                st.session_state.score_sheet[name] = "completed"
                st.session_state.game_over = True

                st.write("### Score Sheet")
                st.write(st.session_state.score_sheet)

            # Check if attempts have finished
            if st.session_state.attempts == 0:
                st.error(
                    f"💀 Game Over! The number was {randomNumber}."
                )

                st.session_state.score_sheet[name] = "failed"
                st.session_state.game_over = True

                st.write("### Score Sheet")
                st.write(st.session_state.score_sheet)

    # Play again button
    if st.session_state.game_over:

        if st.button("🔄 Play Again"):

            st.session_state.randomNumber = random.randint(1, 20)
            st.session_state.attempts = 10
            st.session_state.game_over = False

            st.rerun()


guess_number()
