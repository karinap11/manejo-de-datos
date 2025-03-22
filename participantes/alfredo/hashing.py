class TablaHash:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [[] for _ in range(tamanio)]
 
    def funcion_hash(self, clave):
        # Calculamos el índice usando la suma de los valores ASCII
        # de los caracteres mod el tamaño de la tabla
        return sum(ord(c) for c in clave) % self.tamanio
 
    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        # Añadimos el par clave-valor en la lista del índice correspondiente
        self.tabla[indice].append((clave, valor))
 
    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        # Buscamos en la lista enlazada del índice por la clave
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None
 
 
# Crear la tabla hash con encadenamiento separado
hash_table = TablaHash(5)
 
# Insertar valores, incluyendo colisiones
hash_table.insertar("gato", 10)
hash_table.insertar("perro", 20)
# Colisionará con "gato" si usan el mismo índice
hash_table.insertar("tigre", 30)
 
# Imprimir la tabla hash
for i, lista in enumerate(hash_table.tabla):
    print(f'Índice {i}: {lista}')
 
# Obtener el valor de una clave
print("Valor de 'gato':", hash_table.obtener("gato"))
print("Valor de 'tigre':", hash_table.obtener("tigre"))
 