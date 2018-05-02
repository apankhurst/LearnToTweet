import json
import re

# where the dirty data is stored
original_path  = './original_data/'

# where to store the clean data
new_path = './data/'

# files to read
files = ['2009.json', '2010.json', '2011.json', '2012.json', '2013.json', '2014.json', '2015.json', '2016.json', '2017.json']

for f in files:

    in_file_path = original_path + f
    out_file_path = new_path + f

    # read in the json file 
    with open(in_file_path) as json_data:
        file_data = json.load(json_data)
        json_data.close()

    data_array = []
        
    for json_item in file_data:
        # if the tweet wasn't a retweet, doesn't contain a url, and has <= 140 characters
        # add it to the new file
        data = {}
        if json_item['is_retweet'] == False:
            text = json_item['text']
            created_at = json_item['created_at']
            data['text'] = text
            data['created_at'] = created_at
            if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)) == 0 and len(text) <= 140:
                data_array.append(data)

    with open(out_file_path,'w') as out_file:
        json.dump(data_array, out_file)
