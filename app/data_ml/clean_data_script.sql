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