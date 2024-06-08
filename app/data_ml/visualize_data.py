"""
visualize_data.py
Author: Max Sealey

Below are three functions called to get visualize aspects of the salary data
used in this application.
"""
import matplotlib.pyplot as plt
import numpy as np
from sql_scripts import team_year_pie_chart_script, div_year_stacked_bar_chart_script, \
    division_off_def_trends_linegraph_script
import data_helpers as util


"""
team_salary_breakdown_pie_chart()

Displays pie chart with % of salary cap allocated to each position for a
specific team and year

Args: team (string) and year (int)
Ret: N/A 

Called in this function: data_helpers.position_labels(), data_helpers.get_df_with_cleaned_data(),
                         data_helpers.sb_or_playoffs(), sql_scripts.team_year_pie_chart_script()
"""


def team_salary_breakdown_pie_chart(team, year):
    # Passes in sql script into utility function get_df_with_cleaned_data() to retrieve
    # dataframe with only the data needed to make a prediction
    df = util.get_df_with_cleaned_data(team_year_pie_chart_script(team, year))

    # gets pie chart slices
    pos_slices = ['qb_p', 'rb_p', 'wr_p', 'te_p', 'ol_p', 'idl_p', 'edge_p', 'lb_p', 's_p', 'cb_p']
    pos_data = df[pos_slices]
    pos_sum = pos_data.sum()

    # Displays circular pie chart with labels and % data
    plt.figure(figsize=(10, 8))
    plt.pie(pos_sum, labels=util.position_labels(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Salary Allocation by Position')
    plt.axis('equal')

    # Pie Chart description
    # calls sb_or_playoffs for string describing how the team did in the playoffs
    plt.figtext(0.5, 0.05, util.sb_or_playoffs(team, year, df['playoffs'].iloc[0], df['sb'].iloc[0]),
                ha='center', fontsize=14, bbox={"facecolor": "blue", "alpha": 0.4, "pad": 5})
    plt.show()


"""
division_breakdown_stacked_bar()

Displays a stacked bar chart for each of four teams in a division displaying
percentage of cap spent on each position in a given year

Args: division (string), year/season (int)
Ret: N/A
"""


def division_breakdown_stacked_bar(division, year):
    # uses helper functions to turn division name into list of teams and insert into sql script for data cleaning
    teams = util.get_teams_in_division(division)
    script = div_year_stacked_bar_chart_script(teams, year)
    df = util.get_df_with_cleaned_data(script)

    pos_slices = ['qb_p', 'rb_p', 'wr_p', 'te_p', 'ol_p', 'idl_p', 'edge_p', 'lb_p', 's_p', 'cb_p']
    pos_data = df.set_index('team')[pos_slices]

    # plot stacked bar chart
    pos_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='Paired')

    # set title and labels
    plt.title(f'Salaries by Position for {division} Teams in {year}')
    plt.xlabel('Teams')
    plt.ylabel('Salary Allocation Percentage')
    plt.legend(util.position_labels(), title='Positions', bbox_to_anchor=(1, 1))

    # bottom description
    description = f'Salary breakdown for {division} teams in the {year} season.'
    plt.figtext(0.5, -0.1, description, ha='center', fontsize=10,
                bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})

    plt.tight_layout()
    plt.show()


"""
division_offense_defense_trends_line_graph()

Displays a line graph showing trend in percentage of cap spent on a certain side of the ball
from 2013-2022 for each team in specified division

Args: division (string), side_of_ball (string; input should always be either
'offense_p' or 'defense_p')
Ret: N/A
"""

def division_offense_defense_trends_line_graph(division, side_of_ball):
    # clean and format the data
    teams = util.get_teams_in_division(division)
    script = division_off_def_trends_linegraph_script(teams, side_of_ball)
    df = util.get_df_with_cleaned_data(script)
    sob_formatted = "OFFENSIVE" if side_of_ball == "offense_p" else "DEFENSIVE"

    # plot line graph by iterating through teams in division
    plt.figure(figsize=(10, 6))
    for i in teams:
        team_data = df[df['team'] == i]
        plt.plot(team_data['season'], team_data[side_of_ball], label=i)

    # label graph and display
    plt.xlabel('Season')
    plt.ylabel(f'% of Cap Spent on the {sob_formatted} Side of the Ball')
    plt.title(f'{division} Division {sob_formatted} Spending Trends (2013-2022)')
    plt.xticks(np.arange(2013, 2023, step=1))
    plt.legend()
    plt.grid(True)
    plt.show()


# for testing functions
# team_salary_breakdown_pie_chart("Cardinals", 2022)
# division_breakdown_stacked_bar("AFC East", 2016)
division_offense_defense_trends_line_graph("AFC West", "offense_p")
