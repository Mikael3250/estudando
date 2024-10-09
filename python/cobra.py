import tkinter as tk
import random

# Configurações principais
SIZE = 20
WIDTH, HEIGHT = 400, 400

def move_snake():
    x, y = snake[0]
    dx, dy = directions[dir]
    new_head = (x + dx * SIZE, y + dy * SIZE)
    snake.insert(0, new_head)
    if new_head == food:
        place_food()
    else:
        snake.pop()
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT or new_head in snake[1:]:
        return game_over()
    draw_snake()
    root.after(100, move_snake)

def change_dir(event):
    global dir
    dir = {'Up': 'U', 'Down': 'D', 'Left': 'L', 'Right': 'R'}[event.keysym]

def draw_snake():
    canvas.delete("all")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green")
    canvas.create_rectangle(food[0], food[1], food[0] + SIZE, food[1] + SIZE, fill="red")

def place_food():
    global food
    food = (random.randint(0, (WIDTH // SIZE) - 1) * SIZE, random.randint(0, (HEIGHT // SIZE) - 1) * SIZE)

def game_over():
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))

# Inicializando o jogo
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
snake = [(WIDTH // 2, HEIGHT // 2)]
dir = 'R'
place_food()
root.bind("<KeyPress>", change_dir)
move_snake()
root.mainloop()
