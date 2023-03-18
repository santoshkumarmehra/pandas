import pandas as pd 

data = [1,2,3,4]
series_data = pd.Series(data)
# print(series_data)
# print(type(series_data))
# print(series_data[0])
# for val in range(len(series_data)):
#     print(series_data[val])


# data = [1,2,3,4]
# series_data = pd.Series(data, index=["x","y","z","@"])
# print(series_data)
# print(series_data["x"])
# print(type(series_data))


# data = {"day1":120, "day2":130, "day3":140}
# series_data = pd.Series(data)
# print(series_data)

# data = {"day1":120, "day2":130, "day3":140}
# series_data = pd.Series(data, index=["day1", "day2"])
# print(series_data)


# data = [1,2,3,4,"santosh"]
# series_data = pd.Series(data)
# print(type(series_data))


# data = {"day1":120, "day2":130, "day3":'ssss'}
# series_data = pd.Series(data, index=["day1", "day2"])
# print(series_data)


# dataframe

# data = {"day1":[1,2,3], "day2":["x","y",2]}
# df = pd.Series(data)
# print(df)


# data = {"day1":[1,2,3], "day2":["x","y",2]}
# df = pd.DataFrame(data)
# print(df)

data = {"cal":[20,15,18], "duration":[8,5,10]}
series = pd.DataFrame(data)
print("\n",series)

