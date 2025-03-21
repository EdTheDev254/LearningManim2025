from manim import *

class CircleCreator(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        #circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        self.wait(3)

class SquareCreator(Scene):
    def construct(self):
        square = Square(color=GREEN)
        self.play(Create(square))
        self.wait(3)


class TransformToCircle(Scene):
    def construct(self):
        square = Square(color=GREEN)
        circle = Circle(color=BLUE)
        new_square = square.copy()

        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)
        self.play(Transform(square, new_square))
        self.play(FadeOut(square))
        self.wait(1)


class PositioningObjects(Scene):
    def construct(self):
        square = Square(color=GREEN)
        circle = Circle(color=BLUE)

        self.play(Create(square))
        self.wait(1)
        circle.next_to(square, RIGHT)
        self.play(Create(circle))
        self.wait(1)
        self.play(circle.animate.move_to(square.get_center()))
        self.wait(1)
        self.play(circle.animate.scale(0.2))
        self.wait(1)
        self.play(square.animate.rotate_about_origin(PI/4))
        self.wait(0.5)
        self.play(square.animate.scale(0.5))
        self.wait(1)
        self.play(square.animate.rotate_about_origin(-PI/4))
        self.wait(1)  



