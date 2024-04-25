Proyecto de Análisis de Fake News con NLP
Este proyecto consiste en un sistema de análisis de noticias relacionadas con COVID-19 en el sitio web de la BBC. El sistema recopila noticias, analiza su contenido y calcula el porcentaje general de "fake news" en función del sentimiento de las noticias.

Funcionalidades
Recopilación de noticias: El sistema obtiene noticias relacionadas con COVID-19 del sitio web de la BBC.
Análisis de sentimientos: Utiliza TextBlob para analizar el sentimiento de las noticias y determinar si son positivas, negativas o neutrales.
Cálculo del porcentaje de "fake news": Basado en el análisis de sentimientos, el sistema calcula el porcentaje general de "fake news" en las noticias recopiladas.
Configuración del Proyecto
Clonar el Repositorio:
bash
Copy code
git clone https://github.com/Fabibarq/ProyectoFinal.git
Instalar Dependencias:
Copy code
pip install -r requirements.txt
Ejecutar el Proyecto:
css
Copy code
python main.py
Estructura del Proyecto
main.py: Archivo principal del proyecto que contiene la lógica principal.
utils.py: Contiene funciones utilitarias para la recopilación y análisis de noticias.
noticias_covid_bbc.csv: Archivo CSV donde se almacenan las noticias recopiladas.
requirements.txt: Archivo que especifica las dependencias del proyecto.
Contribución
Si deseas contribuir a este proyecto, ¡eres bienvenido! Puedes enviar solicitudes de extracción con mejoras, correcciones de errores o nuevas características.

Créditos
Este proyecto fue creado por Fabian Barquero Chacon.