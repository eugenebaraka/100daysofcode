import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TURN_ANGLE = 90
class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()


    def create_body(self):

        for position in STARTING_POSITIONS:
            segment = turtle.Turtle(shape="square")
            segment.color("white")
            segment.penup() # prevent drawing line as they move
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # get second to last's segment position
            new_y = self.segments[seg_num - 1].ycor() # get second to last's segment position
            # move the segment to the second to last's position
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].left(TURN_ANGLE) # turn the first segment
        self.segments[0].forward(MOVE_DISTANCE) # move the first segment forward

    def down(self):
        self.segments[0].right(TURN_ANGLE)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        self.segments[0].backward(MOVE_DISTANCE)
