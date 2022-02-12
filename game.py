import turtle
import pandas as pd


screen=turtle.Screen()
screen.title("U.S. States Game")
image="C:/Users/joao.ferreira/Documents/100 days/US-states/us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data=pd.read_csv("C:/Users/joao.ferreira/Documents/100 days/US-states/us-states-game-start/50_states.csv")
all_states=list(data.state)
continua=[]
export=[]

while len(continua)<50:
    answer=screen.textinput(title=f"{len(continua)}/50Guess the State",
                            prompt="What's another state's name ?").title()
    if answer=="Exit":
        for i in all_states:
            if i not in continua:
                export.append(i)
                x=pd.DataFrame(export, columns=['state']) 
                x.to_csv('C:/Users/joao.ferreira/Documents/100 days/US-states/us-states-game-start/teste.csv')
        break
    
    if answer in all_states:
        continua.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)


            