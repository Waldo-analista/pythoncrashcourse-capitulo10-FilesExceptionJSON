print("Ingresa dos números para dividirlos")
print("Ingresa q para salir")

while True:
    dividendo=input('Ingresa el dividendo')
    if dividendo=='q':
        break
    divisor=input('Ingresa el divisor')
    if divisor=='q':
        break
    try: 
        resultado=int(dividendo)/int(divisor)
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        print(f'El resultado de la division entre {dividendo} y {divisor} es: {resultado}')