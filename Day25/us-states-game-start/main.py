import turtle
import pandas as pd
state_data = pd.read_csv('./Day25/us-states-game-start/50_states.csv')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./Day25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
num_correct = 0
num_incorrect = 0
previously_guesed = []
running = True
state_names = state_data['state'].tolist()

def draw_state(state):
    x = int(state_data.loc[state_data['state'] == state]['x'])
    y = int(state_data.loc[state_data['state'] == state]['y'])
    print(x)
    state_turtle.up()
    state_turtle.goto(x, y)
    state_turtle.write(state)

    
while running:
    answer_state = screen.textinput(title=f"{len(previously_guesed)}/50 Guess the State", prompt="What is the name of a State?")
    answer_state = answer_state.title()
    if answer_state in state_names and answer_state not in previously_guesed:
        state_names.remove(answer_state)
        previously_guesed.append(answer_state)
        draw_state(answer_state)
        if len(previously_guesed) == 50:
            running = False
    if answer_state == "Exit":
        break


state_data[state_data['state'].isin(state_names)].to_csv('./Day25/us-states-game-start/states_to_learn.csv')


"""
use the following code to get the x and y values for the states on the image
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""

#screen.exitonclick()
#state_data = pd.read_csv('./Day25/us-states-game-start/50_states.csv')
#print(state_data.head())
