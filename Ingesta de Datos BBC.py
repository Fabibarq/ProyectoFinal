# Este archivo está desactivado y no debe ejecutarse.
# Solo se proporciona como referencia.

import requests
from bs4 import BeautifulSoup
import csv

def obtener_noticias_covid_bbc():
    try:
        termino_busqueda = 'covid'
        url = f'https://www.bbc.co.uk/search?q={termino_busqueda}&filter=news&s=news&dateTo=2024-12-31&dateFrom=2023-01-01&scope=all'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links_noticias = soup.find_all('a')
            urls_noticias = [link['href'] for link in links_noticias if 'article' in link['href']]
            return urls_noticias
        else:
            print(f"Error al realizar la solicitud HTTP: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al obtener las noticias: {e}")
        return None

def obtener_noticia_bbc(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            titulo_noticia =soup.find('h1', class_='ssrcss-1j9m63o-StyledHeading')
            if titulo_noticia is not None:
                titulo = titulo_noticia.get_text()
            else:
                titulo = ''  # Asignar una cadena vacía en lugar de 'Título no encontrado'
            resumen_noticia = soup.find('p', class_='ssrcss-1ww1cww-MetadataSnippet ec2lxfp0')
            if resumen_noticia:
                resumen = resumen_noticia.get_text()
            else:
                resumen = 'Resumen no encontrado'
            paragraphs = soup.find_all('p')
            texto_noticia = '\n'.join([p.get_text() for p in paragraphs])
            return titulo, resumen, texto_noticia
        else:
            print(f"Error al realizar la solicitud HTTP: {response.status_code}")
            return '', '', ''  # Devolver cadenas vacías en lugar de None
    except Exception as e:
        print(f"Error al obtener la noticia: {e}")
        return '', '', ''  # Devolver cadenas vacías en lugar de None

def exportar_csv(titulo, resumen, texto_noticia, nombre_archivo):
    if texto_noticia:
        try:
            with open(nombre_archivo, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([titulo, resumen, texto_noticia])
            print(f"Noticia exportada correctamente a {nombre_archivo}")
        except Exception as e:
            print(f"Error al exportar la noticia a CSV: {e}")

def analizar_noticias_covid_bbc(nombre_archivo='noticias_covid_bbc.csv'):
    noticias_covid_bbc = obtener_noticias_covid_bbc()
    if noticias_covid_bbc is not None:
        for url in noticias_covid_bbc:
            try:
                titulo, resumen, texto_noticia = obtener_noticia_bbc(url)
                exportar_csv(titulo, resumen, texto_noticia, nombre_archivo)
            except Exception as e:
                print(f"Error al analizar la noticia: {e}")
                continue
    else:
        print("No se encontraron noticias sobre COVID en BBC")

analizar_noticias_covid_bbc()
