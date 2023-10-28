from turtle import Turtle
self=Turtle()
class State(Turtle):
    def __init__(self,posiiton_x, position_y,name,color):
        super().__init__()

        self.color(color)
        self.ht()
        self.penup()
        self.goto(posiiton_x, position_y)
        self.write(name)

        #self.all_state=[]
    # def create(self, posiiton_x, position_y, name):
    #
    #     self.color("Red")
    #     self.ht()
    #     self.penup()
    #     self.goto(posiiton_x, position_y)
    #     self.write(name)
