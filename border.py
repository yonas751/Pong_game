from turtle import Turtle
my_list=[(0,-20),(0,0),(0,20)]
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.another_list=[]
        self.border()




    def border(self):

        for i in range(-360,400,40):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.shapesize(1, 0.5)
            turtle.penup()



            turtle.goto(0, i)
            self.another_list.append(turtle)








        # for i in range(len(my_list)-1,0,-1):
        #     new_x=self.another_list[i-1][0]
        #     new_y=self.another_list[i-1][0]
        #     self.another_list[i].goto(new_x,new_y)




