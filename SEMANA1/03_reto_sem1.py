# Reto 3: Desarrollo de Productos con POO
# =======================================
# Tener un programa que reciba una cantidad de productos a ingresar, que luego de ingresarlos (instanciar) podamos llamar a uno de ellos y que nos muestre su descripción y si no, tengamos una opción para terminar el programa. (Usar 

class Almacen:
    def __init__(self):
        self.prod1 = 'Lacteos'
        self.prod2 = 'Arinas'
        self.prod3 = 'Carnes'
        self.prod4 = 'Gaseosas'
        self.prod5 = 'Licores'
objProductos = Almacen()
print(objProductos.prod1, objProductos.prod2, objProductos.prod3, objProductos.prod4, objProductos.prod5)
