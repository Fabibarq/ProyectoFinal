import requests
import csv

# Clave API de News API
API_KEY = '4f35dbf672a8466dac264e768e746df1'

# URL de API base
BASE_URL = 'https://newsapi.org/v2/'

def obtener_noticias(fuente):
    # Endpoint para obtener las principales noticias de una fuente específica
    endpoint = 'top-headlines'
    # Parámetros de la solicitud
    params = {
        'sources': fuente,
        'apiKey': API_KEY
    }
    # Realizar solicitud HTTP
    response = requests.get(BASE_URL + endpoint, params=params)
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Procesar la respuesta JSON
        data = response.json()
        return data['articles']
    else:
        print("Error al obtener las noticias:", response.status_code)
        return None

def guardar_csv(noticias, nombre_archivo):
    # Nombre del archivo CSV
    csv_file = nombre_archivo + '.csv'
    # Abrir el archivo CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Crear el objeto escritor CSV
        writer = csv.writer(csvfile)
        # Escribir el encabezado del archivo CSV
        writer.writerow(['Título', 'Descripción', 'URL'])
        # Escribe cada artículo en el archivo CSV
        for article in noticias:
            writer.writerow([article['title'], article['description'], article['url']])
    print(f"Respuesta JSON guardada correctamente en {csv_file}")

def main():
    print("Selecciona la fuente de noticias:")
    print("1. BBC")
    print("2. Reuters")
    print("3. CNN")
    opcion = input("Ingrese el número correspondiente a la fuente de noticias: ")
    
    if opcion == '1':
        fuente = 'bbc-news'
    elif opcion == '2':
        fuente = 'reuters'
    elif opcion == '3':
        fuente = 'cnn'
    else:
        print("Opción inválida. Saliendo del programa.")
        return
    
    nombre_archivo = "noticiasapi.csv"
    
    # Obtiene las noticias de la fuente especificada
    noticias = obtener_noticias(fuente)
    if noticias:
        # Guarda las noticias en un archivo CSV
        guardar_csv(noticias, nombre_archivo)

if __name__ == "__main__":
    main()
