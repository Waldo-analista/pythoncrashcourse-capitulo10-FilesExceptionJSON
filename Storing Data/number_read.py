import json

filename='numbers_list.json'

with open(filename,'r') as file_object:
    numbers=json.load(file_object)

print(numbers)