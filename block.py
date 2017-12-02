from random import choice
from kivy.utils import get_color_from_hex as hexc
from kivy.uix.button import Button

colors = ((1,0,0,1), (0,1,0,1), hexc('#F0FF12'), hexc('#C421E5'))


class Block(Button):
    def __init__(self,  row, col, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.row = row
        self.col = col
        # use it to start the swap mechanic
        self.pressed = False
        self.text = str(self.row)+","+str(self.col)
        self.background_color = choice(colors)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # pass the initial touch x and y
            self.pressed = touch.pos

    def on_touch_up(self, touch):
        # when released, compare the down (x,y) vs the up (x,y)
        # and do the appropriated swap
        if self.pressed:
            if abs(touch.pos[0] - self.pressed[0]) > abs(touch.pos[1] - self.pressed[1]):
                if touch.pos[0] - self.pressed[0] > 0:
                    # swap right
                    self.swap((self.row, self.col), (self.row, self.col + 1))
                else:
                    # swap left
                    self.swap((self.row, self.col), (self.row, self.col - 1))
            else:
                if touch.pos[1] - self.pressed[1] > 0:
                    # swap up
                    self.swap((self.row, self.col), (self.row - 1, self.col))
                else:
                    # swap down
                    self.swap((self.row, self.col), (self.row + 1, self.col))
            # reset the pressed check
            self.pressed = False

    def swap(self, cord1, cord2):
        try:
            # the swap takes the row and col of both origin and destination
            # block and point the variables to the correct object from the parent.children list
            origin = [x for x in self.parent.children if x.row == cord1[0] and x.col == cord1[1]][0]
            destination = [x for x in self.parent.children if x.row == cord2[0] and x.col == cord2[1]][0]
            # swap the position, row and col information
            dest_pos = destination.pos.copy()
            dest_col, dest_row = destination.col, destination.row
            destination.pos = origin.pos.copy()
            destination.col, destination.row = origin.col, origin.row
            origin.pos = dest_pos.copy()
            origin.col, origin.row = dest_col, dest_row
        except:
            pass