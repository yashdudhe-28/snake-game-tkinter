import tkinter as tk
from tkinter import ttk, messagebox
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Game constants
        self.GAME_WIDTH = 600
        self.GAME_HEIGHT = 400
        self.SPEED = 100
        self.SPACE_SIZE = 20
        self.BODY_PARTS = 3
        self.SNAKE_COLOR = "#00FF00"
        self.FOOD_COLOR = "#FF0000"
        self.BACKGROUND_COLOR = "#000000"
        
        # Game variables
        self.direction = 'right'
        self.score = 0
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)
        
        # Create score label
        self.score_label = ttk.Label(
            self.main_frame,
            text=f"Score: {self.score}",
            font=("Arial", 14)
        )
        self.score_label.pack()
        
        # Create game canvas
        self.canvas = tk.Canvas(
            self.main_frame,
            width=self.GAME_WIDTH,
            height=self.GAME_HEIGHT,
            bg=self.BACKGROUND_COLOR
        )
        self.canvas.pack()
        
        # Initialize game
        self.snake_positions = []
        self.food_position = []
        self.snake_body = []
        
        # Bind keys
        self.root.bind('<Left>', lambda event: self.change_direction('left'))
        self.root.bind('<Right>', lambda event: self.change_direction('right'))
        self.root.bind('<Up>', lambda event: self.change_direction('up'))
        self.root.bind('<Down>', lambda event: self.change_direction('down'))
        
        # Start game
        self.start_game()
        
    def start_game(self):
        # Create snake
        for i in range(self.BODY_PARTS):
            x = self.SPACE_SIZE * (self.BODY_PARTS - i)
            y = self.SPACE_SIZE
            self.snake_positions.append([x, y])
            square = self.canvas.create_rectangle(
                x, y,
                x + self.SPACE_SIZE,
                y + self.SPACE_SIZE,
                fill=self.SNAKE_COLOR,
                tags="snake"
            )
            self.snake_body.append(square)
            
        # Create food
        self.spawn_food()
        
        # Start moving
        self.move()
        
    def spawn_food(self):
        # Remove old food
        if self.food_position:
            self.canvas.delete("food")
            
        # Create new food
        x = random.randint(0, (self.GAME_WIDTH - self.SPACE_SIZE) // self.SPACE_SIZE) * self.SPACE_SIZE
        y = random.randint(0, (self.GAME_HEIGHT - self.SPACE_SIZE) // self.SPACE_SIZE) * self.SPACE_SIZE
        
        self.food_position = [x, y]
        self.canvas.create_oval(
            x, y,
            x + self.SPACE_SIZE,
            y + self.SPACE_SIZE,
            fill=self.FOOD_COLOR,
            tags="food"
        )
        
    def move(self):
        # Get current head position
        head = self.snake_positions[0].copy()
        
        # Update head position based on direction
        if self.direction == 'left':
            head[0] -= self.SPACE_SIZE
        elif self.direction == 'right':
            head[0] += self.SPACE_SIZE
        elif self.direction == 'up':
            head[1] -= self.SPACE_SIZE
        elif self.direction == 'down':
            head[1] += self.SPACE_SIZE
            
        # Add new head
        self.snake_positions.insert(0, head)
        
        # Create new head square
        square = self.canvas.create_rectangle(
            head[0], head[1],
            head[0] + self.SPACE_SIZE,
            head[1] + self.SPACE_SIZE,
            fill=self.SNAKE_COLOR
        )
        self.snake_body.insert(0, square)
        
        # Check for food collision
        if head == self.food_position:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.spawn_food()
        else:
            # Remove tail
            self.snake_positions.pop()
            self.canvas.delete(self.snake_body.pop())
            
        # Check for collisions
        if self.check_collisions():
            self.game_over()
        else:
            # Continue moving
            self.root.after(self.SPEED, self.move)
            
    def check_collisions(self):
        head = self.snake_positions[0]
        
        # Check wall collision
        if (head[0] < 0 or head[0] >= self.GAME_WIDTH or
            head[1] < 0 or head[1] >= self.GAME_HEIGHT):
            return True
            
        # Check self collision
        for body_part in self.snake_positions[1:]:
            if head == body_part:
                return True
                
        return False
        
    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(
            self.canvas.winfo_width() / 2,
            self.canvas.winfo_height() / 2,
            text=f"Game Over! Score: {self.score}",
            font=("Arial", 20),
            fill="red"
        )
        
    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        if (new_direction == 'left' and self.direction != 'right' or
            new_direction == 'right' and self.direction != 'left' or
            new_direction == 'up' and self.direction != 'down' or
            new_direction == 'down' and self.direction != 'up'):
            self.direction = new_direction

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGame(root)
    root.mainloop() 