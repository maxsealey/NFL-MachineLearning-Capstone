"""
main.py
Author: Max Sealey

NOTE FOR EVALUATORS: User interaction will be done
through the CLI. Please run the program on this script.
"""

import dash_functions as dash
import ml_predict as ml
import visualize_data as vd

while True:  # runs until user quits (or program breaks, which shouldn't ever happen)

    dash.welcome_message()

    model = ml.create_model()  # creates and trains model

    while True:  # runs until user is done using program
        option = dash.option_menu()

        if option == 'q':
            dash.byebye_message()
            break

        elif option == str(1):  # prediction option
            while True:
                try:
                    user_input = dash.get_prediction_input()  # get user input and make prediction
                    ml.make_prediction(model, user_input[0], user_input[1], user_input[2])
                    break
                except RuntimeWarning:
                    dash.input_invalid_message()
                except ValueError:
                    dash.input_invalid_message()
                except TypeError:
                    dash.input_invalid_message()
                continue

            cont = dash.continue_or_nah_message()

            if cont == 'y':
                continue
            else:
                break

        elif option == str(2):  # pie chart option
            while True:
                try:
                    user_input = dash.get_pie_chart_input()  # get user input and create pie chart with the information
                    vd.team_salary_breakdown_pie_chart(user_input[0], user_input[1])
                    break
                except RuntimeWarning:
                    dash.input_invalid_message()
                except ValueError:
                    dash.input_invalid_message()
                except TypeError:
                    dash.input_invalid_message()
                continue

            cont = dash.continue_or_nah_message()

            if cont == 'y':
                continue
            else:
                break

        elif option == str(3):  # bar chart option
            while True:
                try:
                    user_input = dash.get_bar_chart_input()  # get user input and create bar graph with the information
                    vd.division_breakdown_stacked_bar(user_input[0], user_input[1])
                    break
                except RuntimeWarning:
                    dash.input_invalid_message()
                except ValueError:
                    dash.input_invalid_message()
                except TypeError:
                    dash.input_invalid_message()
                continue

            cont = dash.continue_or_nah_message()

            if cont == 'y':
                continue
            else:
                break

        elif option == str(4):  # line graph option
            while True:
                try:
                    user_input = dash.get_line_graph_input()  # get user input and create line graph with the information
                    vd.division_offense_defense_trends_line_graph(user_input[0], user_input[1])
                    break
                except RuntimeWarning:
                    dash.input_invalid_message()
                except ValueError:
                    dash.input_invalid_message()
                except TypeError:
                    dash.input_invalid_message()
                continue

            cont = dash.continue_or_nah_message()

            if cont == 'y':
                continue
            else:
                break

        else:
            dash.input_invalid_message()
            continue

    dash.byebye_message()
    break
