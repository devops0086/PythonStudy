import numpy as np
import pandas as pd
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates=pd.date_range('20130101', periods = 6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list(["Apple","Banana","Chocolate","Car"]))
print(df)

#the next set of dataframe is made for strings that turn to columns
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
