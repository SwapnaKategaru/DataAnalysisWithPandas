# Importing pandas library
import pandas as pd

# Creating a DataFrame
integers = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print("Integers:", integers)
""" RESULT
a:    Yes   No
   0   50  131
   1   21    2 """

# DataFrame with string values
strings = pd.DataFrame({'Bob': ['I liked it.', 'It is awful.'], 'Sam': ['Pretty good.', 'Bland.']})
print("Strings:", strings)
""" RESULT
Strings:        Bob           Sam
         0    I liked it.   Pretty good.
         1   It is awful.         Bland. """

# Row labelling with index parameter
index = pd.DataFrame({'Bob': ['I liked it.', 'It is awful.'],
                      'Sam': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
print("Index:", index)
""" RESULT
Index:                Bob           Sam
       Product A    I liked it.  Pretty good.
       Product B   It is awful.        Bland. """

# Return series of data
series = pd.Series([1, 2, 3, 4, 5])
print("Series:", series)
""" RESULT
Series: 0    1
        1    2
        2    3
        3    4
        4    5
        dtype: int64 """

# Column labelling with index parameter
name = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print("Name:", name)
""" RESULT
Name: 2015 Sales    30
      2016 Sales    35
      2017 Sales    40
      Name: Product A, dtype: int64 """

# Read the data into a DataFrame
data_frame = pd.read_csv("C:/Users/fTablePandas.csv.txt")

print("DataFrame:")
print(data_frame)
""" RESULT
DataFrame:
       #                   Name  Type 1  ... Speed  Generation  Legendary
0      1              Bulbasaur   Grass  ...    45           1      False
1      2                Ivysaur   Grass  ...    60           1      False
2      3               Venusaur   Grass  ...    80           1      False
..   ...                    ...     ...  ...   ...         ...        ...
444  399                 Bidoof  Normal  ...    31           4      False
445  400                Bibarel  Normal  ...    71           4      False

[446 rows x 12 columns] """


# Shape attribute to check DataFrame shape
print("Shape:", data_frame.shape)
""" RESULT
Shape: (446, 12) """


# Return first five rows
print("Head:")
print(data_frame.head())
""" RESULT
Head:
   #                   Name Type 1  ... Speed  Generation  Legendary
0  1              Bulbasaur  Grass  ...    45           1      False
1  2                Ivysaur  Grass  ...    60           1      False
2  3               Venusaur  Grass  ...    80           1      False
3  3  VenusaurMega Venusaur  Grass  ...    80           1      False
4  4             Charmander   Fire  ...    65           1      False

[5 rows x 12 columns] """


# Return indexed column as 1st column
data_frame = pd.read_csv("C:/Users/fTablePandas.csv.txt", index_col=2)
print("Index:")
print(data_frame.head())
""" RESULT
Index:
        #                   Name  Type 2  ...  Speed  Generation  Legendary
Type 1                                    ...                              
Grass   1              Bulbasaur  Poison  ...     45           1      False
Grass   2                Ivysaur  Poison  ...     60           1      False
Grass   3               Venusaur  Poison  ...     80           1      False
Grass   3  VenusaurMega Venusaur  Poison  ...     80           1      False
Fire    4             Charmander     NaN  ...     65           1      False
[5 rows x 11 columns] """