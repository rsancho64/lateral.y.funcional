#! /usr/bin/python3


def doblar(algo):
    """funcion pura que dobla su argumento"""
    valorIntermedio = algo * 2
    return valorIntermedio  


if __name__ == "__main__":
    
    entrada = 3
    salida = doblar(entrada)
    print(salida)  # 6
    print(entrada) # 3
    
    entrada = "ma"
    salida = doblar(entrada)
    print(salida)  # mama
    print(entrada) # ma
    
 