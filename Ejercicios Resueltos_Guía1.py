import math
#1
'''class numeros:
    def __init__(self):
        pass

def nro_romano():
    numero = int(input("Ingrese el numero a convertir: "))
    cont = 0
    romano = ""
    if numero >= 5 and numero < 9:
        romano = "V"
        cont = numero - 5
        while cont > 0:
            romano = romano + "I" 
            cont -= 1
        print(romano)    
    elif numero == 4:
        print("IV")
    elif numero < 5:
        cont = numero
        while cont > 0:
            romano = "I" + romano 
            cont -= 1
        print(romano)
    elif numero >= 9:
        romano = "X"
        cont = numero - 10
        while cont < 0:
            romano = "I" + romano
            cont += 1
        print(romano)
    else:
        print("No tengo disponible esa conversión")

nro_romano()'''

#2
'''class romanos:
    def __init__(self,lista):
        self.lista = lista

lista = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

def nro_entero():
    nro_ingresado = input("Ingrese el numero a convertir: ")
    if nro_ingresado in lista:
        print(lista.index(nro_ingresado) + 1)
    else:
        print("No tengo disponible esa conversión")

nro_entero()'''

#3
'''class conjuntos:
    def __init__(self, conjuntos):
        self.conjuntos = conjuntos

conjuntos = int(input("Ingrese los numeros dentro de su conjunto: "))
conjuntos = list(conjunto)

def subconjuntos(conjunto):
    sub = [[]]
    for n in conjunto:
        sub.append([n])
        for i in conjunto:
            if n != i not in sub:
                if i and n not in sub:
                    sub.append([n,i])
    sub.append(conjunto)
    print(sub)    

subconjuntos(conjuntos)'''

#5 
'''class revertir:
    def __init__(self, mensaje):
        self.mensaje = mensaje

mensaje = input("Ingrese su frase: ")

def revierte(entrada):
    entrada = entrada.split(' ') 
    lista = " ".join(entrada[::-1])
    print(lista)    

revierte(mensaje)'''

#6
'''class rectangulo:
    def __init__(self, base1, altura1):
        self.base1 = base1
        self.altura1 = altura1

base1 = int(input("Ingrese el numero de base: "))
altura1 = int(input("Ingrese el numero de altura: "))

def areaR(base, altura):
    area = base * altura
    print(area)

areaR()'''

#7
'''class circulo:
    def __init__(self, distancia):
        self.distancia = distancia

distancia = int(input("Ingrese el radio: "))

def areaC(radio):
    area = math.pi * radio **2
    print(area)

def perimetro(radio):
    perimetro = math.pi * radio * 2
    print(perimetro)

areaC(distancia)
perimetro(distancia)'''
