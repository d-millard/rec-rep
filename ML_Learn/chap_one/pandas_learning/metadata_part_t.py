import pandas as pd
import json

# in json the data set is divided into folders with files
# each file is an artwork
# can contain nested files, more data
# in many cases pandas cannot traverse the folders well enough to get all data
# it is best to pre-process these folders

# to get this data going to be using pd.DataFrame.from_*
# this is the pandas object calling the attribute DataFrame with a method from_
# the * means the objects referring to
"""
this example will:
-find json files in folders
-find ways to read json files that pandas understands
-try to produce identical DataFrame as .csv
"""

# read only the first 5 in every folder
# already have the data needed saved in pickle format

# many uses of from_
# from_records() useful in finding
# it takes a list of tuples where each tuple represents one record in the dataFrame
# need to make sure the order and length of each record matches the columns' because the tuples go in exact
records = [('Espresso', "5$"), ('Flat White', "10$")]
# no custom columns files because we made from a basic DataFrame but can use columns to accept a list of column labels
print(pd.DataFrame.from_records(records, columns=["Coffee", "Price"]))

# to get the json files, read each one, one by one into json objects (using the "json" import)
# taking the necessary data from each and put it in a tuple and append to a list
# then when all are appended to list, put in pandas dataFrame with the from_records(<list of tuples>)
# when done going over all finds can then put together dataFrame

# keys going to be getting
keys = ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']

# now to process the data of the json files


def get_record_from(file_path, keys):
    """
    process a single json file and return a tuple containing
    the specific fields to input to dataFrame
    """

    # use with to conserve resources and open the file input, call it artwork_file
    with open(file_path) as artwork_file:
        # then load the file into a json object
        content = json.load(artwork_file)

        # create a list to store the records data from the file
        record = []
        # loop through the keys (the standard)
        for field in keys:
            # append the content reference to that field (seems like json is treated as a dict)
            record.append(content[field])

        # return tuple to be placed inside a larger list to then create a dataFrame with .from_records()
        return tuple(record)


# works by returning the specified data needed for frame
print(get_record_from("C:\\Test\\artworks\\a\\000\\a00001-1035.json", keys))

# get more data by iterating over multiple files
# just get the first file for every folder to save time right now
# going to need os to traverse through the folder path
import os


def read_artworks(keys):
    """
    Traverse the directories with json files.
    For first file in each directory call function
    for processing single file and go to next directory.
    """
    # get the folder that contains all directories of folders with json files
    json_root = 'C:\\Test\\artworks'

    # list of tuples to return
    artworks = []
    # os.walk takes care of going through the directory and getting to the json files
    for root, _, files in os.walk(json_root):
        # goes through the files of the directory
        for f in files:
            # if the file ends with json read it
            if f.endswith('json'):
                # call the function that processes one file to get content
                # get the path for this by combining the name of the file with the root directory
                # then input the keys to get and return the result as record
                record = get_record_from(os.path.join(root, f), keys)
                # append the tuple from that to the artworks list
                artworks.append(record)
            # break to get the first file only
            break

    # then use the data gotten from to create the dataFrame
    # use the keys as column labels, the list of tuples as records,
    # id as the row indexes using 'index=' not 'col_index' though works the same
    df = pd.DataFrame.from_records(artworks, columns=keys, index='id')

    # return the dataFrame
    return df


# testing the os traversing, json file conversion, dataFrame creator function
print(read_artworks(keys).to_string())


