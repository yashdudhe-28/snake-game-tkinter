# Snake Game

A classic Snake game built with Python and Tkinter, featuring smooth controls and score tracking.

## Features

- Classic snake gameplay
- Arrow key controls
- Score tracking
- Collision detection
- Food spawning
- Game over screen
- Clean and modern interface

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)

## Installation

1. Make sure you have Python installed on your system
2. Clone or download this repository
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```
   python snake_game.py
   ```

2. Game Controls:
   - Use arrow keys to control the snake's direction
   - Up Arrow: Move up
   - Down Arrow: Move down
   - Left Arrow: Move left
   - Right Arrow: Move right

3. Game Rules:
   - Eat the red food to grow and increase your score
   - Avoid hitting the walls
   - Avoid hitting your own body
   - The snake moves continuously
   - Game ends when you collide with walls or yourself

## Game Features

- Smooth snake movement
- Real-time score display
- Random food spawning
- Collision detection
- Game over screen with final score
- Prevents 180-degree turns

## Game Settings

The game can be customized by modifying these constants in the code:
- `GAME_WIDTH`: Width of the game window (default: 600)
- `GAME_HEIGHT`: Height of the game window (default: 400)
- `SPEED`: Game speed in milliseconds (default: 100)
- `SPACE_SIZE`: Size of snake segments and food (default: 20)
- `BODY_PARTS`: Initial snake length (default: 3)
- `SNAKE_COLOR`: Color of the snake (default: green)
- `FOOD_COLOR`: Color of the food (default: red)
- `BACKGROUND_COLOR`: Color of the background (default: black)

## Future Improvements

Potential features for future versions:
- Multiple difficulty levels
- High score tracking
- Sound effects
- Power-ups
- Different themes
- Pause functionality
- Start menu
- Mobile touch controls 