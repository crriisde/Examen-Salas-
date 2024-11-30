print (" ") #Esta linea define el espacio para el nombre 
print (" Cristian David Salas De La O 3-W") #Esta linea muestra el nombre del programador 
print (" ") #Esta linea define el espacio para el nombre 
class Triangulo: #Esta linea define la clase del triangulo 
    def __init__(self, lado1, lado2, lado3): #Esta linea define los datos del triangulo en este caso los lados
        self.lado1 = lado1 #Esta linea define el lado 1 
        self.lado2 = lado2 #Esta linea define el lado 2
        self.lado3 = lado3 #Esta linea define le lado 3

    def imprimir_tipo(self): #Esta linea imprime los datos 
        print(f"Lados: {self.lado1}, {self.lado2}, {self.lado3}") #Esta linea define los lados 
        if self.lado1 == self.lado2 == self.lado3: #Esta linea define como saber si el triangulo es equilatero 
            print("El triángulo es equilatero.") #Esta linea muestra que el triangulo es equilatero
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3: #Esta linea define como saber si el lado es isoceles 
            print("El triángulo es isosceles.") #Esta linea muestra que le triangulo es isoceles 
        else: #Esta linea define que hacer si no se cumplen las conidcciones 
            print("El triángulo es escaleno.") #Esta linea muestra que el triangulo es escaleno 
        
        mayor = max(self.lado1, self.lado2, self.lado3) #Esta linea define el lado mayor del triangulo 
        print(f"El lado mayor es: {mayor}") #Esta linea muestra el lado mayor del triangulo 

lado1 = float(input("Ingresa el primer lado del triángulo: ")) #Esta linea solicita el primer lado del triangulo 
lado2 = float(input("Ingresa el segundo lado del triángulo: ")) #Esta linea solicita el segundo lado del triangulo 
lado3 = float(input("Ingresa el tercer lado del triángulo: ")) #Esta linea solicita el tercer lado del triangulo 

triangulo = Triangulo(lado1, lado2, lado3) #Esta linea define los lados del triangulo 

triangulo.imprimir_tipo() #Esta linea imprime los datos 
