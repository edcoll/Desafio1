# Desafío 1: Periodos perdidos

Api Generador de Datos
Basada en el Nivel 1
Autor: Edwards Coll
Email: edwardscr@hotmail.com / edwardsbcr@gmail.com
Script realizando en Python Ver. 3.7.3


El Script se ejecuta segun lo solicitado en el nivel 1:

GDD.py < in.json > out.json

Los nombres de los archivos no son mandatorios se han colocado in y out como referencia.

El archivo in.json, debe contener un Json como el indicado en las instrucciones:

```json
{
    "id": 6,
    "fechaCreacion": "1992-09-01",
    "fechaFin": "1994-11-01",
    "fechas": [
      "1993-01-01",
      "1992-12-01",
      "1994-09-01",
      "1993-02-01",
      "1994-06-01",
      "1992-10-01",
      "1993-09-01",
      "1994-01-01"]
}
```

El archivo out.json, como resultado sera la entrada y el campo de fechas tendra adicionalmente las fechas generadas cumpliendo con que se obtendran de forma aleatoria y correspondiente al rango con un maximo de 100 fechas generadas pero no entregando la cantidad completa de fechas generadas.


##################################################################################################################

El desafío consiste en lo siguiente:

-	Existe un servicio REST que llamaremos Generador De Datos o GDD.
	-	El servicio responde con una lista de fechas generadas aleatoriamente. Estas fechas se encuentran en un lapso definidos por dos valores: fechaCreacion y fechaFin.
	-	Cada fecha generada corresponde al primer día de un mes.
	-	La respuesta contienen un máximo de 100 fechas. 
	-	El servicio no entrega todas las fechas dentro del periodo, omite algunas de forma también aleatoria.
-	El objetivo de este ejercicio es que determines cuáles son los periodos que faltan.

Este es un ejemplo de la respuesta que entrega este servicio:

```json
{
    "id": 6,
    "fechaCreacion": "1968-08-01",
    "fechaFin": "1971-06-01",
    "fechas": [
      "1969-03-01",
      "1969-05-01",
      "1969-09-01",
      "1971-05-01"]
}
```

Acá se puede apreciar que el servicio generó fechas entre el 1 de agosto de 1968 y el 1 de junio de 1971. Sólo se generaron 4 fechas en este caso. 
De acuerdo a esto, faltarían 5 fechas de 1968, 9 fechas de 1969 y 5 fechas de 1971.
Una versión del GDD se encuentra en este repositorio en GitHub:
https://github.com/previred/Generador_Datos_Desafio_Uno

El desafío puede ser resuelto de tres maneras distintas. 
Tú eliges cuál es la que más te acomoda entre estos tres niveles:

## Nivel 1: 
	Crear un programa que recibe, a través de la entrada estándar, un archivo en formato Json con la estructura de la respuesta de servicio (como el ejemplo de arriba) y que entrega a través de la salida estándar, como respuesta, un archivo Json con las fechas faltantes.
Ejemplo:
	Se entrega un archivo con este contenido:
	
```json
{
    "id": 6,
    "fechaCreacion": "1969-03-01",
    "fechaFin": "1970-01-01",
    "fechas": [
      "1969-03-01",
      "1969-05-01",
      "1969-09-01",
      "1970-01-01"]
}
```

El programa debe responder con archivo con este contenido:
	
```json
{
    "id": 6,
    "fechaCreacion": "1968-08-01",
    "fechaFin": "1971-06-01",
    "fechasFaltantes": [
      "1969-04-01",
      "1969-06-01",
      "1969-07-01",
      "1969-08-01",
      "1969-10-01",
      "1969-11-01",
      "1969-12-01"]
}
```
 
El programa se debe ejecutar de la siguiente manera:
	$ mi_solucion < nombre_archivo_entrada > nombre_archivo_salida
