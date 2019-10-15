"""
	ejercicio practica 2
	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

	Loja, Pichincha, Esmeraldas, Azuay, Imbabura

 

	Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
	Roberto N
 """



datos = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]

#  Funcion anonima para hacer la comparacion de la primera letra de cada placa

resultado = filter(lambda x: x[0] =="l" or x[0] == "p" or x[0]=="e" or x[0] == "a" or x[0] == "i", datos)


print(list(resultado))

