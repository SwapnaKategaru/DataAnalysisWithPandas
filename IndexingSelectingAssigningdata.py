# Importing pandas library
import pandas as pd

data_frame = pd.read_csv("C:/Users/fTablePandas.csv.txt")
print("DataFrame:", data_frame)
""" RESULT
DataFrame:
       #                   Name  Type 1  ... Speed  Generation  Legendary
0      1              Bulbasaur   Grass  ...    45           1      False
..   ...                    ...     ...  ...   ...         ...        ...
445  400                Bibarel  Normal  ...    71           4      False
[446 rows x 12 columns] """

# Access specific column with its attribute
print("Property:")
print(data_frame.HP)
""" RESULT
Property:
0      45
1      60
..     ..
445    79
Name: HP, Length: 446, dtype: int64 """

# Access specific column(having space in heading) with its attribute
print("Property_2:")
print(data_frame['Type 2'])
""" RESULT
Property_2:
0      Poison
1      Poison
...     ...  
445     Water
Name: Type 2, Length: 446, dtype: object """

# Return single specific value
print("Property_3:", data_frame['Type 2'][1])
""" RESULT
Property_3: Poison """


# Select first row of data in DataFrame
print("First_row:")
print(data_frame.iloc[0])
""" RESULT
First_row:
#                     1
Name          Bulbasaur
Type 1            Grass
...                 ...
Legendary         False
Name: 0, dtype: object """


print("loc_1:")
print(data_frame.iloc[:3, 2])
""" RESULT 
loc_1:
0    Grass
1    Grass
2    Grass
Name: Type 1, dtype: object """

print("loc_2:")
print(data_frame.iloc[1:3, 1])
""" RESULT 
loc_2:
1     Ivysaur
2    Venusaur
Name: Name, dtype: object """

print("loc_3:")
print(data_frame.iloc[[0, 1, 2], 0])
""" RESULT 
loc_3:   0    1
         1    2
         2    3
Name: #, dtype: int64 """

print("loc_4:")
print(data_frame.iloc[-5:])
""" RESULT 
loc_4: returns data having [5 rows x 12 columns] """


# Set existing column from table as index(Manipulating index)
print("SetIndex:")
print(data_frame.set_index("Type 1"))
""" RESULT 
SetIndex:
          #                   Name  Type 2  ...  Speed  Generation  Legendary
Type 1                                      ...                              
Grass     1              Bulbasaur  Poison  ...     45           1      False
...     ...                    ...     ...  ...    ...         ...        ...
Normal  400                Bibarel   Water  ...     71           4      False
[446 rows x 11 columns] """


# Conditional selection
print("Condition_1:")
print(data_frame.Name == 'Caterpie')
""" RESULT 
Condition_1:
0      False
       ...  
445    False
Name: Name, Length: 446, dtype: bool """


print("Condition_2:")
print(data_frame.loc[data_frame.Name == 'Caterpie'])
""" RESULT 
Condition_2:
     #      Name Type 1 Type 2  ...  Sp. Def  Speed  Generation  Legendary
13  10  Caterpie    Bug    NaN  ...       20     45           1      False

[1 rows x 12 columns] """


print("Condition_3:")
print(data_frame.loc[(data_frame.Name == 'Caterpie') & (data_frame.Generation >= 2)])
""" RESULT 
Condition_3:
Empty DataFrame
Columns: [#, Name, Type 1, Type 2, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Generation, Legendary]
Index: [] """


print("Condition_4:")
print(data_frame.loc[(data_frame.Name == 'Caterpie') | (data_frame.Generation >= 2)])
""" RESULT 
Condition_4:
       #       Name  Type 1  Type 2  ...  Sp. Def  Speed  Generation  Legendary
13    10   Caterpie     Bug     NaN  ...       20     45           1      False
..   ...        ...     ...     ...  ...      ...    ...         ...        ...
445  400    Bibarel  Normal   Water  ...       60     71           4      False
[281 rows x 12 columns] """


print("Condition_5:")
print(data_frame.loc[data_frame.Name.isin(['Caterpie', 'Pidgeot'])])
""" RESULT 
Condition_5:
     #      Name  Type 1  Type 2  ...  Sp. Def  Speed  Generation  Legendary
13  10  Caterpie     Bug     NaN  ...       20     45           1      False
22  18   Pidgeot  Normal  Flying  ...       70    101           1      False
[2 rows x 12 columns] """


print("Condition_6:")
print(data_frame.loc[data_frame.Generation.isnull()])
""" RESULT 
Condition_6:
Empty DataFrame
Columns: [#, Name, Type 1, Type 2, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Generation, Legendary]
Index: [] """


# Assigning data to a DataFrame
data_frame['fire'] = 'flame'
print(data_frame['fire'])
""" RESULT 
0      flame
       ...  
445    flame
Name: fire, Length: 446, dtype: object """


data_frame['index_back'] = range(len(data_frame), 0, -1)
print(data_frame['index_back'])
""" RESULT 
0      446
1      445
2      444
       ... 
444      2
445      1
Name: index_back, Length: 446, dtype: int32 """
