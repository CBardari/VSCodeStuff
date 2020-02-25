import arcade
import math

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here
x = WIDTH // 2
y = HEIGHT // 2
Radius = 50


@window.event("on_draw")
def game_loop():
    # import global variables here.

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(x, y, Radius, arcade.color.XANADU)


@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
    global Radius
    global x
    global y
    print(f"Your mouse is at ({mouse_x}, {mouse_y})")
    # math
    # side_a = max(x - mouse_x, mouse_x - x)
    side_a = x - mouse_x
    if side_a < 0:
        side_a *= (-1)
    # side_b = max(y - mouse_y, mouse_y - y)
    side_b = y - mouse_y
    if side_b < 0:
        side_b *= (-1)
    distance = math.sqrt((side_a ^ 2) + (side_b * side_b))
    # math
    if distance <= Radius:
        Radius += 1
        print(f"{distance} and {Radius}")
    else:
        print(f"{distance} and {Radius}")


arcade.run()
