def remove_elements(lista):
    if len(lista) > 5:
        lista.pop(5)
    if len(lista) > 4:
        lista.pop(4)
    if len(lista) > 0:
        lista.pop(0)
    return lista