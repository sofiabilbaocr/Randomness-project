import cv2
import numpy as np
import hashlib

total_numeros = 160000
bytes_por_bloque = 1024

def calcular_hash(bloque_bytes):
    return hashlib.sha256(bloque_bytes).digest()

#Abre el video con OpenCV
captura = cv2.VideoCapture("videos/video.mov")
total_frames = int(captura.get(cv2.CAP_PROP_FRAME_COUNT))
total_pares = total_frames - 1

#Revisa si el video se abrió correctamente
print(f"se abrió el video? {captura.isOpened()}")

#Saca los demás datos básicos del video
fps = captura.get(cv2.CAP_PROP_FPS)
ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Imprime los datos del video
print(f"Total de frames: {total_frames}")
print(f"Frames por segundo: {fps}")
print(f"Resolución: {ancho} x {alto}")

#Cuantos hashes necesita sacar de cada par de frames (cada hash da 32 números)
bloques_por_par = total_numeros // 32 // total_pares + 1

numeros = []
pares_usados = 0

#Lee el primer frame
hay_frame, frame_anterior = captura.read()

while len(numeros) < total_numeros:
    #Lee el siguiente frame
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

    #Corta el ruido en bloques repartidos y hashea cada uno
    for i in range(bloques_por_par):
        inicio = i * paso
        bloque = bytes_ruido[inicio:inicio + bytes_por_bloque]
        resultado = calcular_hash(bloque)

        #Cada byte del hash es un número de 0 a 255
        for byte in resultado:
            numeros.append(byte)

    #el frame actual pasa a ser el anterior
    frame_anterior = frame_actual
    pares_usados += 1

captura.release()

#por si se pasa  deja solo 160,000
numeros = numeros[:total_numeros]

#guarda los números, uno por línea
archivo = open("numeros.txt", "w")
for numero in numeros:
    archivo.write(str(numero) + "\n")
archivo.close()

print(f"Pares de frames usados: {pares_usados}")
print("Números generados:", len(numeros))