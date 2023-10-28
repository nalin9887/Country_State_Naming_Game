import turtle
import pandas
from turtle import Turtle,Screen
from state import State


screen=Screen()
tim=Turtle()
screen.setup(800,953)
image="Indiamap.gif"

screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("Indiamap_coordinates")
dat=data["state"]

# def buttonclick(x,y):
#     print(x,y)
#
#  #onscreen function to send coordinate
# turtle.onscreenclick(buttonclick)
state_list=data["state"].to_list()
guessed_state=[]
flag=True
count=0
while len(guessed_state)<28 and flag:
    answer= screen.textinput(f"{count}/28 State Found","Enter the Guess Below write ~exit~ for exit")
    answer=answer.capitalize()
    for n in state_list:
        if answer==n:

            df=data[data.state==f"{answer}"]
            print(df)
            State(int(df["x"]),int(df["y"]),answer,"Black")
            guessed_state.append(answer)
            count+=1
        elif answer=="Exit":
            missing_state=[states for states in state_list if states not in guessed_state]
            print(len(missing_state))
            count=0


            for all in missing_state:
                if count != len(missing_state):
                     df=data[data.state==all]
                     #print(df)
                     State(int(df["x"]),int(df["y"]),all,"Red")
                     count+=1

            flag=False
screen.exitonclick()
#screen.mainloop()

