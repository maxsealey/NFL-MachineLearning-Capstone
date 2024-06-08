"""
ml_predict.py
Author: Max Sealey

Uses Machine Learning (a Supervised Learning Random Forest Classification model)
to make a prediction on the playoff likelihood of teams based on salary cap data
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import data_helpers as util
from sql_scripts import retrieve_prediction_data_script
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

"""
create_model()

Args: N/A
Ret: dictionary containing model, scaler, and the accuracy score

Creates an ML model for predicting whether a team makes the playoffs or not
based on salary cap data (classification: playoffs or not)

Prints accuracy score and classification report to the console, 
displays confusion matrix showing actual vs predicted results on test data

Called in make_prediction(), which is defined right below
"""
def create_model():
    # Passes in sql script into utility function get_df_with_cleaned_data() to retrieve
    # dataframe with only the data needed to make a prediction
    df = util.get_df_with_cleaned_data(retrieve_prediction_data_script())

    # features are % of cap allocated to qb, offense (as a whole), and defense (as a whole)
    features = ['qb_p', 'off_p', 'def_p']
    X = df[features]
    y = df['playoffs']

    # split data into training and testing subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # initialize StandardScaler object, fit and transform the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # initialize RFC model and fit to training data
    model = RandomForestClassifier()
    model.fit(X_train_scaled, y_train)

    # predicts on the scaled test set and stores in y_pred
    y_pred = model.predict(X_test_scaled)

    # compares predictions vs test results
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    # displays accuracy score and classification report
    print(f'Accuracy: {accuracy:.2f}\n')
    print('Classification Report:\n', class_report)
    results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    results_df['Correct Prediction'] = results_df['Actual'] == results_df['Predicted']
    print("")
    print("Actual vs Predicted Outcomes:")
    print(results_df.head(10))
    print("")

    # confusion matrix visualization
    sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d', xticklabels=['No Playoffs', 'Playoffs'],
                yticklabels=['No Playoffs', 'Playoffs'])
    plt.xlabel('Predicted Outcomes')
    plt.ylabel('Actual Outcomes')
    plt.title('NFL Playoff Predictor Confusion Matrix')
    plt.show()

    # returns dictionary with things needed to make prediction with user input
    return {
        'model': model,
        'acc_score': accuracy
    }


"""
make_prediction()

Args: % of cap for QB, % of cap for offense, % of cap for defense
Ret: N/A

Applies user inputs to ML model created in create_model()
"""

def make_prediction(qb_p, off_p, def_p):
    # call create_model and retrieve data
    model_dict = create_model()
    rfc_model = model_dict['model']
    accuracy = model_dict['acc_score']

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
        prediction_text = f'The model predicts that the team will make the playoffs. This is {acc_per}% likely to be true.\n'
    else:
        prediction_text = f'The model predicts that the team will not make the playoffs. This is {acc_per}% likely to be true.\n'

    print(prediction_text)
    return prediction_text


make_prediction(12, 35, 56)