import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# loads data to pandas dataframe
csv = 'nfl_data.csv'
df = pd.read_csv(csv)

# connect to database
conn = sql.connect('../../data/nfl_data.db')
cursor = conn.cursor()

# convert dataframe to sql table
df.to_sql('nfl_data', conn, if_exists='replace', index=False)

conn.commit()

# cleaning and preparing data by creating a new table with only relevant information
new_table_script = '''
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

cursor.executescript(new_table_script)
conn.commit()

# reading relevant data into dataframe to be used in ML model
q = 'SELECT * FROM relevant_data'
df = pd.read_sql_query(q, conn)

conn.close()

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

# predicts labels on the scaled test set and stores in y_pred
y_pred = model.predict(X_test_scaled)

# compares predictions vs test results
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}\n')
print('Classification Report:\n', class_report)
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
results_df['Correct Prediction'] = results_df['Actual'] == results_df['Predicted']
print("")
print("Actual vs Predicted Outcomes:")
print(results_df.head(20))
print("")

# confusion matrix visualization
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d', xticklabels=['No Playoffs', 'Playoffs'], yticklabels=['No Playoffs', 'Playoffs'])
plt.xlabel('Predicted Outcomes')
plt.ylabel('Actual Outcomes')
plt.title('NFL Playoff Predictor Confusion Matrix')
plt.show()