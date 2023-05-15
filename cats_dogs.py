filenames=[r'text_files\cats.txt',r'text_files\dogs.txt']
try:
    texto=''
    for filename in filenames:
        with open(filename) as file_object:
            texto+=file_object.read()+'\n\n'

except FileNotFoundError:
    print('Uno de los archivos no existe')

else:
    print(texto)