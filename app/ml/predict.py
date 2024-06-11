"""
predict.py
Author: Max Sealey

Uses Machine Learning (a Supervised Learning Random Forest Classification model)
to make a prediction on the playoff likelihood of teams based on salary cap data
"""

import data_helpers as util
import model as ml  # for testing purposes

"""
make_prediction()

Args: % of cap for QB, % of cap for offense, % of cap for defense
Ret: N/A

Applies user inputs to ML model created in create_model()
"""


def make_prediction(model, qb_p, off_p, def_p):
    # retrieve data
    rfc_model = model['model']
    accuracy = model['acc_score']

    # allows user inputs to be whole percentage (47%, eg.)
    # converts to decimal usable in the model
    qb_p_dec = util.percent_to_decimal(qb_p)
    off_p_dec = util.percent_to_decimal(off_p)
    def_p_dec = util.percent_to_decimal(def_p)

    # converts accuracy score to a percentage with two decimal places (string)
    acc_per = util.decimal_to_percent(accuracy)

    # makes classification prediction (first element contains 1 or 0) with converted data
    prediction = rfc_model.predict([[qb_p_dec, off_p_dec, def_p_dec]])
    if prediction[0] == 1:
        prediction_text = f'''
    The model predicts that the team will make the playoffs. 
    This is {acc_per}% likely to be true.

    Based on this projection, we recommend giving them prime time games
    and use this as leverage when negotiating with streaming services.

            '''
    else:
        prediction_text = f'''
    The model predicts that the team will not make the playoffs. 
    This is {acc_per}% likely to be true.\n

    Based on this projection, we recommend burying this team's games in 
    midday Sunday slots, keeping them off the air more than projected playoff teams.

                    '''
    print(prediction_text)
    return prediction_text


make_prediction(ml.create_model(), 20, 40, 20)
