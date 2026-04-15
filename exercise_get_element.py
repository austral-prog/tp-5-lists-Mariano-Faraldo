def get_element(lista, indice):

    largo = len(lista)

    if indice >= largo or indice < -largo:
        return None
    else:
        return lista[indice]
    