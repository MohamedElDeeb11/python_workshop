import sys
import pandas as pd

print("args : ", sys.argv)

day =int(sys.argv[1])


df = pd.DataFrame({"users": [1, 2], "employ": [3, 4]})
df['day'] = day
print(df.head())



df.to_parquet(f"output_day_{sys.argv[1]}.parquet")


print(f'pipeline is running for day {day}')