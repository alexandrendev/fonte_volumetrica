from fonte_volumetrica.sort_utils import *
from fonte_volumetrica.utils import *
import numpy as np

def fonte_volumetrica(altura_abertura, raio_abertura, raio_cilindro, altura_cilindro, incremento, sorteios):
    topo_fonte = altura_cilindro
    base_cilindro = 0

    arquivo = 'src/main/fonte_volumetrica/arquivos_gerados/DATA_VOL.txt'

    while topo_fonte < (altura_abertura * 1.5):   
        pts_no_angulo = 0
        topo_fonte = base_cilindro + 4.1
        for i in range(sorteios):
            print(f'sorteios: {i+1}')

            ponto = sorteia_novo_centro(raio_cilindro, topo_fonte, base_cilindro)
            
            if(sorteia_pontos(ponto, altura_abertura, raio_abertura)):
                pts_no_angulo += 1
                    
        salvar_arquivo(arquivo, topo_fonte, pts_no_angulo)
        base_cilindro += incremento



def fonte_pontual(altura_abertura, raio_abertura, incremento, sorteios):
    
    altura_ponto = 0 - incremento;
    while altura_ponto < (altura_abertura * 1.5):
        pts_no_angulo = 0
        altura_ponto += incremento
        print(f'{altura_ponto}')
        for i in range(sorteios):
            #x, y, z
            ponto = np.array([0,0, altura_ponto])
            if(sorteia_pontos(ponto, altura_abertura, raio_abertura)):
                pts_no_angulo += 1   
        arquivo_pontual = f'src/main/fonte_volumetrica/arquivos_gerados/DATA_PONTUAL.txt'
        salvar_arquivo(arquivo_pontual, altura_ponto, pts_no_angulo)   
