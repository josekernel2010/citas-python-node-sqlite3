
import os
from tabulate import tabulate
import requests
from datetime import *
from pyfiglet import *


# Menu
def inicio():
    os.system('cls')
    
    try:
        while True:
            # funcion requests para obtener el token para la autenticacion
            requests.get('http://localhost:3000/citas-medicas/todas')
            titulo = Figlet(font='standard')

            print(titulo.renderText('Citas  Medicas'))
            print("===========================================")
            print(":: Escoja una de las siguientes opciones ::")
            print("===========================================")
            print("\n\t1. Registrar una cita médica")
            print("\t2. Ver todas las citas médicas") 
            print("\t3. Buscar citas médicas de hoy")
            print("\t4. Modificar estado de la cita")
            print("\t5. Eliminar cita")
            print("\t6. Salir")

            opcion = input("\n\tIngrese la opción: ")

            if opcion == "1":
                nueva_cita()
            elif opcion == "2":
                mostrar_citas()
            elif opcion == "3":
                buscar_citas_fecha()
            elif opcion == "4":
                modificar_estado()
            elif opcion == "5":
                eliminar_cita()
            elif opcion == "6":
                break
            else:
                print("\n\t=======================")
                print("\t:: Opción inválida ::")
                print("\t=======================")
                input("Presione una tecla para continuar...")
                os.system("cls")
    except:
        print("\n\t***********************************")
        print('\t:: Error de conección ¯\_(ツ)_/¯ ::')
        print("\t***********************************")
        print("\tSolucione el problema e intente nuevamente")
        input("\tPresione una tecla para salir...")
        return False
        


    #1. Registro de una nueva cita
def nueva_cita():
    os.system('cls')
    print("\n\t============================")
    print("\t:: Ingreso de nueva cita ::")
    print("\t============================\n")
    

    paciente = input("\n\tIngrese el nombre del paciente: ")
    detalle = input("\n\tIngrese el detalle de la cita: ")
    print("\n\t:: Fecha de la cita ::\n")
    fecha = solicitar_fecha()  
    hora = input("\n\tIngrese la hora de la cita: ")
    
    while paciente=='' or detalle=='' or fecha=='' or hora=='':
        os.system('cls')
        print("\n\t============================")
        print("\t::   Campos obligatorios   ::")
        print("\t============================")
        paciente = input("\n\tIngrese el nombre del paciente: ")
        detalle = input("\n\tIngrese el detalle de la cita: ")
        hora = input("\n\tIngrese la hora de la cita: ")
        
    data = {'paciente': paciente, 'detalle': detalle,
            'fecha': fecha, 'hora': hora, 'estado': 'Agendada'}
    respuesta = requests.post('http://localhost:3000/citas-medicas/registrar', data=data)
    print("\n\t"+respuesta.text)
    
    input("\n\tPresione enter para continuar...")
    os.system('cls')


    #2. Mostrar todas las citas
def mostrar_citas():
    os.system('cls')
    respuesta = requests.get('http://localhost:3000/citas-medicas/todas')
    tabla(respuesta)
    input("\n\tPresione enter para continuar...")
    os.system('cls')
    
    
    #3. Buscar citas por fecha    
def buscar_citas_fecha():
    os.system('cls')
    
    fecha_actual = date.today()
    print("\n\t======================")
    print("\t:: Busqueda de cita ::")
    print("\t======================\n")
    print("\t",fecha_actual)
    #fecha = solicitar_fecha()
    respuesta = requests.get('http://localhost:3000/citas-medicas/buscar/', data={'fecha': fecha_actual})
    
    if len(respuesta.json()) > 0:
        tabla(respuesta)
        input("\n\tPresione enter para continuar...")
        os.system('cls')
    else:
        print("\n\t======================")
        print("\t::   No hay citas   ::")
        print("\t======================")   
        input("\n\tPresione enter para continuar...")
        os.system('cls')


    #4. Modificar estado de la cita
def modificar_estado():
    os.system('cls')
    print("\n\t==========================")
    print("\t:: Modificación de cita ::")
    print("\t==========================\n")
    
    try:
            
        id = input("\n\tIngrese el ID de la cita a modificar: ")
        
        # Verificar si existe la cita por medio de la url de la API
        buscar_id = requests.get('http://localhost:3000/citas-medicas/buscar_id/'+id)
        
        if len(buscar_id.json()) > 0:
            # Mostrar la cita a modificar
            tabla(buscar_id)    
            valor = input("\n\tIngrese el nuevo estado de la cita:\n\t1. Agendada\n\t2. Realizada\n\t3. Cancelada\n\t")
            
            while True:
                
                if valor == '1':
                    estado = 'Agendada'
                elif  valor == '2':
                    estado = 'Realizada'
                elif valor == '3':
                    estado = 'Cancelada'
                elif int(valor) >3 or int(valor) <1:
                    print("\nValor fuera de rango")
                    input("Presione una tecla para continuar...")
                    os.system("cls")
                    break
                 
                respuesta = requests.post('http://localhost:3000/citas-medicas/modificar/'+id, data={'estado': estado})
                print("\n\t"+respuesta.text)
                input("\n\tPresione enter para continuar...")
                os.system('cls')
                break
        else:
            print("\n\t=======================================")
            print("\t::   El id de la cita no de existe   ::")
            print("\t=======================================")
            input("\n\tPresione enter para continuar...")
            os.system('cls')
            
    except ValueError:
        print("\n\t===================================")
        print("\t::   El valor  no es correcto   ::")
        print("\t===================================")
        input("\n\tPresione enter para continuar...")
        os.system('cls')
        
        
    #5. Eliminar cita
def eliminar_cita():
    os.system('cls')
    print("\n\t==========================")
    print("\t:::  Eliminar de cita  :::")
    print("\t==========================\n")
    
    try:
        
        id = input("\n\tIngrese el ID de la cita a eliminar: ")
        # Verificar si existe la cita por medio de la url de la API
        buscar_id = requests.get('http://localhost:3000/citas-medicas/buscar_id/'+id)
        
        if len(buscar_id.json()) > 0:   
            respuesta = requests.delete('http://localhost:3000/citas-medicas/eliminar/'+id)
            print("\n\t"+respuesta.text)
            # Mostrar la cita a eliminar
            tabla(buscar_id)
            input("\n\tPresione enter para continuar...")
            os.system('cls')
            
        else:
            print("\n\t=======================================")
            print("\t::   El id de la cita no de existe   ::")
            print("\t=======================================")
            
            input("\n\tPresione enter para continuar...")
            os.system('cls')
            
    except ValueError:
        
        print("\n\t===================================")
        print("\t::   El valor  no es correcto   ::")
        print("\t===================================")
        input("\n\tPresione enter para continuar...")
        os.system('cls')
        
    
    
    # Funcion de ayuda para solicitar fecha
def solicitar_fecha():
    try:
        dia = int(input("\tIngrese el día: "))
        mes = int(input("\tIngrese el mes: "))
        anio = int(input("\tIngrese el año: "))
        fecha = date(anio, mes, dia)

        return fecha
    except ValueError:
        os.system('cls')
        print("\n------------------------------------")
        print("::Error, ingrese una fecha valida::")
        print("------------------------------------")
        return solicitar_fecha()

    
    # Funcion de ayuda para imprimir tabla
def tabla(respuesta):
    datos = []
    for dato in respuesta.json():
        temp=[]
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    head = ['ID', 'Paciente', 'Detalle', 'Fecha', 'Hora', 'Estado']
    tabla = tabulate(datos, head, tablefmt='fancy_grid')
    print()
    print(tabla)
        
        
if __name__ == "__main__":
    inicio()
