import pandas as pd
import numpy as np


columns = ['id', 'artist', 'acquisitionYear', 'medium', 'title']
df = pd.read_csv('C:\\Test\\artwork_data.csv', index_col='id', usecols=columns)
# using the .copy() method when getting data from another df
# splitting the data with the iloc[], a range of rows and all columns
df = df.iloc[49980:50019, :].copy()

# groupby returns all groups and their group by values in a dataFrame
# looping through (instead of regular df returning each row and its column (useful info maybe))
# returns each value grouped by and the sub dataFrame of all data that were grouped by the value
# these are returned within a tuple (allowing tuple unpacking)
for name, group in df.groupby('artist'):
    # the group returned is a natural dataFrame as it would have existed within the other dataFrame
    print(type(group))
    # the .min() method gets the minimum value for the data called upon
    year = group['acquisitionYear'].min()
    # the unpacked values are treated as any other values
    print(f'{name}: {year}')


# TRANSFORMATION
# fill the missing medium values with most frequent values
# take a series as attribute (medium column passed)
def fill_value(series):
    # counts the amount of values for each unique instance in a series (would not work with dataFrame)
    # returns a series of the unique values as x and the counts for each one as y
    # using this with transformation you could compare each value and see what is the most counted (used)
    # and then get the value for that one and replace any with missing data or NaN values
    # the value_counts returns these values in a descending order with the first being the most counted
    values_counted = series.value_counts()
    # the .empty() attribute is a boolean of if the series of frame has data within it
    # if there is no data it will return true
    # if all data is missing, no data can be inferred off and data must stay the way it is
    if values_counted.empty:
        # returns the series because can't do anything else with it
        return series
    # the first row in the .value_counts() series is the one of most counted
    # use the .index[i] to get any row, .index returns all rows
    most_freq = values_counted.index[0]
    # make a new series with all missing data filled with the most counted medium
    # use the .fillna(<fill with>) to fill in all NaN data (missing data)
    new_medium = series.fillna(most_freq)
    return new_medium


# the entire dataFrame is broken into artist groups
# must go over all the artist groups and fill in their missing data
def transform_df(source_df):
    # list of all groups of artists
    group_dfs = []
    # loop through each group of artist
    for name_, group_ in df.groupby('artist'):
        # .copy() performs a deep copy of data structure (df)
        # deep copy each dataFrame of data in each group to filled_df
        filled_df = group_.copy()
        # set all rows of medium column equal to the filled data processed in the previous function
        # taking the medium column series and counting the most frequent data and filling in any NaN data with it
        filled_df.loc[:, 'medium'] = fill_value(group_['medium'])
        # finally appending the new filled artist group to the list of artist groups
        group_dfs.append(filled_df)

    # make an entirely new dataFrame
    """
    use the .concat() to take a list of groups of a dataFrame and 
    add them together to create one large frame again, but it will now be 
    filled with artists' frequent medium values and grouped together by artist
    call the pandas object and then .concat(<list of data>) with the list of data that would like to be combined
    syntax:
    pd.concat(<list of data>)
    """
    new_df = pd.concat(group_dfs)
    return new_df


# the entire work done by the transform_df can be done with the:
# the groupby method returns the dataFrame grouped by group value
# then the [] specify a certain index or label
"""
# syntax:
df[0]  # gets the first column
df['medium']  # gets the column named medium
use this a specifier if working with certain columns
"""
df_copy_2 = df.groupby('artist')['medium']
# then use transform to built in method that takes a parameter of a function that will transform the data
# the dataFrame this is called on gets transformed due to the function called within the .transform() method
# it then returns the data from the custom function
"""
throws error for some reason (look this up)
df.loc[:, 'medium'] = df_copy.transform(transform_df)
print(df.head().to_string())
"""

# aggregation case
# when trying to find the minimum acquisitionYear
# get a copy of the data trying to analyze, column specific
df_copy_2 = df.groupby('artist')['acquisitionYear']
# agg takes any function that takes a series as an input and returns a single value
# np.min takes a series and returns the minimum (look for documentation for more)
min_aq = df_copy_2.agg(np.min)
# a pandas built in method to shorten this is .min()
min_aqe = df_copy_2.min()
min_aq_ex = df.groupby('artist')['acquisitionYear'].min()
print(min_aq_ex)

# filtering
# in case when getting duplicate titles
# first group the dataFrame by titles, grouping all the titles
grouped_titles = df.groupby('titles')
# then state a condition to filter by
# in this case of the this, if the .index attribute returns more than 1 rows (x is the entire groups)
# look more into lambda functions
condition = lambda x: len(x.index) > 1
# then call the .filter() method to take a conditional function and output all values returned from that
dup = grouped_titles.filter(condition)

"""
test_df = transform_df(df)
print(test_df)
"""

"""
# testing some things
# other ways to output the minimum value
for name, group in df.groupby('artist'):
    print(group)
    year = group.loc[group['acquisitionYear'].idxmin(), 'acquisitionYear']
    print(year)
    # or
    year = group.iloc[0, 1]
    print(year)
    for val in group['acquisitionYear']:
        pass
        if val < year:
            year = val
    print(year)
"""



