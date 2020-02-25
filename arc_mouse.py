"""
Check for a mouse click on a circle.

-Draw a circle somewhere, using circle x and circle y variables and radius
-Use mouse_pressed event handler to register a click
"""

import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here
Obj_1_x = 0.5 * WIDTH
Obj_1_y = 0.5 * HEIGHT
circle_radius = 100


@window.event("on_draw")
def game_loop():
    # global here
    global Obj_1_x
    global Obj_1_y
    global circle_radius

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(Obj_1_x, Obj_1_y, circle_radius, arcade.color.XANADU)


@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
    print(f"Your mouse is at ({mouse_x}, {mouse_y})")


arcade.run()
