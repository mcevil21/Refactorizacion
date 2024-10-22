class NoSePuedeCalcular(Exception):
    pass


def CAL_MEDIDA():
    global calcular_media

    def calcular_media(lista):
        if not lista:
            raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía")
        if not all(isinstance(i, (int, float)) for i in lista):
            raise TypeError("Todos los elementos deben ser numéricos")

        return sum(lista) / len(lista)


CAL_MEDIDA()


import math

def calcular_desviacion_estandar(lista):
    if not lista:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía")
    if not all(isinstance(i, (int, float)) for i in lista):
        raise TypeError("Todos los elementos deben ser numéricos")
    if len(lista) == 1:
        return 0

    media = calcular_media(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(varianza)


