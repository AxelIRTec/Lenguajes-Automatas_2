# FUNCIONES CON PARAMETROS FINITOS
x = 1
def saludar(nombre, edad):
    print("Hola " + nombre + " EDAD: " + str(edad))

saludar(edad = 20, nombre="Juan")
saludar(nombre="Mateo", edad=21)
saludar("Alicia",24)

# FUNCIONES CON N PARAMETROS
def asistencia(*alumnos):
    print("ASISTIO: "+alumnos[0])

asistencia("Ledead", "Laura", "Gustom")
asistencia("Iturraldead", "LeVoid")
asistencia("CJ")
