import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0] # head of the snake


    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()  # prevent drawing line as they move
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # get second to last's segment position
            new_y = self.segments[seg_num - 1].ycor() # get second to last's segment position
            # move the segment to the second to last's position
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000) # send the old snake to the location outside the screen
        self.segments.clear()
        self.create_body()
        self.head = self.segments[0] # head of the snake

