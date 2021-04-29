from manim import *
from typing_extensions import runtime
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                   # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class TextAni(Scene):
    def construct(self):
        square2 = Square()
        c1 = Circle(color=BLUE)
        square2.set_fill(GREEN_D, opacity=0.8)
        square2.set_stroke(ORANGE, width=5)
        text = Text("MANIM")
        text.set_color_by_gradient(GREEN, BLUE, RED)
        text.scale(5)
        equa = MathTex(" \sin^2 \\theta + \cos^2 \\theta = 1").scale(3)
        self.play(Create(text, run_time=3))
        self.play(Transform(text, square2, run_time=2))
        self.wait(1.5)
        self.play(Transform(text, equa, run_time=2))
        self.wait(3)
        self.play(Transform(text, c1, run_time=2))
        self.wait()

class TestG(GraphScene):
    def __init__(self, **kwargs):
      GraphScene.__init__(
          self,
          x_min = -5 * PI,
          x_max= 5 * PI,
          y_min= -3,
          y_max= 3,
          graph_origin= ORIGIN,
          **kwargs
      )
    def construct(self):
        self.setup_axes(animate=True)
        self.wait(3)
      
    