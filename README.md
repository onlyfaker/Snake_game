# 🐍 Snake Game 🎮

A classic Snake game built using Python's Turtle graphics module. Navigate the snake to eat food, grow longer, and avoid collisions with the walls and your own tail.

## ✨ Features

- 🕹️ Responsive snake movement controlled by arrow keys
- 🍏 Food spawns at random locations
- 🏆 Score tracking as you eat food
- ⚠️ Game over detection when hitting walls or your own tail
- 📈 Snake grows longer with each food eaten
- 🎨 Smooth animations and clean visual design

## 🎲 How to Play

1. Run the game using Python
2. Control the snake with the arrow keys (Up, Down, Left, Right)
3. Eat the green food to grow longer and increase your score
4. Avoid hitting the walls or your own tail
5. Try to achieve the highest score possible!

## 📁 Project Structure

- `main.py` - The main game loop and setup
- `snake.py` - Contains the Snake class that handles snake behavior and movement
- `food.py` - Contains the Food class that manages food generation
- `scoreboard.py` - Contains the Scoreboard class for score tracking and game over display

## 🔧 Implementation Details

### Snake Class
The snake is built as a series of connected segments with the following features:
- Movement in four directions
- Prevention of 180° turns (can't immediately reverse direction)
- Detection of food collision
- Growth mechanics when food is eaten

### Food Class
Food is implemented with these characteristics:
- Random spawning anywhere on the screen
- Visual representation as a small green circle
- Repositioning when eaten by the snake

### Scoreboard Class
The scoreboard handles:
- Real-time score display
- Game over message when the game ends

## 🚀 Upcoming Features

- 🏅 High score table that appears when the game is over

## 📋 Requirements

- Python 3.x
- Python Turtle module (included in standard library)

## 🎯 Running the Game

```bash
python main.py
```

## 🎛️ Controls

- ⬆️ Up Arrow: Move Up
- ⬇️ Down Arrow: Move Down
- ⬅️ Left Arrow: Move Left  
- ➡️ Right Arrow: Move Right

## 📜 Game Rules

1. Each food eaten increases your score by 1
2. The game ends if you hit a wall
3. The game ends if you hit your own tail
4. The snake moves at a constant speed

## 💫 Credits

Created as a Python learning project. 🐍❤️
