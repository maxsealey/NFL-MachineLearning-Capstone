"""
main.py
Author: Max Sealey

NOTE FOR EVALUATORS: User interaction will be done
through the CLI. Please run the program on this script.
"""
import dash_functions
from app import ml_predict

model = ml_predict.create_model()

while True:
    dash_functions.welcome_message()

    break
