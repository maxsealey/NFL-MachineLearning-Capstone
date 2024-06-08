"""
data_helpers.py
Author: Max Sealey

Utility functions
"""
import pandas as pd
import sqlite3 as sql

"""
get_df_with_cleaned_data()

Args: sql script (string)
Ret: Dataframe with data 


Called in visualize_data.py and ml_predict
"""


def get_df_with_cleaned_data(script):
    # loads data to pandas dataframe
    csv = '../../data/nfl_data.csv'
    df = pd.read_csv(csv)

    # connect to database
    conn = sql.connect('nfl_data.db')
    cursor = conn.cursor()
    df.to_sql('nfl_data', conn, if_exists='replace', index=False)
    conn.commit()

    # cleaning and preparing data by creating a new table with only relevant information
    cursor.executescript(script)
    conn.commit()

    q = 'SELECT * FROM relevant_data'
    df = pd.read_sql_query(q, conn)
    conn.close()
    return df


"""
sb_or_playoffs()

Args: team name (string), year (int), playoffs_bool (int, 1 or 0), sb_bool (int, 1 or 0)
Ret: Statement (string)

Called in visualize_data.py
"""


def sb_or_playoffs(team, year, playoffs_bool, sb_bool):
    won_sb = f'The {team} {"won" if sb_bool else "did not win"} the Super Bowl in {year}.'
    lost_in_playoffs = f'The {team} lost at some point in the playoffs in {year}.'
    did_not_make_playoffs = f'The {team} did not make the playoffs in {year}.'

    if sb_bool:
        return won_sb
    elif playoffs_bool:
        return lost_in_playoffs
    else:
        return did_not_make_playoffs


"""
position_labels()

Args: N/A
Ret: List of easily readable position names

Called in visualize_data.py
"""


def position_labels():
    return ['QB', 'RB', 'WR', 'TE', 'OL', 'IDL', 'EDGE', 'LB', 'S', 'CB']


"""
get_teams_in_division()

Args: division name (string)
Ret: list of four team names (strings)

Called in visualize_data.py
"""


def get_teams_in_division(division):
    if division == "NFC North":
        return ["Bears", "Packers", "Lions", "Vikings"]
    elif division == "NFC East":
        return ["Eagles", "Cowboys", "Commanders", "Giants"]
    elif division == "NFC South":
        return ["Buccaneers", "Saints", "Falcons", "Panthers"]
    elif division == "NFC West":
        return ["Seahawks", "49ers", "Rams", "Cardinals"]
    elif division == "AFC North":
        return ["Bengals", "Steelers", "Browns", "Ravens"]
    elif division == "AFC East":
        return ["Patriots", "Dolphins", "Jets", "Bills"]
    elif division == "AFC South":
        return ["Texans", "Jaguars", "Titans", "Colts"]
    elif division == "AFC West":
        return ["Chiefs", "Chargers", "Raiders", "Broncos"]
    else:
        return "error"


"""
percent_to_decimal()

Args: percentage
Ret: percentage in decimal form

Converts a percentage string to decimal form
"""


def percent_to_decimal(percent_str):
    return float(percent_str) / 100
