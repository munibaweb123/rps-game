import streamlit as st

# Mapping of choices
choices = {"✊": "Rock", "✋": "Paper", "✌": "Scissors"}

def get_winner(player1, player2):
    """Determine the winner based on game rules."""
    if player1 == player2:
        return "It's a tie! 🤝"
    elif (choices[player1] == "Rock" and choices[player2] == "Scissors") or \
         (choices[player1] == "Scissors" and choices[player2] == "Paper") or \
         (choices[player1] == "Paper" and choices[player2] == "Rock"):
        return "🎉 Player 1 Wins!"
    else:
        return "🎉 Player 2 Wins!"

def main():
    st.title("✊✋✌ Rock, Paper, Scissors Game")

    st.write("# 🤷Player 1, choose your move:")
    player1 = st.selectbox("Player 1", list(choices.keys()))

    st.write("# 🤷Player 2, choose your move:")
    player2 = st.selectbox("Player 2", list(choices.keys()))

    if st.button("Play! 🎮"):
        result = get_winner(player1, player2)
        st.subheader(result)

    st.write("💡 Select your emoji and press **Play!** to see the winner.")

if __name__ == "__main__":
    main()
