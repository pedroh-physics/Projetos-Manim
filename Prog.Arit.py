from manim import *

class PA(Scene):
    def construct(self):
        # Título e autor
        title = Text("Progressão Aritmética", font="Courier Prime", font_size=50)
        author = Text("@manual.fisica", font="Courier Prime", font_size=20).to_edge(DOWN)
        self.play(Write(title))
        self.play(Write(author))

        # Escreve a PA e mostra o comportamento da razão
        pa = MathTex("a_1", "a_2", "a_3", "\cdots", "a_{n-1}", "a_n").space_out_submobjects(3)
        self.play(Transform(title, pa))

        arrow1 = Arrow(pa[0].get_right(), pa[1].get_left(), buff=0.1).set_color(RED)
        text1 = MathTex(r"+r", font_size=30).set_color(RED)
        arrow2 = Arrow(pa[1].get_right(), pa[2].get_left(), buff=0.1).set_color(RED)
        text2 = MathTex(r"+r", font_size=30).set_color(RED)
        arrow3 = Arrow(pa[4].get_right(), pa[5].get_left(), buff=0.1).set_color(RED)
        text3 = MathTex(r"+r", font_size=30).set_color(RED)
        self.play(GrowArrow(arrow1), Write(text1.next_to(arrow1, UP)))
        self.play(GrowArrow(arrow2), Write(text2.next_to(arrow2, UP)))
        self.play(GrowArrow(arrow3), Write(text3.next_to(arrow3, UP)))
        self.play(FadeOut(VGroup(arrow1, arrow2, arrow3, text1, text2, text3)))
        self.wait()

        # Termo geral
        a1 = MathTex(r"a_1").shift([0,2,0])
        a2 = MathTex(r"a_2 = a_1 + r").next_to(a1, DOWN)
        a3 = MathTex(r"a_3 = a_2 + r").next_to(a2, DOWN)
        a4 = MathTex(r"a_4 = a_3 + r").next_to(a3, DOWN)
        dots = MathTex(r"\vdots").next_to(a4, DOWN)
        an = MathTex(r"a_n = a_{n-1} + r").next_to(dots, DOWN)
        self.play(ReplacementTransform(title, VGroup(a1, a2, a3, a4, dots, an)))
        a3_nova = MathTex(r"a_3 = a_1 + 2r").next_to(a2, DOWN)
        a4_nova = MathTex(r"a_4 = a_1 + 3r").next_to(a3_nova, DOWN)
        an_nova = MathTex(r"a_n = a_1 + (n-1)r").next_to(dots, DOWN)
        self.play(ReplacementTransform(a3, a3_nova), ReplacementTransform(a4, a4_nova), ReplacementTransform(an, an_nova))
        an_center = MathTex(r"a_n = a_1 + (n-1)r")
        self.play(FadeOut(VGroup(a1, a2, a3_nova, a4_nova, dots)), ReplacementTransform(an_nova, an_center))
        frame_geral = SurroundingRectangle(an_center, buff=0.1)
        legend1 = Text("Fórmula do termo geral", font="Courier Prime", color=YELLOW, font_size=30)
        self.play(Create(frame_geral), Write(legend1.next_to(frame_geral, DOWN)))
        self.play(FadeOut(an_center, frame_geral, legend1))

        # Soma dos n termos
        PA = MathTex("a_1", "a_2", "a_3", "\cdots", "a_{n-1}", "a_n").space_out_submobjects(3)
        self.play(Write(PA))
        soma = MathTex(r"S = a_1 + a_2 + a_3 + \cdots + a_{n-1} + a_n")
        self.play(ReplacementTransform(PA, soma))
        soma_inve = MathTex(r"S = a_n + a_{n-1} + \cdots + a_3 + a_2 + a_1")
        self.play(Write(soma_inve.next_to(soma, DOWN)))
        line = Line(start=[-4,-1,0], end=[4,-1,0], color=YELLOW)
        plus_sign = MathTex(r"+", font_size=40, color=YELLOW)
        self.play(Create(line), Write(plus_sign.next_to(soma_inve, RIGHT)))
        soma2 = MathTex(r"2S = (a_1 + a_n) + (a_2 + a_{n-1}) + \cdots + (a_n + a_1)")
        self.play(Write(soma2.next_to(line, DOWN)))
        self.play(FadeOut(VGroup(soma, soma_inve, line, plus_sign, soma2)))

        text_but = Text("Mas, a soma de termos simétricos", font="Courier Prime", font_size=30, color=YELLOW)
        text_but2 = Text("em uma P.A. é sempre a mesma", font="Courier Prime", font_size=30, color=YELLOW).next_to(text_but, DOWN)
        self.play(Write(VGroup(text_but, text_but2)))
        eq1 = MathTex(r"a_i + a_{n-i+1} = a_1 + (i - 1)r + a_1 + (n - i + 1 - 1)r")
        eq2 = MathTex(r"a_i + a_{n-i+1} = a_1 + a_1 + (n - 1)r")
        eq3 = MathTex(r"a_i + a_{n-i+1} = a_1 + a_n")
        self.play(Write(eq1.next_to(text_but2, DOWN)))
        self.play(ReplacementTransform(eq1, eq2.next_to(text_but2, DOWN)))
        self.play(ReplacementTransform(eq2, eq3.next_to(text_but2, DOWN)))
        self.play(FadeOut(VGroup(text_but, text_but2), eq3))
        soma2copy = MathTex(r"2S = (a_1 + a_n) + (a_2 + a_{n-1}) + \cdots + (a_n + a_1)")
        self.play(Write(soma2copy))
        soma3 = MathTex("2S =", "(a_1+a_n) + (a_1+a_n) + \cdots + (a_1+a_n)")
        self.play(ReplacementTransform(soma2copy, soma3))
        brace = Brace(soma3[1], direction=DOWN, color=YELLOW)
        brace_label = Text("n vezes", font="Courier Prime", font_size=30, color=YELLOW)
        self.play(GrowFromCenter(brace), Write(brace_label.next_to(brace, DOWN)))
        self.play(FadeOut(brace, brace_label))
        final = MathTex(r"2S = (a_1 + a_n)n")
        self.play(ReplacementTransform(soma3, final))
        final2 = MathTex(r"S = \frac{(a_1 + a_n)n}{2}")
        self.play(ReplacementTransform(final, final2))
        frame_soma = SurroundingRectangle(final2, buff=0.1)
        self.play(Create(frame_soma))
        self.wait()
        self.play(FadeOut(final2, frame_soma))

        # Finalização
        Author = Text('Siga @manual.fisica', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(ReplacementTransform(author, Author))
        self.wait()

if __name__ == "__main__":
    PA().render()
