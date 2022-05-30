from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        for num_segments in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.back(20*(num_segments) + 1)
            self.segments.append(new_segment)
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_num].goto(self.segments[segment_num - 1].pos())
        self.segments[0].forward(20)