from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() #creates a circle
        circle.set_fill(PINK, opacity = 0.5) #sets colour and transparency

        square = Square() #creates a square
        square.rotate(PI / 4) #rotates the square

        self.play(Create(square)) #animates the creation of the square
        self.play(Transform(square, circle)) #interpolate the square into the circle
        self.play(FadeOut(square)) #fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square)) #show square on screen
        self.play(square.animate.rotate(PI / 4)) #rotate square
        self.play(Transform(square, circle))
        self.play(
            square.animate.set_fill(PINK, opacity = 0.5)
        )

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()
        square.set_fill(BLUE, opacity = 0.5)

        square.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square))

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)
        self.replacement_transform()

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        self.add(Dot())
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))
