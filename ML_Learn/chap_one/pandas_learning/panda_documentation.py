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
"""
# testing_one.py
this gets the data as csv and prints out a simple statement for each piece of artwork
"""
"""
# testing_two.py
this gets the data in the json files and uses a recursive function to get all the data from the subject
category, the children and other none nested things.
stores all its subjects (details about painting) as key-value pairs to their detail id and name of detail in a dict.
some no subjects or ids and stop it reaches a certain statement.
huge amount of data gotten and saved.
"""

# OPERATIONS ON GROUPS
"""
showing why to use this api in cases
iterate groups, group things based on column values (like a lot of things have similar width and such)
built in methods to increase work flow
"""

# MOTIVATION
"""
apparently no explanation, just get it from examples
(kinda should be the other way around)
"""
# aggregation
"""
if wanted to find the firs acquired artwork, would use .min() function on acquisitionYear column
though if wanted to find the first of every artist would need to use grouping

you would need to split the data by each unique artist, grouping together all data with the same 
artist, (including acquisitionYear)
group data by a certain value and return 1 value for each group is called (aggregation)
AGGREGATION
family of operations (research some)
"""
# transformation
"""
if was going though data on artists artwork and some data was missing (medium for example)
we could just replace this missing data with a flag it is missing.
though another way to fill this missing value is to group together a certain data value (artist name)
and find the most common piece of data in this column to fill it in with (most common medium he used)

TRANSFORMATION
take the dataFrame, split into groups based on certain data value, then perform some computation on data
and return a group/dataFrame that is the same size with data changed based on those computations
"""
# filtering
"""
in the artwork dataFrame there are some titles that repeat, group all titles together and just look
at data where only groups are more than 1 long (some have repeating titles)
then to look specifically to the rows where there are more than 1 row of data, drop the rest of the 
groups that don't follow this format of more than 1

FILTERING
getting specific data from the frame and getting rid of the rest that aren't that data
"""

# ITERATING OVER GROUPS
"""
to organize data into groups based on single column value
use the .groupby('<column name>') method
call the pandas dataFrame and call the method .groupby('<column name>') on it to organize it by that column name
this method returns the data on the groups and what each was organized by
can get each group organized into as well as the data in dataFrame
returns a tuple of what the grouped value was and its good
can be used in a for loop (returns subsets of dataFrame) as example:
for name, group in df.groupby('artist'):
name ==== the name of the artist the group is grouped by
group ==== the data of the group, all other data including artist names
"""
# demo for aggregation
# go over all artist groups (grouped by name)
# get the date for each first acquisition
# fill in some missing values
# groups_demo.py
"""A LESSON LEARNED IS LOOK UP SPECIFIC STUFF ON PANDAS TO SEE IF THERE ARE ANY METHODS FOR IT"""

# BUILT-IN METHODS
# saw in groups_demo.py that using for loops with groups, the data could be analyzed with transformations in mind
"""
in the previous groups_demo.py, to transform data used each group
analyzed each dataset to alter the missing data
"""
# pandas allows the ability to get a grouped dataFrame with specific columns in mind
# to do this after using the .groupby('<group value>') method specify the columns [<columns value>]
# syntax:
# df.groupby('<group value>')['<values to get/columns>']
# this gets the grouped dataFrame and then gets only the columns requested
# this is used instead of going through a loop and getting only the 'medium' from each subset
# working with .transform(<custom transforming function>)
"""
this takes a custom transforming function as a parameter
it returns the return from custom function
does any transformation and returns the data
if working with a specific data can return the data back into its place with loc or iloc
syntax:
df[:, '<column>'] = df['<column>'].transform('<transforming function>')
# or
df = df.transform('<transforming function>')
"""
# aggregation built-ins
# in another case in groups_demo.py found minimum values for each artist
# use the .agg() method
# this takes any function that takes input of a series and returns a single value
# (np.min) is a numpy function that takes a series and returns the minimum
"""
syntax:
ex = df.groupby('<group value>')['<column>'].agg(<function that takes each group series of column and returns a value>)
"""
# in pandas, there are some aggregate functions like .min()
# this will take a dataFrame and go through each aggregation and return a single value for each
"""
syntax:
ex = df.groupby('<group value>')['<column>'].min()
"""
# filtering built-ins
# in the case of looking for duplicate titles
# the filter requires a condition function (or something that is a condition function)
# this is quick when using a lambda function
"""
syntax:
condition = lambda <return>: <case>
ex:
condition = lambda x: len(x.index) > 1
"""
# then use the .filter(<conditional>) to filter the data and return the data that only are true in condition
"""
possibly lambda function could be conditional function
syntax:
ex = df.filter(<conditional function>)
"""
# demo
# called built_demo.py
# perform aggregation, transformation and filtering using built in methods
# will be less complicated code because more will be going on in the background
# TIMESTAMP - 2:15



