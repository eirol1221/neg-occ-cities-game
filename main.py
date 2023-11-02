from turtle import Turtle, Screen
import pandas as pd

MAP = "neg_occ_map.gif"
guessed_cities = []
count_correct_guess = 0
title = "Guess the city or municipality"

screen = Screen()
neg_occ_map = Turtle()
cuco = Turtle()

screen.title("Guess the Negros Occidental cities or municipalities")
screen.setup(700, 900)
screen.addshape(MAP)
neg_occ_map.shape(MAP)

cuco.pencolor("black")
cuco.up()
cuco.hideturtle()

data = pd.read_csv("neg_occ_cities.csv")
all_locations = data.location.to_list()

while len(guessed_cities) < 32:
    answer = screen.textinput(title, "What is another city or municipality?").title()
    if answer == "Exit":
        missed_locations = [city for city in all_locations if city not in guessed_cities]
        df_city = pd.DataFrame(missed_locations)
        df_city.to_csv("missed-locations.csv")
        break
    elif answer in all_locations and answer not in guessed_cities:
        loc_record = data[data.location == answer]
        cuco.goto(int(loc_record.x), int(loc_record.y))
        cuco.write(answer, False, "center", ("Arial", 8, "bold"))
        guessed_cities.append(answer)
        count_correct_guess += 1
        title = f"{count_correct_guess}/32 Locations Correct"