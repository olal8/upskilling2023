
def sumar(elementos):
    lista=[];
    suma=0
    for elemento in elementos:
        if isinstance(elemento,int):
             suma+=elemento
             lista.append(elemento)
    print(suma)
    return lista;
            

listaElementos = [1, "2", 3,4,"cinco",6]
print(sumar(listaElementos))
