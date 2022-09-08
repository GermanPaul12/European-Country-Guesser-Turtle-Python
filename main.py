import turtle
import pandas as pd
#static values
FONT = ("Courier", 7, "normal")

#setting up the screen to show the map 
screen = turtle.Screen()
screen.title("European Country guessing")
image = "European country guessing/Europa.gif"
screen.addshape(image)
screen.setup(900, 800)

#pandas reading the csv and filtering the rows
df_us = pd.read_csv("European country guessing/countrys.csv")
countrys = df_us.country

#my turtle which will write the countrys
t = turtle.Turtle()
t.penup()
t.hideturtle()



correct_guess = []
my_turtle = turtle.Turtle(image)

while len(correct_guess) < 47:
    guess = screen.textinput(title=f"You have guessed {len(correct_guess)}/47 countries.", prompt="Guess a country" ).title()
    for country in countrys:
        if guess == country:
            x_cor = int(df_us.x[(df_us.country == country)])
            y_cor = int(df_us.y[(df_us.country == country)])
            t.goto(x_cor, y_cor)
            t.write(country, align="center", font=FONT)
            correct_guess.append(country)
  
""" def get_mouse_click_cor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop() """

screen.exitonclick()