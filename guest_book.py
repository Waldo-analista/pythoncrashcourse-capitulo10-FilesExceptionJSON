a=True

filename=r'text_files\guest_book.txt'

with open(filename,'w') as file_object:
    while a:
        user_name=input('Ingresa el nombre de usuario completo')
        print('Gracias por ingresar tu nombre de usuario')
        file_object.write(user_name+'\n')
        if user_name=="q":
            a=False

