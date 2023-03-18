import pandas as pd
# print(pd.__version__)

# data = [1,2,3]
# series_data = pd.Series(data)
# print(series_data)

# data = {"day1":120, "day2":130, "day4":140}
# series_data = pd.Series(data, index=["day1", "day2"])
# print(series_data)


# data ={"day1":[1,2,3,4], "day2":[12,13,14,15]}
# df = pd.DataFrame(data, index=["x","y","z","v"])
# print(df.loc[["x","y"]])


# csd_data = pd.read_csv('data.csv')
# print(csd_data.to_string())

# csv_data = pd.read_csv('dirtydata.csv')
# print(csv_data)

# csv_data = pd.read_csv('dirtydata.csv')
# clndata = csv_data.dropna()
# print(clndata.to_string())

# csv_data = pd.read_csv('dirtydata.csv')
# clndata = csv_data.dropna(inplace=True)
# print(clndata) //error

# data = pd.read_csv('dirtydata.csv')
# data1 = data.fillna(120)
# print(data1.to_string())


# data = pd.read_csv('dirtydata.csv')
# x=data["Calories"].mean()
# data["Calories"].fillna(x,inplace=True)
# print(data)

# data = pd.read_csv('dirtydata.csv')
# x=data["Calories"].median()
# data["Calories"].fillna(x,inplace=True)
# print(data)

# data = pd.read_csv('dirtydata.csv')
# x=data["Calories"].mode()[0]
# data["Calories"].fillna(x,inplace=True)
# print(data)



# data = pd.read_csv('dirtydata.csv')
# data["Date"] = pd.to_datetime(data["Date"])
# print(data)

data = pd.read_csv('dirtydata.csv')
data["Date"] = pd.to_datetime(data["Date"])
data.dropna(subset=["Date"], inplace=True)
print(data)