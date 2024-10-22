Script para Obtener Terremotos desde la API de USGS

-----Descripción-----

Este proyecto es un script en Python que consulta los datos de terremotos utilizando la API del US Geological Survey (USGS). El usuario puede especificar un rango de fechas y la magnitud mínima para obtener eventos sísmicos registrados. Se muestran los resultados más relevantes, incluidos la ubicación, magnitud y fecha del terremoto, además de un enlace para más información sobre cada evento.
___________________________________________________________________________________________________________________________________

-----Uso del Script-----

El script define una función llamada obtener_terremotos, que recibe los siguientes parámetros:
obtener_terremotos(inicio, fin, magnitud_min=2.5)

* inicio (str): Fecha de inicio en formato YYYY-MM-DD.
* fin (str): Fecha de fin en formato YYYY-MM-DD.
* magnitud_min (float, opcional): Magnitud mínima de los terremotos a consultar. El valor predeterminado es 2.5.

____________________________________________________________________________________________________________________________________

-----Ejemplo de Uso:-----

obtener_terremotos("2024-10-10", "2024-10-15", 4.0)
Este ejemplo buscará terremotos ocurridos entre el 10 y 15 de octubre de 2024 con una magnitud mínima de 4.0.

____________________________________________________________________________________________________________________________________

-----Salida Esperada-----

Si se encuentran terremotos, se mostrará el número total y los detalles de los 5 primeros eventos:
Se encontraron 3 terremotos.
____________________________________________________________________________________________________________________________________

Lugar: 10 km al suroeste de Tulum, México
Magnitud: 4.3
Fecha: 1696875600000
Más información: https://earthquake.usgs.gov/eventpage/us7000ke2m
____________________________________________________________________________________________________________________________________

Lugar: 50 km al noreste de Santiago, Chile
Magnitud: 5.2
Fecha: 1696889200000
Más información: https://earthquake.usgs.gov/eventpage/us7000ke2p
____________________________________________________________________________________________________________________________________
Si no se encuentran terremotos, se mostrará:

No se encontraron terremotos en el rango especificado.

____________________________________________________________________________________________________________________________________

En caso de error en la solicitud, se mostrará el mensaje:

Error en la solicitud: <detalle del error>

____________________________________________________________________________________________________________________________________

-----Posibles Errores-----

* Error en la solicitud: Puede ocurrir si no hay conexión a internet o la API de USGS no está disponible.
* Formato incorrecto de fechas: Asegúrate de proporcionar fechas en el formato YYYY-MM-DD.
