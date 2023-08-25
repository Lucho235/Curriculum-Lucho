'''
Ejercicio integrador de funciones y listas para realizar EN CLASE
=========
Instrucciones

Una empresa transportista tiene 10 camiones y 15 conductores.
Por cada camión se preparó una planilla con los siguientes datos:
• Código de Dominio (entero de seis dígitos) –
    UTILIZAR FUNCION LEER_EN_RANGO QUE VALIDE EL INGRESO DE ESTE DATO
• Importe a cobrar por kilómetro (real, mayor a cero) –
    UTILIZAR FUNCION LEER_MAYOR_CERO QUE VALIDE EL INGRESO DE ESTE DATO

Por cada viaje realizado por un conductor se ingresa lo siguiente:
• Número de conductor (entero, de 1 a 15)
• Código de Dominio del camión (entero de seis dígitos)
• Cantidad de kilómetros (real, mayor a cero)
El ingreso de esta información finaliza con un número de conductor igual a 99.

Se pide determinar e informar:
a. Un listado ordenado por importe en forma descendente con el importe total recaudado
por conductor teniendo en cuenta el valor por kilómetro ingresado al inicio

b. Código de dominio del camión que recorrió la mayor cantidad de kilómetros especificando
la cantidad de kilómetros (puede haber más de uno)

'''


def LEER_EN_RANGO(dom):
    if 100000<dom<999999:
        return True
    else:
        return False

def LEER_MAYOR_CERO

#main

dominios = []
importexkm = []
kilometrajecamion = [0,0,0,0,0,0,0,0,0,0]

conductores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
recaudacionConductor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#carga camiones
cont = 0
while cont < 10:
    dominio = int(input("ingrese el dominio del camion (numero de 6 digitos) ",cont+1))
    if LEER_EN_RANGO:
        dominios.append(dominio)
    else:
        print("Error, el dominio es invalido")