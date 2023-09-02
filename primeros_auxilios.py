#Desafio PRIMEROS AUXILIOS

print("\nBienvenido al modulo de primeros auxilios\nContinua respondiento si/no")


estimulos= (input("\n->¿El paciente responde a estímulos?(si/no): ")).lower()

if estimulos == "si":
    print("\nValorar la necesidad de llvarlo al hospital más cercano\nFin del programa\n ")
    exit()
else:
    print("\nAbrir la vía Aérea")
    respira= (input("\n->¿El paciente respira?(si/no): ")).lower()
    if respira == "si":
        print ("\nPermitirle posición de suficiente ventilación\nFin del programa\n")
        exit()
    else:
        print("\nAdministrar 5 ventilaciones y llamar a ambulancia")

        se_continua_el_ciclo=True
        while se_continua_el_ciclo:
            signos_vida= (input("\n->¿El paciente tiene signos de vida?(si/no): ")).lower()

            if signos_vida =="si":
                print("\nReevaluar la espera de una ambulancia")
                ambulancia= (input("\n->¿Llego la ambulancia?: ")).lower()
                if ambulancia == "si":
                    print("Fin del programa\n")
                    break

            else:
                print("\nAdministrar compresiones toracicas hasta que llegue ambulancia")
                ambulancia= (input("\n->¿Llego la ambulancia?(si/no): ")).lower()

                if ambulancia=="no":
                    se_continua_el_ciclo
