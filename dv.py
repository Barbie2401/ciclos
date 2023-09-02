#Desafio N° 4 - Modulo 11
#Este programa solicitara el RUT y devolverá el Digito Verificador

#Solicitar Rut a usuario
rut_user= list(input("\nIngresa tu RUT sin puntos ni dígito verificador: ")) 
rut_user.reverse() #Colocar en reversa y en lista los numeros digitados por el usuario
# print(rut_user)

#Serie numerica
numerical_series=[2, 3, 4, 5, 6, 7]

#Contar el indice del ultimo numero de serie menos 1
index_last_series = len(numerical_series)-1 # 5


#crear una lista vacia
results=[]

#Iteracion sobre el indice, valor y el rut
for index, value in enumerate(rut_user):
    if index > index_last_series:
        index_element = index - 6

    else:
        index_element = index
    results.append(int(value)*numerical_series[index_element]) #Se agregan los valores a la lista results


    if len(results)== len(rut_user): #Si el numero de digitos de la lista "resultado" es iguala al numero de la lista "rut_user"
        list_sum = sum(results)  #sumar los numeros de la lista "results"
        resto=(list_sum%11) #Dividir la suma en 11 y guardar el resto
        dv=11-resto #A 11 restarle el resto

        if dv ==10:
            dv="k"
        elif dv==11:
            dv="0"
        else:
            dv
        
        #Imprimir el resultado
        print(f"Su digito verificador es {dv}\n")
        

