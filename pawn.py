class Pawn:
    """ Pawn initialized to position (0,0) with the head up. """
    def __init__(self):
        self.direction = 'UP'
        self.abscissa = 0
        self.ordinate = 0

    def lead(self, orientation):
        """Turn the pawn left or right"""
        if orientation == 'right':
            if self.direction == 'UP':
                self.direction = 'RIGHT'
            elif self.direction == 'RIGHT':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'LEFT'
            elif self.direction == 'LEFT':
                self.direction = 'UP'
            else:
                pass
        elif orientation == 'left':
            if self.direction == 'UP':
                self.direction = 'LEFT'
            elif self.direction == 'LEFT':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'RIGHT'
            elif self.direction == 'RIGHT':
                self.direction = 'UP'
            else:
                pass
        else:
            pass
