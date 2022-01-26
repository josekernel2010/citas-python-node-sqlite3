
import os
from tabulate import tabulate
import requests
from datetime import date
from pyfiglet import *


def inicio():
    os.system('cls')
    while True:
        titulo = Figlet(font='slant')
        print(titulo.renderText('Citas Medicas'))

        print(titulo.renderText('Citas  Medicas'))
        print("===========================================")
        print(":: Escoja una de las siguientes opciones ::")
        print("===========================================")
        print("\n\t1. Registrar una cita médica")
        print("\t2. Ver todas las citas médicas")
        print("\t3. Ver citas médicas de hoy")
        print("\t4. Modificar estado de la cita")
        print("\t5. Eliminar cita")
        print("\t6. Salir")

        opcion = input("\n\tIngrese la opción: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            break


def nueva_cita():
    paciente = input("\n\tIngrese el nombre del paciente: ")
    detalle = input("\n\tIngrese el detalle de la cita: ")
    dia = input("\n\tIngrese el día de la cita: ")
    hora = input("\n\tIngrese la hora de la cita: ")
    data = {'paciente': paciente, 'detalle': detalle,
            'dia': dia, 'hora': hora, 'estado': 'Agendada'}
    respuesta = requests.post('http://localhost:3000/citas-medicas/registrar', data=data)
    print(respuesta.text)

def solicitar_fecha():
    try:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
        fecha = date(anio, mes, dia)

        return fecha
    except ValueError:
        os.system('cls')
        print("\n------------------------------------")
        print("::Error, ingrese una fecha valida::")
        print("------------------------------------")
        return solicitar_fecha()


if __name__ == "__main__":
    inicio()
