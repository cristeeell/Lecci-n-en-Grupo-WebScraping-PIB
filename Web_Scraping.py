import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://datosmacro.expansion.com/pib/ecuador"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tabla_pib = soup.find('table')
    filas = (tabla_pib.find_all('tr'))
    fechas = []
    pib_anual = []
    var_pib_percent = []

    for fila in filas[1:]:
        columnas = fila.find_all('td')
        fechas.append(columnas[0].text.strip())
        pib_dolares = (columnas[2].text.strip().replace("\xa0M$", ""))
        pib_anual.append(f"${pib_dolares}")
        var_pib_percent.append(columnas[3].text.strip())

# DataFrame de pandas
    df = pd.DataFrame({
        'Fecha': fechas,
        'PIB Anual': pib_anual,
        'Var. PIB %': var_pib_percent
    })

# Guardar el DataFrame en un archivo CSV
    df.to_csv('pib_ecuador.csv', index=False)

    print("Felicidades!,El archivo CSV a sido generado exitosamente.")
else:
    print(f"Lo sentimos!,No se pudo acceder al sitio web. Código de estado: {response.status_code}")

print(fechas)
print(pib_anual)
print(var_pib_percent)

#Integrantes del grupo1:
#Moncada Vera Genesis
#Lema Leon Sara
#Salagata Gualpa Damaris
#Sellan Quiñonez Cristell