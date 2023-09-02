#Desafio N°2 - Filtrado compacto

# Este programa devuelve meses mayores a cierto valor

#Importar librerias
import sys

# Datos de ventas
ventas = {  "Enero": 15000,
            "Febrero": 22000,
            "Marzo": 12000,
            "Abril": 17000,
            "Mayo": 81000,
            "Junio": 13000,
            "Julio": 21000,
            "Agosto": 41200,
            "Septiembre": 25000,
            "Octubre": 21500,
            "Noviembre": 91000,
            "Diciembre": 21000
          }

# Recibir input del usuario
umbral = int(sys.argv[1])

resultado = {} #Crear un diccionario vacio

for mes, venta in ventas.items():
    if venta > umbral:
        resultado[mes] = venta
    
print(resultado) #Imprimir resultado

# python mayor_a.py 40000
