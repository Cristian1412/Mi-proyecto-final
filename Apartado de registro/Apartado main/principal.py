from Apartmenu.cargar_guardar_datos import *
from Apartmenu.principal_menu import *
from Apartmodulos.Administrativo.usuarios import *

from Apartmodulos.Servicios.datos import *
from Apartmodulos.Servicios.servicios import *

from Apartmodulos.Ventas.ventas import *

from registros import *

from Apartmodulos.Ventas.datos import *

RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Modulos/Servicios/serviciosyproductos.json"
RUTA_REGISTROS = "registros.txt"
RUTA_VENTAS = "Modulos/Ventas/ventas.json"


datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos = cargar_datos(RUTA)
datos_ventas = cargar_datos_ventas(RUTA_VENTAS)


while True:
    menu_principal()
    opc = pedir_opcion()
    
    if opc == 1:
        print(menu_usuarios())
        opc = pedir_opcion()
        if opc == 1:
            datos = creacion_de_usuario(datos)
        elif opc == 2:
            datos = leer_datos_usuario(datos)
        elif opc == 3:
            datos = actualizar_datos_usuario(datos)
        elif opc == 4:
            datos = eliminar_datos_usuario(datos)
        elif opc == 5:
            datos= categoria_usuario(datos)
        
        

    elif opc == 2:
        
        print(menu_servicios())
        opc = pedir_opcion()
        if opc == 1:
            datos_servicios = generar_servicio(datos_servicios)
            datos_servicios = generar_producto(datos_servicios)
        elif opc == 2:
            listar_servicios(datos_servicios)
        elif opc == 3:
            datos_servicios = actualizar_servicio(datos_servicios)
            datos_servicios = actualizar_producto(datos_servicios)
        elif opc == 4:
            datos_servicios = eliminar_servicio(datos_servicios)
            datos_servicios = eliminar_producto(datos_servicios)
            
    elif opc == 3:
        print(menu_reportes())
        opc = pedir_opcion()
        if opc == 1: 
            cant_servic(datos_servicios)
        cant_product(datos_servicios)

    elif opc == 4:
        print(menu_ventas())
        opc = pedir_opcion()
        if opc == 1:
            ventas_totales(datos)
        elif opc == 2:
            datos_ventas = interacciones_productos(datos_ventas)
        elif opc == 3:
            datos_ventas = interacciones_servicios(datos_ventas)

    elif opc == 5:
        print("Acabas de salir!!")
        break

    registrar_excepcion(Exception)
    
    (cargar_datos, RUTA)
    guardar_datos_servicios(datos_servicios, RUTA_SERVICIOS)
    guardar_datos_ventas(datos_ventas, RUTA_VENTAS)