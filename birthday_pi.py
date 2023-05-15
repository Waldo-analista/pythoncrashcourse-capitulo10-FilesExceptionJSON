filename=r'text_files\pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

birthday=input('Ingresa tu día, mes y año (solo numeros) de tu dia de nacimiento')
if birthday in pi_string:
    print('Tu fecha de nacimiento aparece en el primer millon de digitos de PI')
else:
    print('Tu fecha de nacimiento no aparece en el primer millon de digitos de PI')
    