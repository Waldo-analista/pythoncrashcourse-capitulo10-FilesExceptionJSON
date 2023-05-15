nombre=input('Ingresa tu nombre completo de usuario')
filename=r'text_files\guest.txt'

with open(filename,'w') as file_object:
    file_object.write(nombre)