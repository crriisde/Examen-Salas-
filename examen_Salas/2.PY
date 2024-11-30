print (" ") #esta linea define le espacio para el nombre 
print (" Cristian David Salas De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea define el espacio para el nombre 

class Persona: #esta linea define la clase de la persona 
    def __init__(self, nombre, edad): #esta linea define los datos de la persona 
        self.nombre = nombre #esta linea define el primer parametro de la clase en este caso el nombre 
        self.edad = edad #esta linea define el primer parametro de la clase en este caso la edad 

    def imprimir_datos(self): #esta linea define como imprimir los datos 
        print(f"Nombre: {self.nombre}") #esta linea muestra el nombre 
        print(f"Edad: {self.edad}") #esta linea muestra la edad 
        if self.edad >= 18: #esta linea define como saber si eres mayor de edad o no 
            print("Es mayor de edad.") #esta linea define que mostrar si la edad es mayor a 18
        else: #esta linea define que hacer si no se cumple con la condiccion 
            print("Es menor de edad.") #esta linea define que mostrar si la edad es menor a 18

nombre = input("Ingresa el nombre de la persona: ") #esta linea solicita ingresar el nombre
edad = int(input("Ingresa la edad de la persona: ")) #esta linea solicita ingresar la edad 

persona = Persona(nombre, edad) #esta linea define los datos de la persona 

persona.imprimir_datos() #esta linea imprime los datos
