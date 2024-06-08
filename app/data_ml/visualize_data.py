"""
visualize_data.py
Author: Max Sealey

Below are three functions called to get visualize aspects of the salary data
used in this application.
"""
import matplotlib.pyplot as plt
from sql_scripts import team_year_pie_chart_script
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
    df = util.get_df_with_cleaned_data(team_year_pie_chart_script())

    # extract data for specific team & year
    team_data = df[(df['team'] == team) & (df['season'] == year)]

    # gets pie chart slices
    pos_slices = ['qb_p', 'rb_p', 'wr_p', 'te_p', 'ol_p', 'idl_p', 'edge_p', 'lb_p', 's_p', 'cb_p']
    pos_data = team_data[pos_slices]
    pos_sum = pos_data.sum()

    # Displays circular pie chart with labels and % data
    plt.figure(figsize=(10, 8))
    plt.pie(pos_sum, labels=util.position_labels(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Salary Allocation by Position')
    plt.axis('equal')

    # Pie Chart description
    # calls sb_or_playoffs for string describing how the team did in the playoffs
    plt.figtext(0.5, 0.05, util.sb_or_playoffs(team, year, team_data['playoffs'].iloc[0], team_data['sb'].iloc[0]),
                ha='center', fontsize=14, bbox={"facecolor": "blue", "alpha": 0.4, "pad": 5})
    plt.show()


# strictly for testing function
team_salary_breakdown_pie_chart("Eagles", 2017)