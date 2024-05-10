# deploy.py

import subprocess

# Comandos de despliegue de la aplicación Flask con Docker
COMANDOS_DESPLIEGUE = [
    'cd ProyectoFinal',  # Navegar al directorio de la aplicación
    'git pull origin main',       # Actualizar el repositorio con los últimos cambios
    'docker-compose down',        # Detener los contenedores existentes
    'docker-compose up -d --build',  # Construir y levantar los contenedores
]

# Función para ejecutar comandos del sistema
def ejecutar_comandos_sistema(comandos):
    for comando in comandos:
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        if salida:
            print(salida.decode('utf-8'))
        if error:
            print(error.decode('utf-8'))

# Ejecutar comandos de despliegue
if __name__ == '__main__':
    ejecutar_comandos_sistema(COMANDOS_DESPLIEGUE)
