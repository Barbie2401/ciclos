#Librerias
from string import ascii_lowercase

#Solicitar al usuario que ingrese datos
password_user= input("\nIngrese la contraseña: ").lower()

#Crear diccionario para comparar
dictionary= ascii_lowercase

#Numero de intentos, parte desde cero
attempts= 0

#ciclos y condiciones
for i in password_user:
    for j in dictionary:
        attempts+=1
        if i ==j:
            break

#Respuesta
print(f"La contraseña fue forzada en {attempts} intentos\n")
    

