import math

dados = [
    [1, 0, 1.3048414636],
    [10, 1, 0.0152435704],
    [100, 13, 0.0328786716],
    [1000, 127, 0.0092049983],
    [10000, 1148, 0.0013777788],
    [100000, 11515, 0.0004496003],
    [1000000, 116037, 0.0001533225],
    [10000000, 1157912, 0.0000475081],
    [100000000, 11574566, 0.0000149661]
]


estimativas = []
media = 0
arquivo = 'resulteidos.txt'


for total, vazao, altura in dados:
    angulo_estimado = (vazao / total) * 4 * math.pi
    estimativas.append(angulo_estimado)
    media += angulo_estimado


media /= len(dados)


desvios_padrao = []
erros = []
for i, estimativa in enumerate(estimativas):
    n = dados[i][0]
    desvio = math.sqrt(((estimativa - media) ** 2) / (n - 1))
    desvios_padrao.append(desvio)
    
    erro = desvio / math.sqrt(n)
    erros.append(erro)
    
print("Standard Deviation:", desvios_padrao)
print("Error: ", erros)



i = 0;
with open(arquivo, 'a') as f:
    for erro in erros:
        f.write(f'{10**i} {estimativas[i]} {erro:.10f}\n')
        i += 1