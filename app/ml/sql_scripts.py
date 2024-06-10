"""
sql_scripts.py
Author: Max Sealey

Every function returns a sql script (string) with cleaned data
"""

# LINE BREAK FOR READABILITY

"""
retrieve_prediction_data_script()

Args: N/A
Ret: script (string) 
Getset dataframe with information used to calculate likelihood of making playoffs
in ml_predict.py
"""
def retrieve_prediction_data_script():
    return '''
      DROP TABLE IF EXISTS relevant_data;

      CREATE TABLE relevant_data (
        team VARCHAR(25),
        season INT,
        playoffs INT,
        qb_p NUMERIC(2, 8),
        off_p NUMERIC(2, 8),
        def_p NUMERIC(2, 8)
      );

        INSERT INTO relevant_data (
        team,
        season,
        playoffs,
        qb_p,
        off_p,
        def_p
      )
      SELECT team, season, playoffs, qb_p, offense_p, defense_p 
      FROM nfl_data
      ORDER BY team;
    '''

# LINE BREAK FOR READABILITY


"""
team_year_pie_chart_script()

Args: N/A
Ret: script (string)
Used to get dataframe with information used to calculate likelihood of making playoffs
"""
def team_year_pie_chart_script(team, year):
    return f'''
      DROP TABLE IF EXISTS relevant_data;

      CREATE TABLE relevant_data (
        team VARCHAR(25),
        season INT,
        playoffs INT,
        sb INT,
        qb_p NUMERIC(2, 8),
        rb_p NUMERIC(2, 8),
        wr_p NUMERIC(2, 8),
        te_p NUMERIC(2, 8),
        ol_p NUMERIC(2, 8),
        idl_p NUMERIC(2, 8),
        edge_p NUMERIC(2, 8),
        lb_p NUMERIC(2, 8),
        s_p NUMERIC(2, 8),
        cb_p NUMERIC(2, 8)
      );

        INSERT INTO relevant_data (
        team,
        season,
        playoffs,
        sb,
        qb_p,
        rb_p,
        wr_p,
        te_p,
        ol_p,
        idl_p,
        edge_p,
        lb_p,
        s_p,
        cb_p
      )
      SELECT team, season, playoffs, sb, qb_p, rb_p, wr_p, te_p, ol_p, idl_p, edge_p, lb_p, s_p, cb_p
      FROM nfl_data
      WHERE team = "{team}" AND season = {year};
    '''

# LINE BREAK FOR READABILITY


"""
div_year_stacked_bar_chart_script()

Args: list of four teams
Ret: script (string)
Used to get dataframe of data for four teams (in a division) used to 
make the stacked bar_chart visual
"""
def div_year_stacked_bar_chart_script(teams, year):
    return f'''
    DROP TABLE IF EXISTS relevant_data;
    
      CREATE TABLE relevant_data (
        team VARCHAR(25),
        season INT,
        qb_p NUMERIC(2, 8),
        rb_p NUMERIC(2, 8),
        wr_p NUMERIC(2, 8),
        te_p NUMERIC(2, 8),
        ol_p NUMERIC(2, 8),
        idl_p NUMERIC(2, 8),
        edge_p NUMERIC(2, 8),
        lb_p NUMERIC(2, 8),
        s_p NUMERIC(2, 8),
        cb_p NUMERIC(2, 8)
      );

        INSERT INTO relevant_data (
        team,
        season,
        qb_p,
        rb_p,
        wr_p,
        te_p,
        ol_p,
        idl_p,
        edge_p,
        lb_p,
        s_p,
        cb_p
      )
      SELECT team, season, qb_p, rb_p, wr_p, te_p, ol_p, idl_p, edge_p, lb_p, s_p, cb_p
      FROM nfl_data
      WHERE team IN ("{teams[0]}", "{teams[1]}", "{teams[2]}", "{teams[3]}")
      AND season = {year};
    '''

# LINE BREAK FOR READABILITY


"""
division_off_def_trends_linegraph_script()

Args: list of four teams, side of the ball (string)
Ret: script (string)
Used to get dataframe of data for four teams (in a division) used to 
make the stacked bar_chart visual
"""
def division_off_def_trends_linegraph_script(teams, side_of_ball_p):

    return f'''
    DROP TABLE IF EXISTS relevant_data;

      CREATE TABLE relevant_data (
        team VARCHAR(25),
        season INT,
        {side_of_ball_p} NUMERIC(2, 8)
      );
      
        INSERT INTO relevant_data (
        team,
        season,
        {side_of_ball_p}
      )
      SELECT team, season, {side_of_ball_p}
      FROM nfl_data
      WHERE team = "{teams[0]}" OR team = "{teams[1]}" OR team = "{teams[2]}" OR team = "{teams[3]}"
      ORDER BY season;
    '''
