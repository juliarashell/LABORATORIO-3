def square (n) :
    return n * n 


# Store result from square in a variable / almacenar el resultado del cuadrado en una variable
result = square(  4)
print(result)
# Send the result from square immediately to another function / Envía el resultado del cuadrado inmediatamente a otra función
print(square(  5))
# Use the result returned from square in a conditional expression / Usar el resultado devuelto por el cuadrado en un condicional expresión
if square(3) < 15:
    print('Still less than 15   ')


def swap (a, b) :
    return b,a

a = 2
b = 3
x, y = swap(a, b)
print(x, ',', y)

z = swap(a, b)
print(z)
