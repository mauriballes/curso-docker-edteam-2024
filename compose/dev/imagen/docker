# Imagen base
FROM python:3

# Variables de entorno
ARG MENSAJE
ENV MNS=$MENSAJE

# Ejecutar instrucciones
RUN mkdir /app
RUN mkdir /app2
RUN echo $MENSAJE

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos
# Solo copia archivos
COPY . .
# copia archivos, archivos remotos y comprimidos
ADD . /app2

# El proceso principal que se ejecuta en mi contenedor
CMD ["echo", "Hola Mundo"]