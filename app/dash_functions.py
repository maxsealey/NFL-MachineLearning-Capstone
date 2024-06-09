"""
User Dashboard Helper Functions
Author: Max Sealey

Called in main.py
"""


def welcome_message():
    input(
        '''
----------------------------------------------
NFL Win Prediction Machine Learning Solution
----------------------------------------------
Thank you for using this application. We'll start by training 
the Random Forest Classification model to predict the playoff 
likelihood of any NFL team based on how they allocate player salaries. 

Type anything and click 'enter'

'''
    )


"""
option_menu()
"""
def option_menu():
    res = input(
        '''
-----------------------------------------------------------------------------------
                 NFL PLAYOFF PREDICTOR - MAIN MENU
-----------------------------------------------------------------------------------
Now that the model has been trained, there are four options for interacting
with the data:

    1) Make a prediction for a team with a test data sample
    
    2) Input a Team and a Season/Year (from 2013-2022) and view a 
    pie chart showing how they allocated cap space by position.
    
    3) Input a Division and a Season/Year (from 2013-2022) and view a
    stacked bar chart displaying how each team allocated cap space by position
    
    4) Input a Division and either offense or defense to view a line graph showing
    how much of each team's cap space was spent on that side of the ball.

Please enter a single integer (1-4), or 'q' to quit, and press enter.


'''
    )
    return res


"""
get_prediction_input()
"""
def get_prediction_input():
    print(
        '''
    Please enter the percentage of salary cap for your test team
    for the OFFENSE, DEFENSE, and QB respectively below. Offense and Defense
    must equal 100 or less combined, and QB must be less than Offense.
    
    Format: __:__ (45.67, 12.84, 69.69, etc)
    
    '''
    )
    offense = input("\nPlease enter the percentage of salary cap spent on the OFFENSE: ")

    defense = input("\nPlease enter the percentage of salary cap spent on the DEFENSE: ")

    qb = input("\nPlease enter the percentage of salary cap spent on\n"
               "the QB Position. Must be less than percentage spent on offense:  ")

    return [float(qb), float(offense), float(defense)]


"""
get_pie_chart_input()
"""
def get_pie_chart_input():
    team = input("Please enter the name of an NFL team (e.g. Cardinals, Broncos,\n"
                 "Chiefs, Seahawks, etc.):  ")
    season = input("\nPlease enter a season/year from 2013-2022:  ")

    return [team.capitalize(), int(season)]


"""
get_bar_chart_input()
"""
def get_bar_chart_input():
    div = input("Please enter the name of an NFL division, case-sensitive (e.g. NFC West, NFC East,\n"
                "AFC South, AFC North, etc.):  ")
    season = input("\nPlease enter a season/year from 2013-2022:  ")

    return [div, int(season)]


"""
get_line_graph_input()
"""
def get_line_graph_input():
    div = input("Please enter the name of an NFL division, case-sensitive (e.g. NFC West, NFC East,\n"
                "AFC South, AFC North, etc.):  ")
    sob = input("\nPlease enter either 'Offense' or 'Defense':  ")

    return [div, sob.capitalize()]


"""
input_invalid_message()
"""
def input_invalid_message():
    input("\nThat input does not fit the parameters of what we \n"
          "are looking for. Please type anything and click 'enter' to try again. \n\n")


"""
byebye_message()
"""
def byebye_message():
    print("Thank you for using this application. Take care!")


"""
continue_or_nah_message()
"""
def continue_or_nah_message():
    res = input(
        '\n'
        'Would you like to go back to the main menu and pick an option again?\n'
        'Enter \'y\' to go back and anything else to quit.\n'
        '\n'
    )
    return res
