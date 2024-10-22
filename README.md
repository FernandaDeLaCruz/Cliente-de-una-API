-----------------------------------------------------------------
Profesor: Carlos Rafael Levy Rojas				
Materia: LABORATORIO PARA EL DESPLIEGUE DE APLICACIONES		
Alumna: Maria Fernanda Pastrano de la Cruz			
fecha: 15 de Octubre de 2024					
-----------------------------------------------------------------

----------------Descripción de la Actividad----------------------
Realice un cliente que consulte la api de Terremotos de la USGS
https://earthquake.usgs.gov/fdsnws/event/1/
_________________________________________________________________

----------------------Solución-----------------------------------
Consulta los terremotos desde la API de USGS según las fechas y	
magnitud mínima.								
    Args:							
	inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.	
	fin (str): Fecha de fin en formato 'YYYY-MM-DD'.	
	magnitud_min (float): Magnitud mínima del terremoto 	
	(por defecto 2.5).								
    Returns:							
        list: Lista de terremotos con detalles relevantes.	
________________________________________________________________
