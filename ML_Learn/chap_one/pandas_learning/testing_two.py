import pandas as pd
import json
import os

# pick columns out or update them (clean)
columns = ['id', 'subjectCount', 'subjects']


def get_children(subject, details):
    try:
        for item in subject['children']:
            try:
                # go into next one first fixed repeating issue, look into that
                get_children(item, details)
                details[item['id']] = item['name']
            except KeyError:
                get_children(item, details)
    except KeyError:
        for item in subject['children']:
            details[item['id']] = item['name']
    return details


def get_records(keys):
    artworks = []

    for path, _, files in os.walk('C:\\Test\\Artworks'):
        for file in files:
            if file.endswith('json'):
                with open(os.path.join(path, file)) as full:
                    content = json.load(full)
                    data = []

                    for column in keys:
                        try:
                            data.append(content[column])
                        except KeyError:
                            record = content[column] = 'NaN'
                            data.append(record)
                    artworks.append(tuple(data))

    df = pd.DataFrame.from_records(artworks, index='id', columns=columns)

    details = {}

    for children, i in zip(df['subjects'], df.index):
        if children == 'NaN':
            details[i] = 'NaN'
            continue
        elif children == {'id': 1, 'name': 'subject'}:
            break
        temp = dict()
        temp = get_children(children, temp)
        details[i] = temp

    print(details)


if __name__ == '__main__':
    """
    goes through json files and gets the subjects for each artwork and stores in dictionary
    the key is the artworks id #, or the index in the df
    """
    get_records(columns)


# maybe make pickle for ease
# df.to_pickle('C:\\Test\\pickle_test\\artwork_testing.pickle')

