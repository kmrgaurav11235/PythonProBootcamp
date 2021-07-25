from turtle import Turtle

# Constants
TURTLE_WIDTH = 20
NUM_SEGMENTS = 3
MOVE_DISTANCE = 20


# Snake body: we will create 3 turtles as squares -- lined up with each other.
# Body of a turtle is 20px * 20px -- centered at (0, 0) by default
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for index in range(NUM_SEGMENTS):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            turtle_x_coordinate = index * TURTLE_WIDTH * -1
            new_turtle.setposition(x=turtle_x_coordinate, y=0)
            self.snake_segments.append(new_turtle)

    def move(self):
        # Instead of just moving all three segments forward, we will do this:
        # 1. Move the 3rd segment to where the 2nd segment was.
        # 2. Move the 2nd segment to where the 1st segment was.
        # 3. Move the 1st segment forward.
        # This will allow our snake to make turns correctly
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            # start = last segment, stop = 0, range = -1
            new_x = self.snake_segments[segment_num - 1].xcor()
            new_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)

        self.snake_segments[0].forward(MOVE_DISTANCE)
