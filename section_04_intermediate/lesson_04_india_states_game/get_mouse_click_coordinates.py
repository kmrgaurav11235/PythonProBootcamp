import turtle


def get_mouse_click_coordinate(x, y):
    print(x, y)


IMAGE_PATH = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(height=1000, width=1000)

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

turtle.onscreenclick(get_mouse_click_coordinate)

turtle.mainloop()