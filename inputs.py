
print("Opcion 1: Agregar \nOpcion 2: Eliminar \nOpcion 3: editar")
def tareas():
    lista=[]
  
    while  True:  
        opcion=input('Ingresar opcion: ')
        if int(opcion)==1:
            elemento=input('Ingresa valor: ')
            lista.append(elemento)
            print('nueva lista',lista)
        if int(opcion)==2:
             posicion=input('valor a eliminar: ')
             lista.remove(posicion)
             print('nueva lista',lista)
        if int(opcion)==3:
             posicionElemento=input('tarea a Modificar: ')
             nuevoValor=input('nuevo valor: ')
             lista[int(posicionElemento)] = nuevoValor
             print('nueva lista',lista)
        if int(opcion)==4:
            break;

tareas()