import pandas as pd

data_path = "Data\\LOL_champions_stats.csv"

data = pd.read_csv(data_path)

print(data)