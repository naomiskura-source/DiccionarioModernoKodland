
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo o enojado",
    "BRAINROT": "Cosas que hacen que te vuelvas más tonto"
}

print("BIENVENIDO AL TRADUCTOR MODERNO")

a = int(input(
    "¿Qué necesitas?\n"
    "1. Traducción de una palabra moderna\n"
    "2. Información\n"
    "Elige una opción: "
))

if a == 1:
    word = input(
        "Escribe una palabra que no entiendas: "
    ).upper()

    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Palabra no encontrada. Mejora tu redacción y vuelve a intentarlo.")

elif a == 2:
    print("Este programa te permitirá entender mejor las palabras modernas.")

else:
    print("Opción no válida. Escribe 1 o 2.")
