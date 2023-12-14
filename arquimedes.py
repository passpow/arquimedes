from manim import *

class Arquimedes(Scene):
    def construct(self):
        passpow = Text('passpow', font="Monospace").scale(1).to_corner(DR)
        self.play(Write(passpow))
        circle = Circle(radius=3)
        circle.set_fill(color=BLUE, opacity=0.5)
        self.play(Create(circle))
        for i in range(3,15):
            poly=RegularPolygon(n=i, color=RED, radius=3)
            poly.set_fill(color=RED, opacity=0.5)
            self.play(Create(poly), run_time=0.7)
            self.play(FadeOut(poly))
