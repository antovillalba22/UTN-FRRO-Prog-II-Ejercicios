#-------------------------------> Utilidades <------------------------------------
from datetime import datetime
from estadia import Estadia
from precio import Precio
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    os.system("pause")

def dibujar_linea(longitud=50):
    print('-' * longitud)

red= '\033[31m'
reset = '\033[39m'

estadias = []
#-----------------------------> Funciones de Estadía <----------------------------

def ingresar_estadia():
    patente = input("Ingrese el número de patente: ")
    dibujar_linea()
    if any(estadia.nro_patente == patente for estadia in estadias):
        print(f"La patente {patente} ya ha sido ingresada previamente.")
    else:
        nueva_estadia = Estadia(patente, datetime.now().strftime("%H:%M"))
        estadias.append(nueva_estadia)
        print("Estadía ingresada\n",nueva_estadia)
        dibujar_linea()

def finalizar_estadia():
    patente = input("Ingrese el número de patente para finalizar estadía: ")
    estadia = next((e for e in estadias if e.nro_patente == patente), None)
    if estadia:
        hora_actual = datetime.now().strftime("%H:%M")
        estadia.registrar_salida(hora_actual)
        horas_estadia = estadia.cant_hora
        horas_redondeadas = int(horas_estadia) + (1 if (horas_estadia - int(horas_estadia)) >= 0.5 else 0)
        importe = Precio.calcular_importe(horas_redondeadas)
        print(f"El importe a abonar es: ${importe}")
    else:
        print("La patente no se encuentra registrada.")
        dibujar_linea()

def listar_estadias():
    if not estadias:
        print("No hay estadías registradas.")
    else:
        print("Estadías registradas:")
        for estadia in estadias:
            print(estadia)
    dibujar_linea()

#-------------------------------> Opcion Incorrecta <-----------------------------

def incorrecto(texto):
    limpiar()
    print('')
    print(red+f' x {texto} x'+reset)
    print('')
    pausa()
    limpiar()

#------------------------------------> Inico <------------------------------------

def inicio():
    print()
    print('>>> Inicio Sesión  <<<')
    print()
    decision = input('¿Desea iniciar sesión? [s/n] \n\n> ').upper()
    print()
    while (decision != 'N') and (decision != 'S'):
        limpiar()
        incorrecto('¡Carácter inválido. Intente nuevamente!')
        print()
        print('>>> Inicio Sesión  <<<')
        print()
        decision = input('¿Desea iniciar sesion? [s/n]  \n\n>').upper()
        print()
        limpiar()
    if(decision=='S'):
        menu()

#--------------------------------> Menu Principal <-------------------------------

def menu():
    opcion = ""
    while opcion != "4":  # Cambiar a 4 si agregas la opción para listar
        limpiar()
        print()
        print(">>> Bienvenido al Menú Principal <<<")
        print()
        print("1. Ingresar estadía")
        print("2. Finalizar estadía")
        print("3. Listar estadías")
        print("4. Salir")
        print()
        opcion = input("* Ingrese una opción: ")
        if opcion == "1":
            ingresar_estadia()
        elif opcion == "2":
            finalizar_estadia()
        elif opcion == "3":
            listar_estadias()
        elif opcion == "4":
            limpiar()
            print()
            print("¡Gracias por confiar en nosotros!")
            print()
            print('Hasta pronto...')
            print()
        else:
            incorrecto('¡Opción inválida. Intente nuevamente!')

#---------------------------------> Bienvenida <---------------------------------

def bienvenida():
    limpiar()
    print('')
    print(' # Programación II')
    print('')
    print(' # Proyecto: Sistema de Administración de Estadías')
    print(' # Alumno: Milton F. Ruiz')
    print(' # Comisión: 1')
    print(' # Turno: Mañana')
    print('')
    pausa()
    limpiar()

#-----------------------------> Programa Principal <------------------------------

def programa():
    bienvenida()
    inicio()

#-----------------------------------> Ejecución <---------------------------------

programa()