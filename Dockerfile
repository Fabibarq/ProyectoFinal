   # Usamos una imagen base de Python
FROM python:3.8-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copy all
COPY . /ProyectoFinal

# Dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD [ "python", "start" ]
