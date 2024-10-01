import fonte_volumetrica.simulacao as f
from parallel_utils import*
from concurrent.futures import ProcessPoolExecutor


def executar_fonte_volumetrica(parte):
    f.fonte_volumetrica(22.9, 7.2, 2.42, 4.1, 10**4, parte)
    
    
    
'''
DEFINIÇÃO DE PARÂMETROS.
'''
altura_inicial = 0
# altura_final = 80
# incremento = 1
num_threads = 10

# '''
# PRÉ-CALCULANDO AS ALTURAS E ARMAZENANDO EM UM ARRAY.
# '''
# alturas = calcular_alturas(altura_inicial, altura_final, incremento)


# '''DIVISÃO DAS ALTURAS EM GRUPOS/RANGES MENORES'''    
# partes_alturas = dividir_lista(alturas, num_threads)

# for parte in partes_alturas:
#     print("--------------------\n", parte)


alturas = [0]
'''EXECUÇÃO PARALELA '''
with ProcessPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(executar_fonte_volumetrica, alturas) for _ in range(num_threads)]
    
    for future in futures:
        try:
            future.result()
        except Exception as e:
            print(f'Erro: {e}')