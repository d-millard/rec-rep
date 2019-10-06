import numpy as np
# first create array with 3 random numbers using narray and built in methods
# numpy is strictly for narray objects
three_ran_narray = np.random.rand(3)
# see that it created a narray
print(three_ran_narray)
# know that it is an narray by checking type
print(type(three_ran_narray))
# array has indexing just like any other list
print(three_ran_narray[0])
# or
for i in three_ran_narray:
    print(i)
import pandas as pd
# to make a series panda (pd) must be specified as object and the attribute Series must be called
# pandas works with more than one data type (isn't built around just one like numpy) but it uses narrays
three_ran_series = pd.Series(three_ran_narray)
print(three_ran_series)
# the row labels are indexes
print(three_ran_series[0])  # this is the index 0, or row 0
# can specify the indexes with the Series constructor
# allows custom labels for each row
"""
syntax to specify index is:
index=[data structure that contains the labels (goes in order)]
"""
three_ran_series = pd.Series(three_ran_narray, index=["First", "Second", "Third"])
print(three_ran_series)
# now can access indexes with the labels
print(three_ran_series["Second"])
# but can still use 0 based indexing (built in to data type)
print(three_ran_series[1])
# built in nice output
# can use .index attribute to access the indexes for the array (the row labels)
# this is an array of labels
print(three_ran_series.index)

# creating a random array with 2 columns now (x-y1-y2) (this is dataFrame in pandas, but just a 2d array in general)
# first number is amount of arrays (rows) (length)
# the second is the amount of items in each array (width)
# row and column (x and y)
rand_td_array = np.random.rand(3, 2)
print(rand_td_array)
# can access these like any 2 dimensional array using indexing
# use first index to specify witch array and second witch item
print(rand_td_array[0, 1])
# do the same methodology as Series, but because now using multi dimensions it is a dataFrame
# since pd works with multiple types use the pd object and specify the DataFrame attribute
# use df for shortcut reference to dataFrame (widely accepted)
df = pd.DataFrame(rand_td_array)
print(df)
# like specifying index property "example.index"
# can also specify columns property with a dataFrame
print(df.columns)
# can manipulate index labels with this as well just like with a Series (index=[data structure])
# though with the introduction of columns, can manipulate they're labels as well with the columns keyword
"""
syntax to alter column labels:
columns=[data structure]
"""
df = pd.DataFrame(rand_td_array, index=["First", "Second", "Third"], columns=["First", "Second"])
print(df)
# cannot access individual elements with 0 based index
"""
print(df[0, 1])  # this does not work
"""
# use this instead
# cannot access with positions
# columns first then rows, first y, then x
print(df["First"]["Third"])
# changing the column labels alters the columns property a bit
# makes it instead of rangeIndex an Index
# it also outputs all labels
print(df.columns)
# same format as index property
print(df.index)
# attributes can abe mutated from outside the constructor
# using the attributes on object and setting equal to the new value
df.columns = ["F", "S"]
# and
df.index = ["F", "S", "T"]
print(df)
# can access single rows and columns with the labels
# the first column (cannot use indexes to access this)
print(df["F"])
# can then access rows with the column selected with another [] index/label grab
# this one can use labels AND indexes
print(df["F"][1])
print(df["F"][1])
# or
print(df["F"]["S"])








