filename=r'text_files\poll.txt'

while True:
    reason_programming=input('Ingrese su razon para programar')
    if reason_programming=='q':
        break
    with open(filename,'a') as file_object:
        file_object.write(reason_programming+'\n')
    