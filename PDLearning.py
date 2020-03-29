import numpy as np
import pandas as pd
(print("Start"))
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates=pd.date_range('20130101', periods = 6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list(["Apple","Banana","Chocolate","Car"]))
print(df)

#1the next set of dataframe is made for strings that turn to columns
print("Exercise1")
dates=pd.date_range('20130101', periods = 6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("EFGH"))
print(df)

#turn dictionaries into a Series
df2 = pd.DataFrame({"A":1.,
                    'B':pd.Timestamp('20200101'),
                    'C':pd.Series(np.random.randn(), index=list(range(4)), dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","test2","test3","test4"]),
                    'F':"foo"})
print(df2)
print(df2.dtypes)

#2printing top and bottom of data
print("Exercise2")
print(df.head())
print(df.tail(3))

#4.1 this is actually after 4, to see what dtypes come up with using just pandas
print("Exercise4.1")
print(df.dtypes)
print(df2.dtypes)

#3displaying index and column
print(3)
print(df.index)
print(df.columns)

#4moving dataframes to numpy
print("Exercise4")
print(df.to_numpy)
print(df.dtypes)

print(df2.to_numpy)
print(df2.dtypes)

print("explanation for why use NumPy arrays, instead of Python when dealing with stats in the notes section")
'''
Why use NumPy Arrays?
NumPy is meant for creating homogeneous n-dimensional arrays (n = 1..n).
Unlike Python lists, all elements of a NumPy array should be of same type.
so the following code is not valid if data type is provided
numpy_arr = np.array([1,2,"Hello",3,"World"], dtype=np.int32)  # Error

However, for python lists, this is a valid code
py_arr = [1,2,"Hello",3,"World"]  # Valid Code

NumPy arrays are made to be created as homogeneous arrays,
 considering the mathematical operations that can be performed on them.
 It would not be possible with heterogeneous data sets.
 https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121
'''

#5 describing the data as in mean, median, etc.
print("Exercise5")
print(df.describe())

#6 transposing data
print("Exercise6")
print(df)
print(df.T)

#7Sorting data by row
print("Exercise7 this will sort by column it seems")
print(df.sort_index(axis=0,ascending=False))

#8Sorting by column
print("Exercise8 sorting by column")
print(df.columns) #this will show the column names
print(df.sort_values(by='F',ascending=False)) #this will show what column name to sort by

#9 isolating data dataframes
print("Exercise9 isolating columns, and printing just one column")
print(df.E.sort_values(ascending=False))
print(df.sort_values(by='E',ascending=False))
print(df.E)

#10 slicing rows up, not columns. splitting rows.
print("Exercise10 splitting rows up")
print(df["20130101":"20130105"])
print(df[0:3])
print(df.iloc[:, 0]) #tried to isolate the first columns

#11 Selection by label
print("Exercise11 Selection by label (so row 0 for example)")
print(df.loc[dates[2]]) #this is actually row 4 in Excel. in pandas 0 = first row where array is

#SideStep1 Understanding data frames using Pandas, constructing
df3=pd.DataFrame([[1,2],[3,4],[5,6]],index=['John','Bon','Bovine'],columns=['Jack','Jill'])
'''
Square brackets are lists, they can be changed. Parentheses "()" are tuples, and cannot be changed.
Single label. Note this returns the row as a Series.

df.loc['viper']
max_speed    6
shield       5
Name: viper, dtype: int64
List of labels. Note using [[]] returns a DataFrame.

df.loc[['viper', 'sidewinder']]
'''
print(df3)

#12
