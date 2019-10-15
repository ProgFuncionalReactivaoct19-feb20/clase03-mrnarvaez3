"""
	Funcional - Aplicado funcion filter
	Roberto N
"""
def es_vocal(x):
	vocales = ["a", "e", "i", "0", "u"]
	if x in vocales:
		return True
	else:
		return False

datos = ["e", "c", "u", "a", "d", "o", "r"]

resultado = filter(es_vocal, datos)


print(list(resultado))