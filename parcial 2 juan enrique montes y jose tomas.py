
def programa_estructura_secuencial():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    print("Hola,", nombre)
    print("Tienes", edad, "años")

def programa_estructura_secuencial2():
    numero1 = int(input("Ingrese el primer número para sumar: "))
    numero2 = int(input("Ingrese el segundo número: "))
    suma = numero1 + numero2
    print("La suma de", numero1, "y", numero2, "es igual a", suma)

def programa_decision_simple():
    temperatura = float(input("Ingrese la temperatura en grados Celsius para saber si hace calor o frio: "))
    if temperatura > 30:
        print("Hace calor.")
    else:
        print("No hace tanto calor.")

def programa_decision_simple2():
    numero = int(input("Ingrese un número para decidir cual es par o impar: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

def programa_decision_compuesta():
    edad = int(input("ingrese su edad para verificar si es mayor o menor de edad: "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

def programa_decision_compuesta2():
    nota = float(input("Ingrese su nota del 1 al 100 : "))
    if nota >= 90:
        print("Tienes una A.")
    elif nota >= 80:
        print("Tienes una B.")
    elif nota >= 70:
        print("Tienes una C.")
    else:
        print("Tienes una F.")

def programa_decision_secuencial():
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        print("El número es positivo.")

def programa_decision_secuencial2():
   numero = float (input("ingrese un numero para saber si es menor o mayor a 10 "))
   if numero > 10:
       print("el numero", numero , "es mayor de 10")
   elif numero < 10: 
       print ("el numero", numero , "es menor que 10")
   else:
       print( "el numero", numero, "es igual a 10 ")

def programa_decision_anidada():
   lado1 = float (input( "ingrese la longitud del primer lado del triangulo"))
   lado2 = float (input(" ingrese la longitud del segundo lado del triangulo"))
   lado3 = float (input("ingrese la longitud del tercer lado del triangulo"))
   if lado1== lado2 == lado3:
       print("el triangulo es equilatero")
   elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
       print ("el triangulo es isoceles ")
   else: 
       print ( "el triangulo es escaleno ")

def programa_decision_anidada2():
    x = int(input("Ingrese un número X: "))
    y = int(input("Ingrese un número Y: "))
    if x > 0:
        if y > 0:
            print("X e Y son positivos.")
        else:
            print("X es positivo, Y es negativo.")
    elif x < 0:
        if y > 0:
            print("X es negativo, Y es positivo.")
        else:
            print("X e Y son negativos.")
    else:
        print("X e Y son cero.")

def programa_ciclo_for():
    for i in range(3):
        print("hola", i)

def programa_ciclo_for2():
    total = 0
    for i in range(1, 10):
        total += i
    print("La suma de los números del 1 al 10 es:", total)

def programa_ciclo_while():
    contador = 0
    while contador < 5:
        contador += 1

def programa_ciclo_while2():
    numero = int(input("Ingrese un número negativo: "))
    while numero >= 0:
        numero = int(input("Por favor, ingrese un número negativo: "))
    print("Gracias por ingresar un número negativo.")

def programa_repetitivo_decision():
    inicio = int(input("Ingrese el número por el que desea iniciar: "))
    fin = int(input("Ingrese el número por el que desea terminar: "))
    contador = inicio
    print("Números pares en el rango de", inicio, "a", fin, ":")
    while contador <= fin:
        if contador % 2 == 0:
            print(contador)
        contador += 1

def programa_repetitivo_decision2():
    contador = 1
    while contador <= 10:
        numero = int(input("Ingrese el número " + str(contador) + ": "))
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
        contador += 1




programa_estructura_secuencial()
programa_estructura_secuencial2()
programa_decision_simple()
programa_decision_simple2()
programa_decision_compuesta()
programa_decision_compuesta2()
programa_decision_secuencial()
programa_decision_secuencial2()
programa_decision_anidada()
programa_decision_anidada2()
programa_ciclo_for()
programa_ciclo_for2()
programa_ciclo_while()
programa_ciclo_while2()
programa_repetitivo_decision()
programa_repetitivo_decision2()