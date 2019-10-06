# testing pandas out here
"""
pandas documentation - "https://pandas.pydata.org/pandas-docs/stable/"
pandas course on pluralsight (PANDAS FUNDAMENTALS)
folder pandas_learning
"""

# OVERVIEW
# data input and output
# indexing and filtering data
# working with groups
# creating plots

# GETTING STARTED
"""
expect topics like:
data types
I/O capabilities (think this is like when I got .csv)
operations on groups
data filtering 
plotting
"""

# __THE DATASET__
# best to work with real public datasets
# working with:
# "Tate Collection metadata"
# this contains about 70,000 artworks and is available as json or csv.
# "https://github.com/tategallery/collection"
# data is very introductory

# BASIC OBJECTS
"""
import statements:
import pandas as pd - pandas object is being imported and renamed because it contains a function called pandas
import numpy as np - numpy object is being imported and renamed because it contains a function called numpy
"""
# numpy isn't necessary but some attributes and methods make working in pandas easier
# both add new data types:
"""
from numpy:
np.array / np.ndarray
array is a basic numpy array (not sure what is special about it) - its just a simple list
but ndarray can have n dimensions 3rd,4th ... dimensional arrays/lists, not confusing concepts but easier to make
from pandas:
pd.series - dataset with a single column (I think like x - y)
pd.DataFrame - dataset with multiple columns (I think like x - y - x - ...)
"""
# numpy array - this is a list
"""
syntax:
the np object with attributes called on it 
possibly:
np.attribute.method(input)
"""
# numpy has built in random functions
"""
called on np object to create a list of random objects
np.random.rand(input)
"""
# EX:
# made with 3 random elements
import numpy as np

numpy_array_ex = np.random.rand(3)
print(numpy_array_ex)
# or
import random as ran


def rand_array(amount, i=0):
    narray = list()
    while i < amount:
        narray.append(ran.random())
        i += 1
    return narray


numpy_array_ex = rand_array(3)
print(numpy_array_ex)
# panda Series - the one column (I think like a typical graph)
"""
use pd object and call Series attribute and methods accordingly
pd.Series()
output format is:
x     y
0     324
1     435
.........
"""
# EX:
# made with 3 random elements
import pandas as pd

pd_series = pd.Series(np.random.rand(3))
"""
in this context it acts as 3 elements in the np array makes 3 sequences in the series
"""
# acts as a table you would see in a graph
# x is incremented by 1 and left is the input into series or y
print(pd_series)

# pandas DataFrame
"""
syntax:
pd object followed by DataFrame attribute and methods accordingly
pd.DataFrame()
output is:
      0       1
0     234     235
1     34      90
2     2354    8456
.................
"""
# EX
# this example is creating two columns of random numbers
# the amount of dimensions in the numpy array corresponds to the amount of columns
second_array = np.random.rand(3, 2)
print(second_array)  # 2nd dimensional list/array
pd_dataFrame = pd.DataFrame(second_array)
print(pd_dataFrame)
# thinking about it differently
"""
regular numpy arrays are similar to lists, just a sequence of data
then putting that array into a series, we got row labels to all sequences of data (like x-y)
or by putting that possibly multi dimensional array in a dataFrame we get row label and column labels for all sequences
(this could be x-y1-y2 (this could technically map multiple dimensions of data but another axis would have to be added 
for each new column))
"""

# DEMO
"""
creating series object (just row)
creating dataFrame object (x-y1-y2)
inspect properties (see what can be seen and manipulated)
"""

# go to pandas_demo_ex.py

# EXPLORING PANDAS DATA INPUT CAPABILITIES
# explore formats that pandas can handle (csv, xls, txt...)
# starting to work with dataset by taking
# tate dataset: CSV and formatting it on the fly
# try to get similar results with the
# tate dataset: JSON
# learn to work with pandas input api (the syntax, properties, defaults, etc...)

# PANDAS COMPATIBLE DATA FORMATS
"""
the different data sources:
(three types of input and output)
-text files (txt,csv,tsv)
-binary (when need to work with other software formats (not supported types like-xls)) 
 to get a direct xls it must be in binary. also useful for io performance (guessing it 
 can optimize data used and suck (not sure))
-relational databases (read data from relational databases (sql and (maybe access)))
"""
"""
text formats:
-csv (comma separated values) (have already actually used getting this in ML exercise)
 separator does not always have to be comma, can be tab
-json (nest objects instead of flat format like csv (a column inside column???))
-html table (comes in handy when getting data from an online web page) 
"""
# if built in methods don't support need can build own and cast data to python objects like lists, tuples, dicts...
# think the numpy examples from before
# think over thinking this (just means not all data has to be in these supported formats
# but can just be stored in data types)
# (has something to do with casting to python objects (research this))
# think it just means if method wont work well just write your own method to get data into a python object

# TATE COLLECTION METADATA: TAKE ONE
# fist try to interpret all the artwork data stored in one .csv file
# go to file "metadata_part_o.py"

# TATE COLLECTION METADATA: TAKE TWO
# fist try to interpret all the artwork data stored in json
# go to file "metadata_part_t.py"

# NO TESTING YET
# won't do testing until after next module so I have something other than just getting data into the python
# when testing want to get csv and json and work with both, like they can both have different functions but lead
# to creating the same dataFrame and then work on that dataFrame
# maybe what is the most complicated artwork (most descriptive, taking in character count/commas)
# i think this has something to do with children

# INDEXING AND FILTERING
# cleaning up code and data
# typical questions when selecting data/filtering
# getting the right data, (learn methods pandas provides)
# also see that data isn't always clean and have to deal with unexpected cases
# best ways to select data in pandas and best strategies to avoid errors
"""
the task:
-how many distinct artists are there in the dataset?
-how many artworks by Francis Bacon are there?
-what is the artwork with the biggest dimensions (area)?
"""

# THE BASICS
"""
# column selection:
# can get a specific column from df by use of label
# this will return a Series from a DataFrame since it has just one column
syntax:
df['<column name>']
# can also pass a list of column labels for multiple columns to be selected
# this will now return DataFrame because it has multiple columns (y's)
syntax:
df[['<column name 1>', '<column name 2>']]
# another way to select a column in pandas
# can use the dataFrame attribute of the column name
syntax:
df.<column name>
# THOUGH this is discouraged (avoid it) because its results vary (little weird)
"""
# column selection from a larger dataFrame can help micro manage segments of the data

# DEMO 1
# going through first task
# -how many distinct artists are there in the dataset?
# count the number of distinct artists in the dataset
# go to demo_indx&filt.py

# FILTERING
# logical test on values
# like doing a logic test on an excel table
# filter row values out if condition is true of false
"""
df['artist'] == 'Bacon, Francis'
in this case if the artist was not 'Bacon, Francis' their name on the dataset would
be false while if they are it would be true
artist column would be true and false checking if it was that name
the result would be a new series with bool in the artist column whether each is true
the new series would have same labels as source but would be just the artist and rows (x-y)
"""

# DEMO 2
# second task
# count how many artworks by Francis Bacon
# use the .value_counts() method to return a series of value row and count column
# use the bool test to make a series of bool of each comparison in a set
# go to demo_indx&filt.py

# INDEXING DONE THE RIGHT WAY
"""
code may start looking clumsy
may start to be inconsistent, getting errors and such
could get unexpected results and data
doing it the right way means a more consistent way
"""
# working with more consistent attributes work with:
# 'loc' and 'iloc'
"""
allow to get data in a more consistent way
loc gets data by labels
iloc gets data by position
"""
# labels vs positions
"""
row labels are just row names set as indexes when reading file
column labels are just column names
(both are just names of the indexes they represent)
positions are zero based index, start from zero and go up (row and columns)
"""
# loc
"""
call loc on a dataFrame object
put desired labels in square brackets
in the first place before comma is the row indexer 
in the second place after comma is the column indexer 
syntax:
df.loc[<row index label>, <column label>]
this is a reliable approach from getting out of dataFrame
though loc is much more powerful
for example it can have another data structure in itself like Series
it can use conditional statements learned from before to add Series of true and false in
syntax:
df.loc[df[<column label> == 'value'], :]  # (colon means all) slice from the start to end
"""
# iloc
"""
works same as loc but works with positional values instead
in differing cases other than the ones presented in the loc 
can work with slices and lists of items
syntax:
df.iloc[<index start>:<index stop>, [<list of indexes>]]
or 
df.iloc[:, [<list of indexes>]]  # colon means everything because it is a slice from the start to end
syntax:
df.iloc[<row index>, <column index>]
syntax:
df.iloc[df[<column index>] == 'value', :] # colon means everything, slice from the start to end
"""

# DEMO 3
"""
-practice with loc and iloc
-find the biggest artwork in collection of data
-learn how to deal with common problems in data analysis
"""
# go to demo_indx&filt.py

# DOS AND DON'TS
# indexing and filtering is one of the most important part of analyzing data
# working with the data structures, cleaning data, getting indexes/columns, filtering, adding new data, etc...
# learned that when working with a full column, any operation happens on all the data within never the column itself
# best strategies:
# "always use iloc and loc"
# most reliable and will not give unexpected results (can use it most times while shorthand won't always work)
# difficult to access row without loc or iloc
#
"""
rare exceptions to this would be:
accessing an column
df['<column label>']
accessing multiple columns in a list
df[[<list of column labels>]]
filtering data into a filtered new dataFrame/Series
df.loc[df[<column name>] == '<attribute to test for 1>', '<value to output for true condition>']
"""
# things to avoid:

# TESTING
# will do testing, look back at all stuff and do something
# look at previous testing section

# OPERATIONS ON GROUPS



