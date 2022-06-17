from turtle import Turtle
starting_position = (0, 0)
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for num_segments in range(3):
            self.add_segment(starting_position)
    
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_num].goto(self.segments[segment_num - 1].pos())
        self.head.forward(move_distance)
    
    def move_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
        
    def move_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
        
    def move_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        
    def move_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].pos())