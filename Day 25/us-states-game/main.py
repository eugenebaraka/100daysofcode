import turtle
import pandas
from choose_state import ChooseState

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read in data
states_data = pandas.read_csv("50_states.csv")
states_data["state"] = states_data["state"].str.lower()

# get choose state object
chooses_state = ChooseState()
score = 0

game_is_on = True

remaining_states = states_data["state"].tolist() # states left to guess

while game_is_on:
    # prompt user to guess the state
    answer = screen.textinput(title=f"{score}/50 States Correct",
                              prompt="What's another state's name")
    answer = answer.lower()

    if answer == "exit":
        # generate csv of states to learn
        learn_these = pandas.DataFrame({"state":remaining_states})
        learn_these.to_csv("states_to_learn.csv")
        # break the game
        game_is_on = False
    if answer in remaining_states:
        # get hold of x and y of the state
        x = float(states_data[states_data["state"] == answer]["x"])
        y = float(states_data[states_data["state"] == answer]["y"])

        # move the answer to the x and y coordinates
        chooses_state.move_answer(x, y, answer)
        score += 1
        remaining_states.remove(answer) # remove the already guessed answer

    # check if all the states have been guessed and end the game
    if len(remaining_states) == 0:
        print("Well done!! All states correctly guessed!")
        game_is_on = False
