import requests

# Clave API de News API
API_KEY = '4f35dbf672a8466dac264e768e746df1'

# URL de API
BASE_URL = 'https://newsapi.org/v2/'

# Endpoint de una fuente específica
endpoint = 'top-headlines'

# Parámetros de la solicitud
params = {
    'sources': 'bbc-news',  # Cambia la fuente según tus preferencias
    'apiKey': API_KEY
}

# Realiza la solicitud HTTP
response = requests.get(BASE_URL + endpoint, params=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Procesa la respuesta JSON
    data = response.json()
    # Nombre del archivo CSV
    csv_file = 'NOTICIASAPI.csv'
    # Abre el archivo CSV en modo escritura
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Crea el objeto escritor CSV
        writer = csv.writer(csvfile)
        # Escribe el encabezado del archivo CSV
        writer.writerow(['Título', 'Descripción', 'URL'])
        # Escribe cada artículo en el archivo CSV
        for article in data['articles']:
            writer.writerow([article['title'], article['description'], article['url']])
    print("Respuesta JSON guardada correctamente en NOTICIASAPI.csv")
    # Imprime el título de cada noticia
    for article in data['articles']:
        print(article['title'])
else:
    print("Error al obtener las noticias:", response.status_code)# Realiza la solicitud HTTP
response = requests.get(BASE_URL + endpoint, params=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Procesa la respuesta JSON
    data = response.json()
    # Nombre del archivo CSV
    csv_file = 'NOTICIASAPI.csv'
    # Abre el archivo CSV en modo escritura
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Crea el objeto escritor CSV
        writer = csv.writer(csvfile)
        # Escribe el encabezado del archivo CSV
        writer.writerow(['Título', 'Descripción', 'URL'])
        # Escribe cada artículo en el archivo CSV
        for article in data['articles']:
            writer.writerow([article['title'], article['description'], article['url']])
    print("Respuesta JSON guardada correctamente en NOTICIASAPI.csv")
    # Imprime el título de cada noticia
    for article in data['articles']:
        print(article['title'])
else:
    print("Error al obtener las noticias:", response.status_code)
