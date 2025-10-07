import sys
from collections import Counter

def contar_frecuencias(texto):
    letras = [c.lower() for c in texto if c.isalpha()]
    total = len(letras)
    count = Counter(letras)
    return {letra: (count[letra] / total) * 100 for letra in count}

frec_esp = {
    'a': 11.96, 'b': 0.92, 'c': 2.92, 'd': 6.87, 'e': 16.78,
    'f': 0.52, 'g': 0.73, 'h': 0.89, 'i': 4.15, 'j': 0.30,
    'k': 0.0, 'l': 8.37, 'm': 2.12, 'n': 7.01, 'ñ': 0.29,
    'o': 8.69, 'p': 2.776, 'q': 1.53, 'r': 4.94, 's': 7.88,
    't': 3.31, 'u': 4.80, 'v': 0.39, 'w': 0.0, 'x': 0.06,
    'y': 1.54, 'z': 0.15
}

def generar_mapa_sustitucion(texto):
    frec_texto = contar_frecuencias(texto)
    letras_texto = sorted(frec_texto, key=lambda x: -frec_texto[x])

    abc = list("abcdefghijklmnñopqrstuvwxyz")
    for letra in abc:
        if letra not in letras_texto:
            letras_texto.append(letra)

    letras_esp = [l for l, _ in sorted(frec_esp.items(), key=lambda x: -x[1])]

    mapa = {cif: real for cif, real in zip(letras_texto, letras_esp)}
    return mapa

def aplicar_descifrado(texto, mapa):
    resultado = ""
    for c in texto:
        if c.isalpha():
            nuevo = mapa.get(c.lower(), c.lower())
            if c.isupper():
                nuevo = nuevo.upper()
            resultado += nuevo
        else:
            resultado += c
    return resultado

def mostrar_mapa(mapa):
    print("\nMapa de sustitución actual:")
    for cif, real in sorted(mapa.items()):
        print(f"{cif} → {real}")
    print("-" * 40)

def descifrado(mapa, texto):
    print("Escribe cambios en formato  letra_cifrada=letra_real  (ej: q=e)")
    print("Escribe 'salir' para terminar.\n")

    while True:
        mostrar_mapa(mapa)
        texto_descifrado = aplicar_descifrado(texto, mapa)
        print("\nTexto descifrado parcial:\n")
        print(texto_descifrado[:1000])  # muestra los primeros 1000 caracteres
        print("\n----------------------------")
        cambio = input("Introduce cambio (o 'q'): ").strip().lower()

        if cambio == "q":
            break

        if "=" not in cambio or len(cambio) != 3:
            print("Formato incorrecto. Usa algo como 'x=e'")
            continue

        cif, real = cambio.split("=")
        if cif not in mapa:
            print("Esa letra cifrada no existe en el mapa.")
            continue

        # Actualizar el mapa: aseguramos que no haya duplicados
        # Si otra letra ya estaba asignada a la 'real', se desasigna
        for k, v in mapa.items():
            if v == real:
                mapa[k] = mapa[cif]
        mapa[cif] = real

        print(f"Cambio aplicado: {cif} → {real}\n")

    print("\n=== Descifrado final ===\n")
    print(aplicar_descifrado(texto, mapa))

# ------------------ Programa principal ------------------
if len(sys.argv) < 2:
    print("Uso: python3 descifrador.py <archivo.txt>")
    sys.exit(1)

ruta_archivo = sys.argv[1]

with open(ruta_archivo, 'r', encoding='utf-8') as f:
    texto_cifrado = f.read()

mapa = generar_mapa_sustitucion(texto_cifrado)
descifrado(mapa, texto_cifrado)


