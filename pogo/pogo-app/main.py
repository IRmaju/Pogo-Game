import streamlit as st
import time
import random

# Game Setup
st.title("Pong Game")
st.write("Control the paddles with buttons. Player 1 is on the left, Player 2 is on the right.")

# Initialize player scores
player_1_score = 0
player_2_score = 0

# Ball movement variables
ball_x = 0
ball_y = 0
ball_dx = 0.2  # Horizontal speed
ball_dy = -0.2  # Vertical speed

# Paddle positions
paddle_1_y = 0  # Player 1 paddle position (Y axis)
paddle_2_y = 0  # Player 2 paddle position (Y axis)

# Initialize score display
score_display = st.empty()

# Function to update the game state
def update_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_1_y, paddle_2_y, player_1_score, player_2_score

    # Update Ball Position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_y > 290:
        ball_y = 290
        ball_dy *= -1  # Bounce back
    if ball_y < -290:
        ball_y = -290
        ball_dy *= -1  # Bounce back

    # Ball collision with paddles
    if (ball_x > 340 and ball_x < 350) and (ball_y < paddle_2_y + 50 and ball_y > paddle_2_y - 50):
        ball_x = 340
        ball_dx *= -1  # Reverse direction for right paddle

    if (ball_x < -340 and ball_x > -350) and (ball_y < paddle_1_y + 50 and ball_y > paddle_1_y - 50):
        ball_x = -340
        ball_dx *= -1  # Reverse direction for left paddle

    # Ball out of bounds (reset)
    if ball_x > 390:
        player_1_score += 1
        ball_x = 0
        ball_y = 0
        ball_dx = random.choice([0.2, -0.2])
        ball_dy = random.choice([0.2, -0.2])
        
    elif ball_x < -390:
        player_2_score += 1
        ball_x = 0
        ball_y = 0
        ball_dx = random.choice([0.2, -0.2])
        ball_dy = random.choice([0.2, -0.2])

# Streamlit UI controls
# Player 1 paddle control (Left)
paddle_1_up = st.button("Player 1 Up", key="up1")
paddle_1_down = st.button("Player 1 Down", key="down1")

# Player 2 paddle control (Right)
paddle_2_up = st.button("Player 2 Up", key="up2")
paddle_2_down = st.button("Player 2 Down", key="down2")

# Adjust paddle movement based on button presses
if paddle_1_up:
    paddle_1_y = min(250, paddle_1_y + 20)
if paddle_1_down:
    paddle_1_y = max(-250, paddle_1_y - 20)

if paddle_2_up:
    paddle_2_y = min(250, paddle_2_y + 20)
if paddle_2_down:
    paddle_2_y = max(-250, paddle_2_y - 20)

# Main Game Loop
while True:
    update_game()

    # Display Score
    score_display.text(f"Player 1 Score: {player_1_score}  |  Player 2 Score: {player_2_score}")

    # Simulate Ball Movement (Drawing)
    st.write(f"Ball position: ({ball_x:.2f}, {ball_y:.2f})")

    # Display Paddle and Ball Positions
    st.write(f"Player 1 Paddle: {paddle_1_y} | Player 2 Paddle: {paddle_2_y}")
    
    # Refresh the screen every 0.05 seconds (to create a game loop)
    time.sleep(0.05)

    # Stop the game after a condition (like after some time or score limit)
    if player_1_score >= 5 or player_2_score >= 5:
        st.write("Game Over!")
        break

