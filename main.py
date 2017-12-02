from kivy.app import App
from kivy.uix.widget import Widget
from block import Block


class Grid(Widget):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        start_pos = (100, 500)
        size = 50
        for j in range(10):
            for i in range(10):
                self.add_widget(
                    Block(j, i, pos=(start_pos[0] + i * size, start_pos[1] - j * size), size=(size - 1, size - 1)))


class MainApp(App):
    def build(self):
        return Grid()


if __name__ == '__main__':
    MainApp().run()