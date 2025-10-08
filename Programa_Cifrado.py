import string
from collections import Counter

letras = ["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
texto = str(input("¿Qué texto quieres descifrar? : \n"))

def calcular_frecuencia(texto):
    texto_upper = texto.upper()
    counts = Counter(ch for ch in texto_upper if ch in string.ascii_uppercase)
    freq = {ch: counts.get(ch, 0) for ch in string.ascii_uppercase}
    return freq

def sustitucionAutomatica(freq, letras):
    sorted_cipher = sorted(freq.keys(), key=lambda k: freq[k], reverse=True)
    clave = {}
    for i, cipher in enumerate(sorted_cipher):
        clave[cipher] = letras[i] if i < len(letras) else None
    return clave

def sustituir(texto, clave):
    texto_aux = texto.upper()
    for cipher, plain in clave.items():
        if plain:
            texto_aux = texto_aux.replace(cipher, plain)
    return texto_aux

def sustitucionManual(texto, clave):
    texto_act = texto
    while True:
        letraCambio= input("\n¿Qué letra del mensaje quieres cambiar? (Pon STOP para salir) ").strip().lower()
        letra = buscar(clave, letraCambio)
        if letraCambio.upper() == "STOP":
            break
        if len(letra) != 1 or letra not in string.ascii_uppercase:
            print("Por favor, introduce una letra válida (A-Z).")
            continue
        nueva = input("¿Por qué letra la quieres cambiar? ").strip().lower()
        antiguo = clave.get(letra)
        clave[buscar(clave, nueva)] = antiguo
        clave[letra] = nueva
        texto_act = texto_act.replace(nueva, nueva.upper())
        texto_act = texto_act.replace(antiguo, nueva)
        texto_act = texto_act.replace(nueva.upper(), antiguo)
        print("\nTexto actualizado:\n")
        print(texto_act)
        print("\nClave actualizada:")
        print(printClave(clave))
    return texto_act, clave

def buscar(clave, letra):
    cla = ""
    for let in string.ascii_uppercase:
        if clave[let] == letra:
            cla = let
            break
    return cla

def printClave(clave):
    res = ""
    for letra in string.ascii_uppercase:
        val = clave.get(letra)
        res += f"{letra}: {val if val is not None else '-'}; "
    return res

# EJECUCIÓN
freq = calcular_frecuencia(texto)
clave = sustitucionAutomatica(freq, letras)
texto_sustituido = sustituir(texto, clave)

print("\nTexto sustituido automáticamente:\n")
print(texto_sustituido)
print("\nClave inicial:\n")
print(printClave(clave))

texto_final, clave_final = sustitucionManual(texto_sustituido, clave)

print("\nTexto final:\n")
print(texto_final)
print("\nClave final:\n")
print(printClave(clave_final))
