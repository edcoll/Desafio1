#########################################################
#	Script: Desafio 1 - Api Generador de Datos (GDD)	#
#	Nivel de Entrega: 1									#
#	Autor: Edwards Coll									#
#	Email: edwardscr@hotmail.com / edwardsbcr@gmail.com #
#	Fecha: 23/05/2019									#
#	Python 3.7.3 										# 
#########################################################

#******************Librerias*********************
import sys, json, random;
from datetime import datetime, date

#******************Funciones*********************
def SeparaFecha(fecha):
	y=int(fecha[:4])
	m=int(fecha[5:7])
	d=int(fecha[8:10])
	return [int(y),int(m),int(d)]

def CantFechas(f1,f2,l):
	d1=SeparaFecha(f1)
	d2=SeparaFecha(f2)

	#Se restan 12 meses al inicial ej 12-3=9
	m=12-d1[1]
	y=d2[0]-d1[0]
	a=0
	#Se suman los 1eros meses con los ultimos
	ciclos=m+d2[1]
	#Se ajustan la cantidad de 12 meses por cada year de diferencia
	if y!=1:
		a=1
		while a!=y:
			ciclos=ciclos+12
			a=a+1
	#Se restan la cantidad de fechas que ya existen
	ciclos = ciclos - len(l)

	#Si la cantidad excede de 100 numeros se fijara el numero 100 como maximo
	if ciclos>100:
		ciclos=100
	#print("ciclos "+str(ciclos))
	return ciclos

def TransformarFecha(fecha_completa):
	f=SeparaFecha(fecha_completa)
	try:
		return datetime(f[0],f[1],f[2])
	except:
		print("Formato invalido para la Fecha: "+fecha_completa) 
		exit()

def str_to_date(fecha):
	f=SeparaFecha(fecha)
	return date(f[0],f[1],f[2])

def diferencia(fecha1, fecha2):
    return (fecha2 - fecha1).days
#************************************************

#Tomando el archivo Json
data = json.load(sys.stdin)
#Validando Fecha Fin mayor a Fecha Creacion
f1=str_to_date(data["fechaCreacion"])
f2=str_to_date(data["fechaFin"])
result = diferencia(f1, f2)
if result <= 0:
	print("Error, fechaFin no puede ser mayor a fechaCreacion")
	exit()
#Calcular Cantidad de fechas posibles
cant_ciclos = CantFechas(data["fechaCreacion"],data["fechaFin"],data["fechas"])
#Se define un rango entre 1 y la cantidad de ciclos posibles calculados
ciclosTotales=random.randrange(1,cant_ciclos)

#Se inicia Identificando Fecha de Creacion y Fin
ini = TransformarFecha(data["fechaCreacion"])
fin = TransformarFecha(data["fechaFin"])

while ciclosTotales>0:
	#Generando Fecha Random
	f_random = ini + (fin - ini) * random.random()
	#Se ajusta la fecha obtenida en formato y corresponda a la 1era del mes
	fix_random = f_random.strftime('%Y-%m-01')
	#Se compara si la fecha ya existe en la lista de fechas para evitar redundancia
	x=0
	for fecha in data["fechas"]:
		if str(fix_random) == fecha:
			x=1
	if x!=1:
		#print("Agregar Fecha")
		data["fechas"].append(fix_random)
	ciclosTotales=ciclosTotales-1

#Transformar e imprimir Json
json = json.dumps(data)
print(json)
