class TablaHashDoble:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio
 
    def funcion_hash_primaria(self, clave):
        # Función hash primaria
        return sum(ord(c) for c in clave) % self.tamanio
 
    def funcion_hash_secundaria(self, clave):
        # Función hash secundaria (debe ser diferente de cero)
        return 1 + (sum(ord(c) for c in clave) % (self.tamanio - 1))
 
    def insertar(self, clave, valor):
        indice = self.funcion_hash_primaria(clave)
        desplazamiento = self.funcion_hash_secundaria(clave)
 
        # Aplicamos doble hashing hasta encontrar un índice vacío
        while self.tabla[indice] is not None:
            indice = (indice + desplazamiento) % self.tamanio
 
        self.tabla[indice] = (clave, valor)
 
    def obtener(self, clave):
        indice = self.funcion_hash_primaria(clave)
        desplazamiento = self.funcion_hash_secundaria(clave)
 
        # Buscamos en la tabla usando doble hashing
        while self.tabla[indice] is not None:
            if self.tabla[indice][0] == clave:
                return self.tabla[indice][1]
            indice = (indice + desplazamiento) % self.tamanio
 
        return None
 
# Crear la tabla hash con doble hashing
hash_table = TablaHashDoble(7)
 
# Insertar valores, incluyendo posibles colisiones
hash_table.insertar("gato", 10)
hash_table.insertar("perro", 20)
hash_table.insertar("tigre", 30)  # Puede colisionar y usará doble hashing
 
# Imprimir la tabla hash
for i, elemento in enumerate(hash_table.tabla):
    print(f'Índice {i}: {elemento}')
 
# Obtener el valor de una clave
print("Valor de 'gato':", hash_table.obtener("gato"))
print("Valor de 'tigre':", hash_table.obtener("tigre"))