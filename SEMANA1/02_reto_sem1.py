# Reto 2: Ingresar Personas
# ===========================
# Hacer un programa que primero capture cuantas Personas vamos a ingresar, luego pedir su nombre, dni y fecha de nacimiento y al final mostrarlas en un orden de la mas joven a la mas adulta

# num_pers = int(input("Ingrese un número de personas: "))
pers = []
for k in range(3):
    pers.append(input('Ingresa su nombre: '))
    pers.append(input('Ingresa su dni: '))
    pers.append(input('Ingresa su fecha de nacimiento: '))
    pers.sort()
print (pers)

    
