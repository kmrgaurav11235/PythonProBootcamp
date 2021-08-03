import turtle

IMAGE_PATH = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(height=1000, width=1000)

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

answer_state = screen.textinput(title="Guess the state", prompt="What is another State's name?")

screen.exitonclick()
