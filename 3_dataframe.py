import pandas as pd

# data = {"cal":[480, 320, 540], "dur":[50,35,47]}
# df = pd.DataFrame(data)
# print(df)
# print((type(df)))

# data = {"cal":[480, 320, 540], "dur":[50,35,47]}
# df = pd.DataFrame(data)
# print(df.loc[0])


# data = {"cal":[480, 320, 540], "dur":[50,35,47]}
# df = pd.DataFrame(data)
# print(df.loc[[0,1]])

# data = {"cal":[480, 320, 540], "dur":[50,35,47]}
# df = pd.DataFrame(data, index=["day1", "day2","day3"])
# print(df)

data = {"cal":[480, 320, 540], "dur":[50,35,47]}
df = pd.DataFrame(data, index=["day1", "day2","day3"])
print(df.loc["day2"])


data = {"cal":[480, 320, 540], "dur":[50,35,47]}
df = pd.DataFrame(data, index=["day1", "day2","day3"])
print(df.loc[["day2", "day1"]])

