# 🐍 Snake Game
A classic Snake Game built with Python’s turtle graphics module.
Control the snake, eat food to grow, and avoid collisions with the walls or your own tail. The longer you survive, the higher your score!

# 🎮 How It Works
1. When you start the game, a snake appears in the center of the screen.
2. Use the arrow keys to control the snake’s direction:
⬆️ Up – Move up
⬇️ Down – Move down
⬅️ Left – Move left
➡️ Right – Move right
3. The goal is to eat the red food that appears randomly on the screen.
4. Each time you eat food:
  - The snake grows longer
  - Your score increases
5. The game ends if:
  - The snake hits the wall
  - The snake collides with its own tail
  - When the game ends, a “Game Over” message appears on the screen.

# 🧩 Features
  - Smooth snake movement using time.sleep() and screen.update()
  - Automatic screen refresh for real-time animation
  - Collision detection with food, walls, and tail
  - Score tracking with live updates
  - Clean modular structure (separate classes for Snake, Food, and Scoreboard)

# ⚙️ Requirements
  - Python 3.7+
  - No external packages required (only uses built-in turtle and time modules)

# 🧠 Learning Concepts
This project demonstrates:
  - Object-Oriented Programming (OOP) in Python
  - Event handling with turtle.onkey()
  - Collision detection and coordinate tracking
  - Real-time screen updates using turtle.tracer() and screen.update()
  - Modular code design

# 💡 Future Improvements
  - Add a high score tracker that saves between sessions
  - Include levels or speed increase as the player progresses
  - Add background music or sound effects
  - Display a restart button when the game ends
