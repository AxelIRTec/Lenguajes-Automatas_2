# Entrada de Datos


print("Ingresa tu Nombre:")
nombre = input()
print(type(nombre))
Palabras = nombre.split(" ")
nombre = nombre.capitalize()
nombre = nombre.replace(" ", "-")
accu = " "

for Palabra in Palabras:
    accu = accu + Palabra.capitalize() + " "

print("Hola: " + accu)
