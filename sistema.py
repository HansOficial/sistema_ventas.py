from datetime import datetime as time
import sqlite3
import sys
import os
def insert():
    ing = int(input("¿cuantas personas vas a ingresar? :"))
    cont = 0
    while cont < ing:
        cont += 1
        name = input("Ingrese nombres: ")
        last_name = input("Ingrese apellidos de {}: ".format(name))
        mail = input("Ingrese Correo de {}: ".format(name))
        phone = input("Ingrese numero telefonico de {}: ".format(name))
        marca_phone = input("Ingrese Marca de telefono: ")
        modelo_phone = input("Ingrese Modelo de telefono: ")
        date_ingreso = time.now()
        date_entrega = input("Fecha de entrega?: ")
        with sqlite3.connect("data_phone.db") as con:
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS telefonos (nombres TEXT, apellidos TEXT, correo TEXT, telefono TEXT, marca TEXT, modelo TEXT, fecha_ingreso TEXT, fecha_entrega TEXT)")
            cursor.execute("INSERT INTO telefonos (nombres, apellidos, correo, telefono, marca, modelo, fecha_ingreso, fecha_entrega) VALUES (?,?,?,?,?,?,?,?)", (name, last_name, mail,phone, marca_phone, modelo_phone, date_ingreso, date_entrega))
            print("Datos ingresados con exito")
            con.commit()
    cls = input("Desea limpiar pantalla?: ")
    if cls == "si":
        os.system("clear")
    else:
        pass






def view():
    with sqlite3.connect("data_phone.db") as con:
        cursor = con.cursor()
        row = cursor.execute("SELECT * FROM telefonos")
        rows = row.fetchall()
        for i in rows:
            print("======="*30)
            print("Nombres {}\nApellidos {}\nCorreo {}\nTelefono {}\nMarca {}\nModelo {}\nFecha ingreso {}\nFecha entrega {}\n".format(i[0], i[1], i[2], i[3], i[4] ,i[5], i[6], i[7]))
            print("======="*30)
    cls = input("Desea limpiar pantalla?: ")
    if cls == "si":
        os.system("clear")
    else:
        pass


def menu():
    while True:
        print("SISTEMA DE REGISTRO CLIENTES V1 \"LINIA DE COMANDOS\"\n")
        print("""

        1- INGRESA CLIENTE
          
        2- VER CLINTES
          
        0- SALIR 

        """)
        try:
            OP = int(input("Ingrese opcion: "))
            if OP == 1:
                insert()
            elif OP == 2:
                view()
            elif OP == 0:
                sys.exit()
            else:
                print("opcion invalida")


        except ValueError:
            print("ingrese una opcion valida")

menu()
     
