import fonte_volumetrica.simulacao as f
from parallel_utils import*
from concurrent.futures import ProcessPoolExecutor


def executar_fonte_pontual(parte):
    f.fonte_pontual(22.9, 7.2, 10**7, parte)


altura_inicial = 0
altura_final = 80
incremento = 1

qtde = 12
alturas = []

alturas = calcular_alturas(altura_inicial, altura_final, incremento)

partes_alturas = dividir_lista(alturas, qtde)

with ProcessPoolExecutor(max_workers=qtde) as executor:
    futures = [executor.submit(executar_fonte_pontual, parte) for parte in partes_alturas]
    
    for future in futures:
        try:
            future.result()
        except Exception as e:
            print(f'Erro: {e}')