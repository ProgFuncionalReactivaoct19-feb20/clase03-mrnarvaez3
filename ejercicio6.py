"""
	ejercicio practica 1 
	Dado un conjunto de palabras, filtrar todas aquellas que sean palindromas 
	Roberto N
"""

#  metodo para comparar la palabra original con la palabra invertida
def palindromas(x):
	palabra = "".join(reversed(x))
	if x == palabra:
		return True
	else:
		return False

datos = ["oro", "pais", "oso", "radar", "sol", "seres"]

resultado = filter(palindromas, datos)


print(list(resultado))