import pandas as pd

# get the data first
# already pre loaded things saved as .pickle format
df = pd.read_pickle('C:\\Test\\artwork_csv.pickle')
print(df.columns)

# basic python way to get the unique artists
# add all to set and output its len
unique_artist = set()
for i in df['artist']:
    unique_artist.add(i)
print(len(unique_artist))

# pandas way to do so involves the built in .unique() method that creates a numpy array of all unique values
"""
call .unique() method on pandas and pass in a parameter to check for uniqueness
this produces a numpy array of all unique values
syntax:
pd.unique(<data set to go through>)
then get the length of the array to see amount of all the unique artists
"""
unique_artist = len(pd.unique(df['artist']))
print(type(pd.unique(df['artist'])))
print(unique_artist)

# DEMO 2
# can create an entire data structure (Series) with a statement that compares the artists names
# the result of that comparison is given to each instance tested at
s = df['artist'] == 'Bacon, Francis'
# .value_counts() counts the amount of each instance for each unique value
# this is a series itself of value being counted as row indexes (true or false) and the counts being column
print(s.value_counts())

# or can be dont like
# creates a series of each artist name and the count of how many times they appear in dataset
artist_count = df['artist'].value_counts()
# makes a series with the row indexes being the value being counted and its count as column values (x-y)
print(type(artist_count))
# then goes to the 'Bacon, Francis' row and gets the y value associated
print(artist_count['Bacon, Francis'])

# DEMO 3
print(df.loc[1035, 'artist'], "1")  # print the art piece with id 1035 artist
print(df.iloc[0, 0], "2")  # print the first row with first column value
# comes out in a Serious of the row indexes being the column labels with each corresponding values
# (auto conversions going on), if data coming out data frame goes to either 1 column or row
# it will auto convert to a Series to either represent that Row with columns represented by their values
# or each row represented by its column value (keep in mind)
# this is because each row has this data and it can be represented like this
print(df.iloc[0, :], "3")  # print the first row with all columns, this actually comes out in a Serious
print(df.iloc[0:2, 0:2], "4")  # print the first 2 row [0, 1] with the first two columns [0, 1]

# try multiplication
# area = df['height'] * df['width']
# cannot work because the data in these columns aren't seen as number but object
# but pandas would have used each column instance and multiplied the two of each index
# it couldn't do this either because the input data was dirty, not all numbers
# this is most likely because not all data is a number (possible NaN)
print(type(df['height']))
print(type(df['width']))
# values are all over the place
# .sort_values() sorts the values into classifications based upon data
print(df['width'].sort_values().head())  # head takes a look at a little of the first instances in the data structure
print(df['width'].sort_values().tail())  # tail takes a look at a little of the last instances in the data structure
# the input data isn't perfect and needs cleaning
# need to convert the column data into numeric format and find a way to flag any non given (missing) data
# missing data is common and pandas handles it with Not a Number value or (NaN)

# try to convert data to numeric
# use the .to_numeric() method that takes data with numbers, decimals, constants and converts it to numeric data
# call it on the pandas object and ue the parameter of a Series of data to convert
# the numeric value is float for all values (changes dtype from object to float)
"""
syntax:
pd.to_numeric(df['<column>'])
"""
# pd.to_numeric(df['width'])  # cannot work because of missing data
# pass additional arguments to the to_numeric() method called errors=
# errors= handles any errors thrown and accepts a value of how to handle it
# in this case 'coerce' is used to convert any error to NaN value
"""
syntax:
pd.to_numeric(df['<column label>'], errors='<how to handle>')
"""
print(pd.to_numeric(df['width'], errors='coerce'))
# loc and iloc allow to write to column and replace existing data with brand new data
# to do so access the data that needs to be replaced with loc and set it equal to new data
# in this case it is accessing all the rows' width column values and replacing it with cleaned
# numeric data that has NaN in missing data locations
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')  # new data dtype is float64

print(pd.to_numeric(df['height'], errors='coerce'))
# in this case it is accessing all the rows' height column values and replacing it with cleaned
# numeric data that has NaN in missing data locations
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')  # new data dtype is float64

print(df['width'] * df['height'])  # run correctly meaning the data is clean
print(df['units'])  # the width and height are represented as millimeters

# now have to create new column to represent the area
# create a series of the new values for the area
area = df['height'] * df['width']
# use the .assign() method to add another column to dataFrame
"""
.assign() is called on the data frame to be added to with a default value that will be the column label 
set to the series of data that will go into this column, all set equal to the same dataFrame returning a new dataFrame       
syntax:
df = df.assign(<label of column>=<column data>)
"""
# in this case the area is found by multiplying the new datasets for width and height and set to a series called area
# area is then called in .assign() method where its label will be area
df = df.assign(area=area)

print(df['area'].max())  # built in max method that gets highest numeric value in 'area' column
print(df['area'].idxmax())  # .idxmax() gets the index of row that has the .max() method
# using .idxmax() to display the data for the artwork with the max
# using it in loc to get the row auto Series for a row object with all column data
print(df.loc[df['area'].idxmax(), :])

# additional column labels after condition will output a data structure of the
# column name values for every row that condition is true
s = df.loc[df['artist'] == 'Blake, William', 'title']
print(s)
