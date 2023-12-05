# Face Detection using OpenCV

Este repositorio contiene un script en Python que utiliza OpenCV para realizar la detección de caras en tiempo real a partir de una transmisión de video de la cámara. Se emplea un clasificador pre-entrenado de caras para identificar y delimitar las caras detectadas en el video.

## Descripción del Código

El script utiliza la biblioteca OpenCV para capturar video desde la cámara, convierte cada cuadro de video a escala de grises y luego utiliza un clasificador de Haar pre-entrenado para detectar caras en el cuadro actual. Las caras detectadas se resaltan con un cuadro delimitador de color verde en el video en tiempo real.

## Uso

Para ejecutar el código, se requiere tener OpenCV instalado y el clasificador pre-entrenado de caras (haarcascade_frontalface_default.xml) en el mismo directorio que el script. El programa se ejecuta y muestra la transmisión de video en una ventana, con las caras detectadas resaltadas por cuadros delimitadores verdes. Para salir del programa, presiona la tecla 'q'.

## Requisitos

El script está escrito en Python y utiliza la biblioteca OpenCV. Asegúrate de tener instalada la versión correspondiente de OpenCV para su ejecución.

## Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la detección de caras, optimizar el código o agregar nuevas funcionalidades, siéntete libre de abrir un issue o enviar un pull request.

---

¡Gracias por revisar este repositorio! Si encuentras útil este código o tienes alguna pregunta, no dudes en ponerte en contacto.
