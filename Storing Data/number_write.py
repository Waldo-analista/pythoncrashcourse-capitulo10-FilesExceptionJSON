import json

numbers=[1,2,4,5,9,12,25]

filename='numbers_list.json'

with open(filename,'w') as file_object:
    json.dump(numbers,file_object)
