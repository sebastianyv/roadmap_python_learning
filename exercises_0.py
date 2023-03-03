# 0. Expon las funciones mencionadas anteriormente Creando ejemplos:
"""

# Función print()
message = "Este es un mensaje de los ejercicios de tationis"
print(message)

# Función input()
message = input("Ingrese un mensaje para Joshua: ")
print(message)

# Función sum()
a = (3, 4, 6, 8)
x = sum(a, 80)
print(x)

# Funcion map()
a = (3, 4, 6, 8)
x = map(lambda x: x * 2, a)
y = tuple(x)
print(y)    


# Funcion filter()
numeros = (1, 2, 3, 4, 5, 3, 4, 5, 6, 6, 7, 7,)

def check_filter(numero):
    if numero == 6:
        return True
    return False

check_numero = filter(check_filter, numeros)

final_numero = list(check_numero)

print(final_numero)


#Funcion min()

min_numero = min(numeros)

print(min_numero)


#Funcion max()

max_numero = max(numeros)

print(max_numero)
"""

#Funcion len()
grupo21 = [1, 5, "cuatro", 6, "doce", 54]
print(len(grupo21))


#Funcion enumerate()

enumerateEjm = enumerate(grupo21)

print(list(enumerateEjm))


#Funcion range()

rangeEjm = range(0,100,8)

print(list(rangeEjm))

#Funcion id()

g = 6

print("El id de 6 es ", id(g ))

#Funcion chr()

print(chr(67))


#Funcion abs()
float = -85.57
print(abs(float))


#Funcion reversed()
palabra = "Python curso"

print(list(reversed(palabra)))


# funcion round() 
number = 14.25
rounded_number = round(number)
print(rounded_number)

# Funcion str()
print(str('1993'))
print(str('sonic'))
print(str('swim'))

# Funcion set() 
list_numbers = [2,4,6,8,10,12]
numbers_set = set(list_numbers)
print(numbers_set)

# Funcion int()
result = int(10.12)
print('int(10.12):',result)

# Funcion type() 
prime_number = [1,10,25,56,789]

result = type(prime_number)
print(result)

# Funcion dict()
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

# Funcion list()
vowel_string = 'aeiou'
print(list(vowel_string))


vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))


vowel_list = ['a', 'e', 'i', 'o', 'u']
print(list(vowel_list))

# Funcion tuple() 

""" crear una tupla a partir de una lista """ 
t2 = tuple([1, 4, 6])
print('t2 =', t2)

"""  creando una tupla a partir de una cadena """ 
t1 = tuple('Python')
print('t1 =',t1)

"""  crear una tupla a partir de un diccionario """ 
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)

# Funcion float() 
number = 10
print('float(10):',float(number))

# Funcion eval() 
number = 50

square_number = eval('number * number')
print(square_number)

# Funcion open() 
"""
'r'	Abre un archivo para leer. (por defecto)
'w'	Abre un archivo para escribir. Crea un nuevo archivo si no existe o trunca el archivo si existe.
'x'	Abra un archivo para la creación exclusiva. Si el archivo ya existe, la operación falla.
'a'	Abrir para agregar al final del archivo sin truncarlo. Crea un nuevo archivo si no existe.
't'	Abrir en modo texto. (por defecto)
'b'	Abrir en modo binario.
'+'	Abrir un archivo para actualizar (lectura y escritura)
"""

file_name = open("path_to_file", mode='r')
print(file_name)

file_name = open("path_to_file", mode='w')

file_name = open("path_to_file", mode='a')

file_name = open("text.txt", mode='t')



#Funcion all() 
boolean_list = ['True', 'True', 'True']

result = all(boolean_list)
print(result)

boolean_list = ['True', 'True', 'False', 'False']

result = all(boolean_list)
print(result)
