print (" ") #Esta linea define el espacio del nombre
print (" Cristian David Salas De La O 3-W") #Esta linea deifne le nombre 
print (" ") #Esta linea define el espacio para el nombre 
class Calculadora: #Esta linea define la clase para la calculadora 
    def __init__(self, num1, num2):  #Esta linea define los datos de la clase 
        self.num1 = num1
        self.num2 = num2

    def sumar(self): #Esta linea define sumar los numeros 
        return self.num1 + self.num2

    def restar(self): #Esta linea define restar los numeros 
        return self.num1 - self.num2

    def multiplicar(self): #Esta linea define multiplicar los numeros 
        return self.num1 * self.num2

    def dividir(self): #Esta linea define dividir los numeros 
        if self.num2 != 0: 
            return self.num1 / self.num2
        else:
            return "Error: División por cero." 

#Esta lineas solicitan los datos 
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Esta linea define crear un objeto Calculadora
calculadora = Calculadora(num1, num2)

#Esta linea muestra los resultados
print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")
