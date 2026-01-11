import sys
import pandas as pd

print('args : ', sys.argv)

day = int(sys.argv[1])

df =pd.DataFrame({'m1':[1,2],'m2':[1,3]})
df.to_parquet(f"/app/output/output_day_{sys.argv[1]}.parquet")



print(f'pipeline is running for day {day}')