import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('Ghana map game')
image = "image.gif"
screen.addshape(image)
screen.setup(width=491, height=725)
turtle.shape(image)

data = pd.read_csv('map_csv.csv')

#correct_guesses = []
#missed_guesses = []
still_guessing = True
while still_guessing:
    region_guess = screen.textinput(title=f'{len(correct_guesses) - 2}/{len(data.Region)}',
                                    prompt='Enter another region name:')
    guess = region_guess
    region = data.Region.to_list()
    
    if guess.title() == 'Exit':
        missed_guesses = [missed_guesses.append(row) for row in region if row not in correct_guesses]
        print(missed_guesses)
        #for row in region: # region has been converted to a list.
           #if row not in correct_guesses:
                #missed_guesses.append(row)
        df = pd.DataFrame(missed_guesses)
        print(df)
        df.to_csv('regions_to_learn.csv')
        break

    correct_guesses = [correct_guesses.append(guess)for row in region if guess in row]

    #for row in region:
        #if guess in row:
            #correct_guesses.append(guess)
    region_data = data['Regoin'] # emf of the programme.hahaha
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(region_data.x), int(region_data.y))
    t.write(guess)


#screen.exitonclick()

# map_data = {
#     'region': ['greater accra', 'volta', 'eastern', 'northern', 'ahafo', ' ashanti', 'bono east',
#                'bono', 'central', 'north east', 'oti', 'savannah', 'upper east', 'upper west',
#                'western', 'western north'],
#     'coor': ['83.0 -165.0', '115.0 -110.0', '41.0 -106.0', '62.0 136.0', '-127.0 -66.0', '-37.0 -76.0', '-35.0 1.0',
#              '-124.0 -15.0', '-17.0 -186.0', '15.0 192.0', '100.0 12.0', '-87.0 104.0', '-6.0 231.0', '-114.0 203.0',
#              '-99.0 -199.0', '-150.0 -126.0']
# }
#
# df = pd.DataFrame(map_data)
# df.to_csv('map_csv.csv')
#
# print(screen.screensize())
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
