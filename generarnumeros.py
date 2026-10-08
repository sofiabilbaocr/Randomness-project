import cv2
import numpy as np
import hashlib

TOTAL_NUMEROS = 160000
BYTES_POR_BLOQUE = 1024


def calcular_hash(bloque_bytes):
    return hashlib.sha256(bloque_bytes).digest()


#Abre el video con OpenCV
captura = cv2.VideoCapture("videos/video.mov")
total_frames = int(captura.get(cv2.CAP_PROP_FRAME_COUNT))
total_pares = total_frames - 1

#Cuantos hashes necesita sacar de cada par de frames (cada hash da 32 números)
bloques_por_par = TOTAL_NUMEROS // 32 // total_pares + 1

numeros = []

#Lee el primer frame
hay_frame, frame_anterior = captura.read()

while len(numeros) < TOTAL_NUMEROS:
    # Lee el siguiente frame
    hay_frame, frame_actual = captura.read()
    if not hay_frame:
        break

    #Diferencia entre frames consecutivos
    diferencia = cv2.absdiff(frame_actual, frame_anterior)

    #Se queda solo con el último bit de cada valor
    bits = diferencia & 1

    #junta los bits de 8 en 8 para formar bytes
    bytes_ruido = np.packbits(bits.flatten()).tobytes()

    #Separación entre bloques para repartirlos por todo el frame
    paso = len(bytes_ruido) // bloques_por_par

    #Corta el ruido en bloques repartidos y hasheamos cada uno
    for i in range(bloques_por_par):
        inicio = i * paso
        bloque = bytes_ruido[inicio:inicio + BYTES_POR_BLOQUE]
        resultado = calcular_hash(bloque)

        #Cada byte del hash es un número de 0 a 255
        for byte in resultado:
            numeros.append(byte)

    #el frame actual pasa a ser el anterior
    frame_anterior = frame_actual

captura.release()

#por si se pasa, deja exactamente 160,000
numeros = numeros[:TOTAL_NUMEROS]

#guarda los números, uno por línea
archivo = open("numeros.txt", "w")
for numero in numeros:
    archivo.write(str(numero) + "\n")
archivo.close()

print("Números generados:", len(numeros))