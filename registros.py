import datetime
import os

def registrar_excepcion(excepcion):

  fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  mensaje = f"{fecha_hora}: {excepcion.__class__.__name__} - {excepcion}"

  try:
    with open("registros.txt", "a") as archivo:
      archivo.write(mensaje + "\n")
  except Exception as e:
    print(f"Error al registrar excepción: {e}")