from Ejercicio6_Class import Pila #Importar la clase desde otro archivo
mi_pila = Pila()

# Agregar elementos a la pila
mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)

# Mostrar el estado de la pila
print(mi_pila)

# Ver el elemento superior con peek
print("Elemento en la cima:", mi_pila.peek())

# Quitar el elemento superior con pop
print("Elemento quitado:", mi_pila.pop())

# Mostrar el estado de la pila después de pop
print(mi_pila)

# Verificar si la pila está vacía
print("¿Está vacía?", mi_pila.esta_vacia())

# Vaciar la pila con pop
mi_pila.pop()
mi_pila.pop()
print(mi_pila.pop())  # La pila está vacía

# Verificar si la pila está vacía nuevamente
print("¿Está vacía?", mi_pila.esta_vacia())
