import pandas as pd

"""
columns = ['id', 'artist', 'artistId', 'creditLine']
df = pd.read_csv('C:\\Test\\artwork_data.csv', index_col='id', usecols=columns)
for index, artist, artistID, creditLine in zip(df.index, df['artist'], df['artistId'], df['creditLine']):
    print(f'Artwork ID: {index}\n'
          f'Artist: name - {artist}, id - {artistID}\n'
          f'The artwork was {creditLine}.')
"""
df = pd.read_csv('C:\\Test\\artwork_data.csv')
print(df.to_string())

"""
if want to save as pickle:
df.to_pickle('C:\\Test\\pickle_test\\artwork_testing.pickle')
"""

