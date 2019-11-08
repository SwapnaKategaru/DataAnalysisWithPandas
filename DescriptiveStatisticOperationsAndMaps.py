# Importing pandas library
import pandas as pd

data_frame = pd.read_csv("C:/Users/fTablePandas.csv.txt")

# Generates attributes of given column for integers
speed = data_frame.Speed.describe()
print("Speed:")
print(speed)
""" RESULT
Speed:
count    446.000000
mean      67.654709
std       29.803055
min        5.000000
25%       45.000000
50%       65.000000
75%       90.000000
max      180.000000
Name: Speed, dtype: float64 """

# Generates attributes of given column for strings
legendary = data_frame.Legendary.describe()
print("Legendary:")
print(legendary)

""" RESULT
Legendary:
count       446
unique        2
top       False
freq        417
Name: Legendary, dtype: object """

# Check mean of the speeds allotted
Mean = data_frame.Speed.mean()
print("Mean:")
print(Mean)
""" RESULT
 Mean:
67.65470852017937 """

# Find list of unique values in data
uni_value = data_frame.Legendary.unique()
print("Unique_value:")
print(uni_value)
""" RESULT 
Unique_value:
[False  True] """

# Find list of unique value counts
counts = data_frame.Legendary.value_counts()
print("Counts:")
print(counts)
""" RESULT 
Counts:
False    417
True      29
Name: Legendary, dtype: int64 """

# remean the scores
data_frame_speed_mean = data_frame.Speed.mean()
print(data_frame.Speed.map(lambda s: s - data_frame_speed_mean))
""" RESULT:
0     -22.654709
1      -7.654709
         ...    
444   -36.654709
445     3.345291
Name: Speed, Length: 446, dtype: float64 """


# Faster way to remean the Speed column
data_frame_speed_mean = data_frame.Speed.mean()
print(data_frame.Speed - data_frame_speed_mean)
""" RESULT
0     -22.654709
1      -7.654709
         ...    
444   -36.654709
445     3.345291
Name: Speed, Length: 446, dtype: float64 """


# apply() method transforms whole DataFrame by calling custom method on each row.
def remean_speed(row):
    row.Speed = row.Speed - data_frame_speed_mean
    return row


print(data_frame.apply(remean_speed, axis='columns'))
""" RESULT
       #                   Name  Type 1  ...      Speed  Generation  Legendary
0      1              Bulbasaur   Grass  ... -22.654709           1      False
..   ...                    ...     ...  ...        ...         ...        ...
444  399                 Bidoof  Normal  ... -36.654709           4      False
445  400                Bibarel  Normal  ...   3.345291           4      False
[446 rows x 12 columns] """

# Recheck that first row of dataframe(Speed) still has its original value
print(data_frame.head(1))
""" RESULT
   #       Name Type 1  Type 2  ...  Sp. Def  Speed  Generation  Legendary
0  1  Bulbasaur  Grass  Poison  ...       65     45           1      False
[1 rows x 12 columns] """


# Combine selected columns(strings only)
print("Combine:")
print(data_frame.Name + " - " + data_frame.Name)
""" RESULT
Combine:
0                              Bulbasaur - Bulbasaur
                           ...                      
445                                Bibarel - Bibarel
Name: Name, Length: 446, dtype: object """
