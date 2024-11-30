print (" ") # Esta linea da el espacio para el nombre 
print (" Cristian David Salas De La O 3-W") #Esta linea muestra el nombre del programador 
print (" ") #Esta linea da el espacio para el nombre 

class Alumno: #Esta linea define la class del alumno 
    def __init__(self, nombre, nota): #Esta linea define los datos de la class del alumno 
        self.nombre = nombre #esta linea define el primer parametro de una clase en este caso el nombre 
        self.nota = nota #esta linea define el primer parametro de una clase en este caso la nota 

    def imprimir_datos(self): #esta linea defiene como definir la nota y el nombre 
        print(f"Nombre: {self.nombre}") #esta linea muestra el nombre 
        print(f"Nota: {self.nota}") #esta linea muestra la nota 
        if self.nota >= 5: #esta linea define como saber si reprobaste o pasaste 
            print("Aprobado felecidades muy bien tu") #esta linea deifne que mostrar si la nota es mayor a 5
        else: #esta linea define que mostrar si no se cumple la concidcion del numero mayor a 5
            print("Reprobado jajajaja") #esta linea define que mostrar si la nota es menor a 5

nombre = input("Ingresa el nombre del alumno ") #esta linea solicita el nombre del alumno 
nota = float(input("Ingresa la nota del alumno ")) #esta linea solicita la nota del alumno 

alumno = Alumno(nombre, nota) #esta linea deifne los datos del alumno 

alumno.imprimir_datos() #esta linea define el mostrar los datos 
