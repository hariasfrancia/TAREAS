# Reto 1: Desarrollar un programa de bienvenida
# =============================================
# Para este reto tendremos que hacer lo siguiente:
# 1.-Ingresar un nombre y su edad.
# 2.-Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) debe ir a dormir y si no hacer la tarea.
# 3.-Si es mayor de edad que indique que no esta obligado a hacer nada.

# input('\n')
nombre = str(input('Ingrese su nombre: '))
edad = int(input('Ingrese su edad: '))
hora = int(input('Ingrese hora(FORMATO: 24 HRS): '))
# if edad < 18 and hora > 5:
#     print('Usted es menor de edad, debe ir a dormir o hacer la tarea')
# else:
#     print('No estoy obligado a hacer la tarea')
# if edad < 6:
#     print('Usted debe ingesar una edad VÁLIDA, mayor a 5 años')
if edad < 6:
    print('Usted debe ingesar una edad VÁLIDA, mayor a 5 años')
elif edad < 18 and hora > 17:
    print('Usted es menor de edad, debe ir a dormir')
    print('Si no, debes hacer la tarea')
elif hora < 18:
    print('No estoy obligado a hacer la tarea')
elif edad > 17:
    print('No estoy obligado a hacer la tarea')
else:
    print('Si no debes hacer la tarea')

    