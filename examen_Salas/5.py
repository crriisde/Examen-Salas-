print (" ") #esta linea define le espacio para el nombre 
print (" Cristian David Salas De La O 3-W") #esta linea muestra el nombre del programador 
print (" ") #esta linea define el espacio para el nombre 
class Agenda: #esta linea define la clase de la agenda 
    def __init__(self): #esta linea define el primer parametro de la clase en este caso la edad 
        self.contactos = {}

    def añadir_contacto(self): #esta linea el contacto 
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        self.contactos[nombre] = {'telefono': telefono, 'email': email}

    def lista_contactos(self): #esta linea define la lista 
        for nombre, datos in self.contactos.items():
            print(f"{nombre}: {datos['telefono']}, {datos['email']}")

    def buscar_contacto(self): #esta linea busca el contacto 
        nombre = input("Buscar nombre: ")
        if nombre in self.contactos:
            print(f"{nombre}: {self.contactos[nombre]['telefono']}, {self.contactos[nombre]['email']}")
        else:
            print("No encontrado")

    def editar_contacto(self): #esta linea perimite editar el contacto 
        nombre = input("Editar nombre: ")
        if nombre in self.contactos:
            telefono = input("Nuevo Telefono: ")
            email = input("Nuevo Email: ")
            self.contactos[nombre] = {'telefono': telefono, 'email': email}

#estas lineas crean el menu y sus interacciones
agenda = Agenda()
while True:
    print("\n1. Añadir\n2. Lista\n3. Buscar\n4. Editar\n5. Salir")
    opcion = input("Opcion: ")

    if opcion == '1': agenda.añadir_contacto()
    elif opcion == '2': agenda.lista_contactos()
    elif opcion == '3': agenda.buscar_contacto()
    elif opcion == '4': agenda.editar_contacto()
    elif opcion == '5': break
    else: print("Opcion invalida.")
