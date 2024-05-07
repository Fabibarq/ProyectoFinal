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
    # Guardar las respuestas JSON en un archivo
    with open('noticiasapi.json', 'w') as outfile:
        json.dump(data, outfile)
    print("Respuesta JSON guardada correctamente en noticiasapi.json")
    # Imprimir el título de cada noticia
    for article in data['articles']:
        print(article['title'])
else:
    print("Error al obtener las noticias:", response.status_code)
