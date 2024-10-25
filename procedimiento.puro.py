#! /usr/bin/python3

__objeto = [11, 22, 33]  # objeto y estado global
             # lo alcanza todo el codigo 

def doblarLista(posicion):
    """procedimiento puro de doblar un item 
    en la lista particular __objeto, que es global"""
    global  __objeto
    __objeto[posicion] = __objeto[posicion] * 2

# TO DO ....
def doblar(lista, donde):
    """procedimiento puro de doblar un item en una lista"""
    pass
    # nonlocal lista  :/
    # lista[donde] = lista[donde]  * 2 :/

if __name__ == "__main__":
    
    print(__objeto)  # [11, 22, 33]
    doblarLista(1) # procedimiento puro
    print(__objeto)  # [11, 44, 33]

    lista0 = ["ma","pa"]
 
    print(lista0)  # ["ma","pa"]
    doblar(lista0, 1) # procedimiento puro
    print(lista0)  # ["ma","papa"]

    

 