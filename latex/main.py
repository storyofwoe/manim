from manim import *

class LatexTest(Scene):
    def construct(self):
        tex1 = MathTex(r"12x^2 + 17x -5 = 0")
        tex2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        tex3 = MathTex(r"x = \frac{-17 \pm \sqrt{17^2 - 4 \cdot 12 \cdot -5}}{2 \cdot 12}")
        tex4 = MathTex(r"x = \frac{-17 \pm \sqrt{529}}{24}")
        tex5 = MathTex(r"x = -\frac{17}{24} \pm \frac{23}{24}")
        tex6 = MathTex(r"x_1 = \frac{6}{24}")
        tex7 = MathTex(r"x_2 = -\frac{40}{24}")
        tex8 = MathTex(r"x_1 = \frac{1}{4}")
        tex9 = MathTex(r"x_2 = -\frac{5}{3}")
        tex10 = MathTex(r"x_1 = \frac{1}{4},")


        self.wait(0.5)
        self.play(Create(tex1), run_time = 2)
        self.play(tex1.animate.move_to(UP * 3))

        box = SurroundingRectangle(tex1, color = WHITE, buff = MED_LARGE_BUFF)

        self.play(Create(box))
        self.play(Create(tex2), run_time = 2)

        self.play(ReplacementTransform(tex2, tex3), run_time = 2)
        self.wait(0.5)
        self.play(ReplacementTransform(tex3, tex4), run_time = 2)
        self.wait(0.5)
        self.play(ReplacementTransform(tex4, tex5), run_time = 2)
        self.wait(0.5)
        
        tex6.shift(DOWN + 2 * LEFT)
        tex7.shift(DOWN + 2 * RIGHT)

        self.play(Create(tex6), Create(tex7))
        self.play(Uncreate(tex5))
        self.wait(0.5)

        tex8.move_to(tex6.get_center())
        tex9.move_to(tex7.get_center())

        self.play(
            ReplacementTransform(tex6, tex8),
            ReplacementTransform(tex7, tex9)
        )

        self.play(
            tex8.animate.shift(UP + RIGHT),
            tex9.animate.shift(UP + LEFT)
        )

        tex10.move_to(tex8.get_center())

        self.play(ReplacementTransform(tex8, tex10))


        # self.play(tex2.animate.next_to(box, DOWN))
        # self.play(Create(tex3), run_time = 2)

        self.wait(0.5)

# How to animate an equation changing in Manim?
# https://manimclass.com/manim-latex/