import math
import numpy as np

medias = []
desvios = []

for i in range(1, 10**8 + 1):
    dados = np.loadtxt(f'/fonte_volumetrica/arquivos_gerados/volumetrica/{i}.txt')
    vazao = dados[:, 1] # <- 1st column
    
    angulos_solidos = []
    for value in vazao:
        angulo_solido = (value / i) * 4*np.pi
        angulos_solidos.append(angulo_solido)
        

    media = np.mean(angulos_solidos)
    medias.append(media)
    
    angulo_solido_medio =  media / i * 4*np.pi
    
    
    somatorio = sum((x - media) ** 2 for x in angulos_solidos)
    
    desvio = np.sqrt(somatorio / (len(angulos_solidos)-1))
    
    
    i *= 10



# estimativas = []
# media = 0
# arquivo = 'resulteidos.txt'


# for total, vazao, altura in dados:
#     angulo_estimado = (vazao / total) * 4 * math.pi
#     estimativas.append(angulo_estimado)
#     media += angulo_estimado


# media /= len(dados)


# desvios_padrao = []
# erros = []
# for i, estimativa in enumerate(estimativas):
#     n = dados[i][0]
#     desvio = math.sqrt(((estimativa - media) ** 2) / (n - 1))
#     desvios_padrao.append(desvio)
    
#     erro = desvio / math.sqrt(n)
#     erros.append(erro)
    
# print("Standard Deviation:", desvios_padrao)
# print("Error: ", erros)



# i = 0;
# with open(arquivo, 'a') as f:
#     for erro in erros:
#         f.write(f'{10**i} {estimativas[i]} {erro:.10f}\n')
#         i += 1