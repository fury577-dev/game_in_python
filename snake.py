import random
import os
import time

WIDTH = 20
HEIGHT = 10

snake = [(5, 5)]
direction = "RIGHT"
food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print("O", end="")
            elif (x, y) == food:
                print("X", end="")
            elif x == 0 or x == WIDTH-1 or y == 0 or y == HEIGHT-1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print(f"Score: {score}")
    print("Controls: W A S D | Ctrl+C to quit")

def move_snake():
    global food, score
    head_x, head_y = snake[0]

    if direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    else:
        new_head = (head_x + 1, head_y)

    if (
        new_head in snake or
        new_head[0] == 0 or new_head[0] == WIDTH-1 or
        new_head[1] == 0 or new_head[1] == HEIGHT-1
    ):
        print("\nGame Over!")
        print(f"Final Score: {score}")
        exit()

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
    else:
        snake.pop()

def game_loop():
    global direction
    try:
        while True:
            draw()
            move_snake()
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nGame exited.")

if __name__ == "__main__":
    game_loop()
