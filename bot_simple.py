from emtvlcapi import *

parada = input("Parada: ")

lineas = emtvlcapi.get_bus_times(stop=parada)

for linea in lineas:
    print(linea)