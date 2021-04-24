import random
secretnumber = random.randint(1, 5)

print('Tiene que adivinar el numero Leandro perro hijueputa del 1 al 20')

for c in range(1,5) :
    user_value = int((input('Numero\n')))
    if user_value < secretnumber :
        print('El numero secreto es mayor')
    elif user_value > secretnumber :
        print('El numero secreto es menor')
    else :
        break
if user_value == secretnumber :
    print('well done!')
    print('The correct number is '+ str(secretnumber) + ' lo adivinaste en '+ str(c) + ' intentos')
#else : 
#   print('Pasaron las 7 oportunidades')