from turtle import Turtle
class Snake:

    MOVE_DISTANCE = 20

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        POSITIONS = [(-40,0), (20, 0), (0, 0)]
        for position in POSITIONS:
            self.add_segment(position)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def add_segment(self, position):
        segment = Turtle("circle")
        segment.color("white")
        segment.penup()
        segment.goto(position[0], position[1])
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
