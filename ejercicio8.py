"""
	Ejercicio practica 3
	Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.

	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
	Roberto N
"""

datos = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]

#  Funcion anonima para obtener la palabra necesariax
resultado = filter(lambda x: len(x)%2 == 0, datos)


print(list(resultado))
