import random
import streamlit as st


def guessing_number():

    st.title("GUESS THE NUMBER GAME")

    name = st.text_input(
        "Enter your name:",
        key="gn_name"
    )

    if name:
        st.write(f"Hola, {name}!")

    # Secret number
    if "gn_secret_number" not in st.session_state:
        st.session_state["gn_secret_number"] = random.randint(1, 20)

    # Attempts
    if "gn_attempts" not in st.session_state:
        st.session_state["gn_attempts"] = 10

    # Score sheet
    if "gn_score_sheet" not in st.session_state:
        st.session_state["gn_score_sheet"] = {}

    # Game status
    if "gn_game_over" not in st.session_state:
        st.session_state["gn_game_over"] = False


    # If game has ended
    if st.session_state["gn_game_over"]:

        st.error("GAME ENDED!")

        if st.button("Play Again", key="gn_restart_after_end"):

            st.session_state["gn_secret_number"] = random.randint(1, 20)
            st.session_state["gn_attempts"] = 10
            st.session_state["gn_game_over"] = False

            st.rerun()

        return


    secret_number = st.session_state["gn_secret_number"]
    attempts = st.session_state["gn_attempts"]

    st.write(f"Attempts left: {attempts}")


    # User's guess
    guess = st.number_input(
        "Enter your guess (1 - 20):",
        min_value=1,
        max_value=20,
        step=1,
        key="gn_user_guess"
    )


    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        guess_button = st.button(
            "Guess",
            key="gn_guess_button"
        )

    with col2:
        end_button = st.button(
            "END GAME",
            key="gn_end_button"
        )


    # END GAME
    if end_button:

        st.session_state["gn_game_over"] = True

        st.rerun()


    # GUESS
    if guess_button:

        if guess == secret_number:

            st.success(
                f"🎉 Correct, {name}! "
                f"The number was {secret_number}."
            )

            score = attempts * 10

            if name:
                st.session_state["gn_score_sheet"][name] = score

            st.write(f"Your score: {score}")


            if st.button(
                "Play Again",
                key="gn_play_again_win"
            ):

                new_number = random.randint(1, 20)

                while new_number == secret_number:
                    new_number = random.randint(1, 20)

                st.session_state["gn_secret_number"] = new_number
                st.session_state["gn_attempts"] = 10

                st.rerun()


        else:

            st.session_state["gn_attempts"] -= 1

            if guess < secret_number:
                st.warning("Too low! Try again.")

            else:
                st.warning("Too high! Try again.")


            if st.session_state["gn_attempts"] <= 0:

                st.error(
                    f"GAME OVER! The number was {secret_number}."
                )


                if st.button(
                    "Play Again",
                    key="gn_play_again_lose"
                ):

                    new_number = random.randint(1, 20)

                    while new_number == secret_number:
                        new_number = random.randint(1, 20)

                    st.session_state["gn_secret_number"] = new_number
                    st.session_state["gn_attempts"] = 10

                    st.rerun()


    # Score sheet
    if st.session_state["gn_score_sheet"]:

        st.subheader("Score Sheet")

        for player, score in st.session_state["gn_score_sheet"].items():

            st.write(f"{player}: {score}")


guessing_number()
  

