from manim import *

class CircleCreator(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        #circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        self.wait(3)
