Api Generador de Datos
Basada en el Nivel 1
Autor: Edwards Coll
Email: edwardscr@hotmail.com / edwardsbcr@gmail.com
Script realizando en Python Ver. 3.7.3


El Script se ejecuta segun lo solicitado en el nivel 1:

GDD.py < in.json > out.json

Los nombres de los archivos no son mandatorios se han colocado in y out como referencia.

El archivo in.json, debe contener un Json como el indicado en las instrucciones:

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

El archivo out.json, como resultado sera la entrada y el campo de fechas tendra adicionalmente las fechas generadas cumpliendo con que se obtendran de forma aleatoria y correspondiente al rango con un maximo de 100 fechas generadas pero no entregando la cantidad completa de fechas generadas.

