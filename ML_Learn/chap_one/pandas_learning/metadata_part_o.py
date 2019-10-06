import pandas as pd

"""
look into the artwork_data.csv file
looking into it see that it has attributes like, not limited to:
id, accession_number, artist, artistRole....
Each corresponds to some data about an art piece
these attributes act as descriptive columns for entire data set to follow

csv is a first class format in pandas (treated as the best)
to read a csv file use the pandas object and call a method:
syntax:
read_csv(<file path/name>.csv)
"""

"""
in example:
- load csv file artworks, makes a dataFrame
- inspect the dataFrame made
- avoid reading redundant data (data of the same or uselessness)
"""

# use os to get the path name from system
# could not get using the build in path finder join method to work
# NEED MORE RESEARCH ON THIS
# import os
# path = os.path.join('..', 'Test', 'artwork_data.csv')
# print(path)

# get the csv file and make it a data frame
# use nrows=<number> to get only a certain amount of full rows (all columns)
artwork_csv = pd.read_csv('C:\\Test\\artwork_data.csv', nrows=5)
# use the to_string() method call on any string to see the entire string (gets reduced when files get too large)
print(artwork_csv.to_string())

# use index_col=<label>
# many of these things only work in this method call
# uses the specified column as the row indexes (the column indexes are treated the same way as rows)
artwork_csv = pd.read_csv('C:\\Test\\artwork_data.csv', nrows=5, index_col='id')
# technically not seen until now but this makes the rows column act as a column in itself (labeled)
# before even when changing rows labels, couldn't add a label for all the column
print(artwork_csv.to_string())

# can also begin limiting columns
# use the usecols=[<any necessary columns>, <column label>...]
# this has to be a list of column labels
# cannot exempt any necessary columns like the index column, must include it in this list
artwork_csv = pd.read_csv('C:\\Test\\artwork_data.csv', nrows=5, index_col='id', usecols=['id', 'artist'])
print(artwork_csv.to_string())
# are able to actually use column positions (0 based index to access the columns)
# though not able to mix labels and indexes
artwork_csv = pd.read_csv('C:\\Test\\artwork_data.csv', nrows=5, index_col=0, usecols=[0, 1])
print(artwork_csv.to_string())

# more columns to into using more of the data
# create a list of all labels of columns to use
# then use this in the usecols= because it accepts a list of labels/positions
columns_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear',
                  'height', 'width', 'units']
artwork_csv = pd.read_csv('C:\\Test\\artwork_data.csv', index_col='id', usecols=columns_to_use)
print(artwork_csv.to_string())
# getting the data produces issue:
# sys:1: DtypeWarning: Columns (9,13) have mixed types. Specify dtype option on import or set low_memory=False.
# this error means there is some trash data within some columns like width creating data issues (for example strings)
# don't worry about this data right now
# work with it in next module when working with these special columns

# to save this data for later for later use
# use the pandas object to be saved with method "to.pickle(<save to what path>)"
# syntax:
# <object to be saved>.to_pickle(<path to save>.pickle)
artwork_csv.to_pickle('C:\\Test\\artwork_csv.pickle')
"""
pickle is a native python format for serialization (not sure)
in this case it just means writing and reading python formats to and from a drive
"""

# could get this pickle back with the pandas read_pickle() method
# works the same as a pandas read_csv
artwork_csv = pd.read_pickle('C:\\Test\\artwork_csv.pickle')
print(artwork_csv)










