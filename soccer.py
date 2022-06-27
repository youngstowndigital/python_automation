import pandas as pd

df_premier21 = pd.read_csv('https://football-data.co.uk/mmz4281/2122/E0.csv')

df_premier21.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)

print(df_premier21)
