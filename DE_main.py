import turtle
import pandas as pd
#static values
FONT = ("Courier", 10, "normal")

#setting up the screen to show the map 
screen = turtle.Screen()
screen.title("European Country guessing")
image = "/Users/german/Documents/Coding/Python projects/My coding projects/Turtle Library/European country guessing/Europa.gif" 
screen.addshape(image)
screen.setup(900, 800)


df_ger = pd.read_csv("/Users/german/Documents/Coding/Python projects/My coding projects/Turtle Library/European country guessing/länder.csv")
länder = df_ger.länder

#my turtle which will write the countrys
t = turtle.Turtle()
t.penup()
t.hideturtle()


correct_guess = []
my_turtle = turtle.Turtle(image)

while len(correct_guess) < 47:
    guess = screen.textinput(title=f"Du hast {len(correct_guess)}/47 Länder bereits erraten.", prompt="Rate ein Land" ).title()
    for land in länder:        
        if guess == land:
            x_cor = int(df_ger.x[(df_ger.länder == land)])
            y_cor = int(df_ger.y[(df_ger.länder == land)])
            t.goto(x_cor, y_cor)
            t.write(land, align="center", font=FONT)
            correct_guess.append(land)

