filename=r'text_files\learning_python.txt'
'''
#Se lee el archivo completo
with open(filename) as file_object:
    lines=file_object.read().strip()
    for i in range(0,3):
        print(lines)
'''

'''
#Se lee el archivo por linea
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
'''
with open(filename) as file_object:
    lines=file_object.readlines()

str=''
for i in lines:
    str+=i.replace("Python","JavaScript")
print(str)
