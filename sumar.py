while True:
    numero_1=input('Ingresa el primer número a sumar')
    if numero_1=='q':
        break
    numero_2=input('Ingresa el segundo número a sumar')
    if numero_1=='q':
        break
    try: 
        resultado=int(numero_1)+int(numero_2)
        print(f'La suma del número {numero_1} y el número {numero_2} es: {resultado}')
    except ValueError:
        print('No has ingresado números')