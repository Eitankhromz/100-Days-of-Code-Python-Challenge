import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
correct_ans = []
score = 0

#Use a loop to allow the user to keep guessing
while len(correct_ans) < 50:
    #Convert guess into Title case
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").title()


    # Check if the Guess is among the 50 states
    if answer_state == "Exit":
        # states_to_learn.csv
        missing_states = [state for state in all_states if state not in correct_ans]
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_ans:
        #         missing_states.append(state)
        l_states = pandas.DataFrame(missing_states)
        l_states.to_csv("states_to_learn.csv")
        break
    for state in all_states:
        if answer_state == state:
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            state_data = df[df.state == answer_state]
            new_turtle.goto(int(state_data.x), int(state_data.y))
            new_turtle.write(answer_state)

            #Record the correct guesses in a list
            correct_ans.append(answer_state)

            #Keep track of the score
            score += 1









