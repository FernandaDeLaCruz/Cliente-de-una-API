import requests

def obtener_terremotos(inicio, fin, magnitud_min=2.5):
    """
    Consulta los terremotos desde la API de USGS según las fechas y magnitud mínima.
    Args:
        inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        fin (str): Fecha de fin en formato 'YYYY-MM-DD'.
        magnitud_min (float): Magnitud mínima del terremoto (por defecto 2.5).
        
    Returns:
        list: Lista de terremotos con detalles relevantes.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    
    # Parámetros de consulta
    params = {
        "format": "geojson",
        "starttime": inicio,
        "endtime": fin,
        "minmagnitude": magnitud_min
    }

    try:
        respuesta = requests.get(url, params=params)
        respuesta.raise_for_status()  # Verifica si hubo errores en la solicitud
        datos = respuesta.json()
        
        terremotos = datos.get("features", [])
        if terremotos:
            print(f"Se encontraron {len(terremotos)} terremotos.")
            for terremoto in terremotos[:5]:  # Muestra los primeros 5 terremotos
                props = terremoto["properties"]
                print(f"\nLugar: {props['place']}")
                print(f"Magnitud: {props['mag']}")
                print(f"Fecha: {props['time']}")
                print(f"Más información: {props['url']}")
        else:
            print("No se encontraron terremotos en el rango especificado.")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

# Ejemplo de uso
obtener_terremotos("2024-10-10", "2024-10-15", 4.0)
