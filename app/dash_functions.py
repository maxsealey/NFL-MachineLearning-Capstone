"""
User Dashboard
Author: Max Sealey

For the time being, user interaction will be done through the CLI.
"""


def welcome_message():
    input(
        '''
----------------------------------------------
NFL Win Prediction Machine Learning Solution
----------------------------------------------
Thank you for using this application. We'll start
by training the Random Forest Classification model
to predict the playoff likelihood of any NFL team
based on how they allocate salary data. 

Please hit any key.
'''
    )
