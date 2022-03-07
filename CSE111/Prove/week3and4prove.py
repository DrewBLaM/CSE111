# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from Prove.draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, 300, 350)
    draw_cloud(canvas, 600, 300)
    draw_moon(canvas, 50, 300)
    draw_tree(canvas, 500, 120)


    #Grass
    for i in range(5000):
        x = random.randint(0, scene_width)
        y = random.randint(0, scene_height / 4)
        draw_grass(canvas, x, y)
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, width=0, fill = "midnightblue")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 4, width=0, fill = "saddle brown")

def draw_cloud(canvas):
    draw_oval(canvas, 150, 250, 250, 200, fill = "white")

def draw_grass(canvas, x, y):
    draw_rectangle(canvas, x, y, x + 2, y + 20, outline="darkGreen", fill="green")


def draw_tree(canvas, x, y):
    #trunk
    draw_rectangle(canvas, x, y, x + 20, y + 200, outline="Sienna4", fill="Sienna4")
    #leaves
    for i in range(15):
        rand_x = random.randint(x - 80, x + 5)
        rand_y = random.randint(y + 150, y + 220)
        draw_oval(canvas, rand_x, rand_y, rand_x + 100, rand_y + 30, outline = "green", fill = "green")

def draw_cloud(canvas, x, y):
    for i in range(5):
        rand_x = random.randint(x, x + 50)
        rand_y = random.randint(y, y + 60)
        draw_oval(canvas, rand_x, rand_y, rand_x + 100, rand_y + 20, outline = "floralwhite", fill = "floralwhite")

def draw_moon(canvas, x, y):
    draw_oval(canvas, x, y, x+150, y+150, outline = "midnightblue", fill="palegoldenrod")
    draw_oval(canvas, x + 30, y + 30, x + 180, y + 180, outline = "midnightblue", fill="midnightblue")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()