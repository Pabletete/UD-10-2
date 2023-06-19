import requests
from bs4 import BeautifulSoup

def extraer_datos_web(url):
    # Realizar la petición GET a la página web
    response = requests.get(url)

    # Verificar si la petición fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup con el contenido HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraer los datos de la página web
        # Aquí puedes agregar el código específico para extraer la información que necesitas
        # Puedes utilizar las funciones y métodos de BeautifulSoup para buscar y manipular elementos HTML

        # Ejemplo: Extraer el título de la página
        titulo = soup.title.string
        print("Título:", titulo)

        # Ejemplo: Extraer todos los enlaces de la página
        enlaces = soup.find_all('a')
        print("Enlaces:")
        for enlace in enlaces:
            print(enlace['href'])
    else:
        print("No se pudo acceder a la página:", response.status_code)


# Ejemplo de uso
url = 'https://www.cosmopolitan.com/es/consejos-planes/planes-ocio/a41078807/datos-curiosos-impresionar/'
extraer_datos_web(url)
