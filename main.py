from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line, Rectangle
from random import uniform, randint
from math import hypot


class Partikel(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data = []

        for i in range(80):
            self.data.append([
                uniform(0, 800),
                uniform(0, 500),
                uniform(-80, 80),
                uniform(-80, 80),
                randint(2, 4)
            ])

        Clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):

        self.canvas.clear()

        with self.canvas:

            Color(0.02, 0.02, 0.06, 1)
            Rectangle(
                pos=self.pos,
                size=self.size
            )

            for p in self.data:

                p[0] += p[2] * dt
                p[1] += p[3] * dt

                if p[0] <= 0 or p[0] >= self.width:
                    p[2] *= -1

                if p[1] <= 0 or p[1] >= self.height:
                    p[3] *= -1

            # Garis antar partikel
            for i in range(len(self.data)):

                for j in range(i + 1, len(self.data)):

                    a = self.data[i]
                    b = self.data[j]

                    jarak = hypot(
                        a[0] - b[0],
                        a[1] - b[1]
                    )

                    if jarak < 100:

                        Color(
                            0.3,
                            0.7,
                            1,
                            0.3
                        )

                        Line(
                            points=[
                                a[0], a[1],
                                b[0], b[1]
                            ],
                            width=1
                        )

            # Titik partikel
            Color(0.4, 0.9, 1, 1)

            for p in self.data:

                r = p[4]

                Ellipse(
                    pos=(
                        p[0] - r,
                        p[1] - r
                    ),
                    size=(
                        r * 2,
                        r * 2
                    )
                )


class PartikelApp(App):

    def build(self):
        self.title = "Particle"
        return Partikel()


PartikelApp().run()
