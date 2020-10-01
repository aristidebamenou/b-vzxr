from pawn import Pawn


class Board:
    """ Width * height size board initialized with a robot. The robot is a pawn """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robot = Pawn()

    def step(self, value):
        """ Anticipates the robot's movements on the board """
        if self.robot.direction == 'UP':
            self.robot.ordinate += value
            if self.robot.ordinate >= self.height:
                self.robot.ordinate = self.height - 1
        elif self.robot.direction == 'RIGHT':
            self.robot.abscissa += value
            if self.robot.abscissa >= self.width:
                self.robot.abscissa = self.width - 1
        elif self.robot.direction == 'DOWN':
            self.robot.ordinate -= value
            if self.robot.ordinate < 0:
                self.robot.ordinate = 0
        elif self.robot.direction == 'LEFT':
            self.robot.abscissa -= value
            if self.robot.abscissa < 0:
                self.robot.abscissa = 0
        else:
            pass

    def move(self, lead, step):
        """Move the robot in one direction with a number of steps """
        self.robot.lead(lead)
        self.step(step)
        return self.robot.abscissa, self.robot.ordinate
