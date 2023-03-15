import cv2

# Cargar el clasificador de caras pre-entrenado
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Bucle principal de procesamiento de video
while True:
    # Capturar un cuadro de video
    ret, frame = cap.read()
    
    # Convertir el cuadro a escala de grises para facilitar la detección de caras
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en el cuadro actual utilizando el clasificador de caras
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Dibujar un cuadro delimitador alrededor de cada cara detectada
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    # Mostrar el cuadro de video con los cuadros delimitadores dibujados
    cv2.imshow('Video',frame)
    
    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()