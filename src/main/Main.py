import fonte_volumetrica.main as f


print("//////////PREENCHA OS CAMPOS//////////")

altura_abertura = float(input("Altura ate a abertura(cm):"))
raio_abertura = float(input("Digite o raio da abertura(cm):"))
tipo_fonte = int(input("Digite o número correspondente a fonte desejada.\n1-Fonte pontual\n2-Fonte volumetrica:"))

# Fonte volumetrica
if(tipo_fonte == 2):
    altura_fonte = float(input("Digite a altura da fonte(cm): "))
    raio_fonte = float(input("Digite o raio da fonte(cm): "))
    qtde_passos = int(input("Digite a quantidade de deslocamentos da fonte ate a abertura(cm): "))
    sorteios = int(input("Digite a quantidade de sorteios por altura: "))
    
    f.fonte_volumetrica(altura_abertura, raio_abertura, raio_fonte, altura_fonte, qtde_passos, sorteios, True)

else:
    sorteios = int(input("Digite a quantidade de sorteios por altura: "))
    qtde_passos = int(input("Digite a quantidade de deslocamentos da fonte ate a abertura: "))
    f.fonte_volumetrica(altura_abertura, raio_abertura, 0, 0, qtde_passos, sorteios, False)