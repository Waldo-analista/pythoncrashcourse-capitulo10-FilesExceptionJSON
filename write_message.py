filename=r'text_files\programming.txt'
'''
with open(filename,'w') as file_object:
    file_object.write('I love programming in Python\n')    
    file_object.write('I love creating new games\n')  
'''
    
with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datasets\n')    
    file_object.write('I love creating apps that run in a browser\n')  