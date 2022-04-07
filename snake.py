from turtle import Turtle

# Starting position to start and measures in angles to move the snake
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # self.head contains the head of the snake which is the main element that checks such as collisions with elements
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        """
        Creation of new snake segment that add to the head
        :param position: position of the new segment
        """
        new_snake_segment = Turtle("square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)

    def extend(self):
        """
        Add new snake's segment
        """
        self.add_segments(self.segments[-1].position())

    def move(self):
        """
        Management of the movement of the snake and its segments
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.head.forward(MOVE)

    def reset(self):
        """
        New game
        """
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

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
