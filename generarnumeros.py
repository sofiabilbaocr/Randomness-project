import cv2

#Se abre el video con OpenCV
captura = cv2.VideoCapture("videos/video.mov")

#Revisa si el video se abrió correctamente
print(f"se abrió el video? {captura.isOpened()}")

#Saca los datos básicos del video
total_frames = int(captura.get(cv2.CAP_PROP_FRAME_COUNT))
fps = captura.get(cv2.CAP_PROP_FPS)
ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Imprime los datos del video
print(f"Total de frames: {total_frames}")
print(f"Frames por segundo: {fps}")
print(f"Resolución: {ancho} x {alto}")

#Cierra el video
captura.release()