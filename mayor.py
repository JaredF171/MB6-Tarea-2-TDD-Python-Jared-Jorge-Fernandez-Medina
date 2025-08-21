def mayor(lista):
    if not lista:
        return None
    
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor