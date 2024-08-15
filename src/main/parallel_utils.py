
def dividir_lista(lista, partes):
    comprimento = len(lista)
    tamanho_parte = comprimento // partes
    resto = comprimento % partes
    
    sublistas = []
    inicio = 0
    
    for i in range(partes):
        fim = inicio + tamanho_parte + (1 if i < resto else 0)  # Adiciona 1 elemento extra para as primeiras "resto" partes
        sublistas.append(lista[inicio:fim])
        inicio = fim
    
    return sublistas

def calcular_alturas(altura_inicial, altura_final, incremento):
    alturas = []
    altura_atual = altura_inicial

    while altura_atual <= altura_final:
        alturas.append(altura_atual)
        altura_atual += incremento
        
    return alturas