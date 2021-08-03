import turtle
import pandas

IMAGE_PATH = "blank_states_img.gif"
CSV_PATH = "india_states.csv"

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(height=1000, width=1000)

screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

writer_turtle = turtle.Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()

states_data_frame = pandas.read_csv(filepath_or_buffer=CSV_PATH)

remaining_states_list = states_data_frame["state"].to_list()
total_num_states = len(remaining_states_list)
guessed_num_states = 0
is_game_ongoing = True

while is_game_ongoing:
    answer_state = screen.textinput(title=f"{guessed_num_states}/{total_num_states} States Correct",
                                    prompt="What is another State's name?").title()

    if answer_state in remaining_states_list:
        remaining_states_list.remove(answer_state)
        guessed_num_states += 1

        answer_state_dataframe = states_data_frame[states_data_frame.state == answer_state]
        x_coordinate = float(answer_state_dataframe.x)
        y_coordinate = float(answer_state_dataframe.y)

        writer_turtle.goto(x=x_coordinate, y=y_coordinate)
        writer_turtle.write(answer_state, font=("Arial", 10, "normal"), align="center")

        if guessed_num_states == total_num_states:
            is_game_ongoing = False


screen.exitonclick()
