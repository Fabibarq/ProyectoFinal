import csv
from textblob import TextBlob
import matplotlib.pyplot as plt

def obtener_porcentaje_fake(texto):
    sentimiento = TextBlob(texto).sentiment.polarity
    porcentaje_neutral = (1 - abs(sentimiento)) * 100
    porcentaje_positivo = max(0, sentimiento) * 100
    porcentaje_negativo = max(0, -sentimiento) * 100
    porcentaje_fake = (porcentaje_positivo + porcentaje_negativo) / 2  # Tomamos el promedio de positividad y negatividad como fake
    return porcentaje_neutral, porcentaje_positivo, porcentaje_negativo, porcentaje_fake

def obtener_porcentaje_fake_general(archivo_csv):
    porcentajes_neutral = []
    porcentajes_positivo = []
    porcentajes_negativo = []
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            if len(fila) >= 3:
                _, _, texto_noticia = fila
                neutral, positivo, negativo, fake = obtener_porcentaje_fake(texto_noticia)
                porcentajes_neutral.append(neutral)
                porcentajes_positivo.append(positivo)
                porcentajes_negativo.append(negativo)
    if porcentajes_neutral:
        porcentaje_neutral_promedio = sum(porcentajes_neutral) / len(porcentajes_neutral)
        porcentaje_positivo_promedio = sum(porcentajes_positivo) / len(porcentajes_positivo)
        porcentaje_negativo_promedio = sum(porcentajes_negativo) / len(porcentajes_negativo)
        porcentaje_fake = (porcentaje_positivo_promedio + porcentaje_negativo_promedio) / 2  # Tomamos el promedio de positividad y negatividad como fake
        return porcentaje_neutral_promedio, porcentaje_positivo_promedio, porcentaje_negativo_promedio, porcentaje_fake
    else:
        return None, None, None, None

def graficar_desglose_porcentaje_fake(porcentaje_neutral, porcentaje_positivo, porcentaje_negativo):
    if porcentaje_neutral is not None:
        labels = ['Neutral', 'Positivo', 'Negativo']
        sizes = [porcentaje_neutral, porcentaje_positivo, porcentaje_negativo]
        explode = (0.1, 0, 0)  # Explode neutral slice
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Desglose del Porcentaje de Sentimientos')
        plt.axis('equal')
        plt.savefig('desglose_porcentaje_fake.png')  # Guardar el gráfico como imagen PNG
        plt.show()
    else:
        print("No se encontraron datos para graficar.")

# Nombre del archivo CSV con las noticias de la BBC
archivo_csv = 'NOTICIASAPI.csv'

# Obtener el porcentaje general de fake news en la página de la BBC
porcentaje_neutral, porcentaje_positivo, porcentaje_negativo, porcentaje_fake = obtener_porcentaje_fake_general(archivo_csv)
if porcentaje_fake is not None:
    print(f"Porcentaje general de fake news en la BBC: {porcentaje_fake:.2f}%")
    print(f"Porcentaje de Neutralidad: {porcentaje_neutral:.2f}%")
    print(f"Porcentaje de Positividad: {porcentaje_positivo:.2f}%")
    print(f"Porcentaje de Negatividad: {porcentaje_negativo:.2f}%")
    # Generar y mostrar el gráfico descriptivo
    graficar_desglose_porcentaje_fake(porcentaje_neutral, porcentaje_positivo, porcentaje_negativo)
else:
    print("No se encontraron datos para calcular el porcentaje de fake news.")
