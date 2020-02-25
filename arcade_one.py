import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.WHITE)

# Initialize your variables here

position_x_obj1 = 0
position_y_obj1 = 0
Determine_X = 0
Determine_Y = 0
speed = 30
size = 0
minSize = 10
size_det = 0
maxSize = 100
size_second = 0
expansionRate = 10
Opp_x = 0
Opp_y = 0
third_x = 0
third_y = 0
fourth_x = 0
fourth_y = 0


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global WIDTH
    global HEIGHT
    global position_x_obj1
    global position_y_obj1
    global Determine_X
    global Determine_Y
    global speed
    global size
    global maxSize
    global minSize
    global expansionRate
    global size_det
    global Opp_x
    global Opp_y
    global size_second
    global third_x
    global third_y
    global fourth_x
    global fourth_y
    global Min_Half

    # update your variables here.

    if size <= minSize:
        size += expansionRate
        size_det = 1

    if size > minSize and size_det == 0:
        size -= expansionRate

    if size < maxSize and size_det == 1:
        size += expansionRate

    if size >= maxSize:
        size -= expansionRate
        size_det = 0

    if position_x_obj1 > 0 and Determine_X == 1:
        position_x_obj1 -= speed

    if position_y_obj1 > 0 and Determine_Y == 1:
        position_y_obj1 -= speed

    if position_x_obj1 < WIDTH and Determine_X == 0:
        position_x_obj1 += speed

    if position_y_obj1 < HEIGHT and Determine_Y == 0:
        position_y_obj1 += speed

    if position_y_obj1 >= HEIGHT and Determine_Y == 0:
        Determine_Y = 1

    if position_x_obj1 >= WIDTH and Determine_X == 0:
        Determine_X = 1

    if position_y_obj1 <= 0 and Determine_Y == 1:
        Determine_Y = 0

    if position_x_obj1 <= 0 and Determine_X == 1:
        Determine_X = 0
    
    size_second = maxSize - size

    Opp_x = ((0.5 * WIDTH) - position_x_obj1) + (0.5 * WIDTH)
    Opp_y = ((0.5 * HEIGHT) - position_y_obj1) + (0.5 * HEIGHT)

    third_x = position_x_obj1
    fourth_y = position_y_obj1

    third_y = ((0.5 * HEIGHT) - position_y_obj1) + (0.5 * HEIGHT)
    fourth_x = ((0.5 * WIDTH) - position_x_obj1) + (0.5 * WIDTH)

    # Draw things here.
    arcade.start_render()

    arcade.draw_circle_filled(WIDTH * 0.5, HEIGHT * 0.5, min(0.5 * WIDTH, 0.5 * HEIGHT), arcade.color.CANDY_APPLE_RED)

    arcade.draw_circle_filled(third_x, third_y, size_second, arcade.color.BLACK)

    arcade.draw_circle_filled(fourth_x, fourth_y, size, arcade.color.BLACK)

    # arcade.draw_line(position_x_obj1, position_y_obj1, Opp_x, Opp_y, arcade.color.BLACK, size - 50)

    # arcade.draw_line(third_x, third_y, fourth_x, fourth_y, arcade.color.BLACK, size - 50)

    arcade.draw_circle_filled(position_x_obj1, position_y_obj1, size, arcade.color.BLACK)

    arcade.draw_circle_filled(Opp_x, Opp_y, size_second, arcade.color.BLACK)

arcade.run()
