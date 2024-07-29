import fonte_volumetrica.simulacao as f

def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

def obter_int(mensagem, opcoes=None):
    while True:
        try:
            valor = int(input(mensagem))
            if opcoes and valor not in opcoes:
                print(f"Por favor, insira um valor válido: {opcoes}")
            elif valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

print("//////////PREENCHA OS CAMPOS//////////")

altura_abertura = obter_float("Altura até a abertura (cm): ")
raio_abertura = obter_float("Digite o raio da abertura (cm): ")
tipo_fonte = obter_int("Digite o número correspondente à fonte desejada.\n1-Fonte pontual\n2-Fonte volumétrica: ", [1, 2])

# Fonte volumétrica
if tipo_fonte == 2:
    altura_fonte = obter_float("Digite a altura da fonte (cm): ")
    raio_fonte = obter_float("Digite o raio da fonte (cm): ")
    qtde_passos = obter_int("Digite o valor do incremento da altura da fonte: ")
    sorteios = obter_int("Digite a quantidade de sorteios por altura: ")
    
    f.fonte_volumetrica(altura_abertura, raio_abertura, raio_fonte, altura_fonte, qtde_passos, sorteios)
else:
    sorteios = obter_int("Digite a quantidade de sorteios por altura: ")
    qtde_passos = obter_int("Digite o valor do incremento da altura da fonte: ")
    f.fonte_pontual(altura_abertura, raio_abertura, qtde_passos, sorteios)
