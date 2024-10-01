from fonte_volumetrica.sort_utils import *
from fonte_volumetrica.utils import *
import numpy as np

def fonte_volumetrica(altura_abertura, raio_abertura, raio_cilindro, altura_cilindro, sorteios, alturas):
    
    base_cilindro = alturas[0]
    topo_fonte = base_cilindro + altura_cilindro

    arquivo = f'src/main/fonte_volumetrica/arquivos_gerados/volumetrica/{sorteios}.txt'

    for base_cilindro in alturas:  
        pts_no_angulo = 0
        topo_fonte = base_cilindro + altura_cilindro
        for i in range(sorteios):
            # print(f'sorteios: {i+1}')

            ponto = sorteia_novo_centro(raio_cilindro, topo_fonte, base_cilindro)
            
            if(ponto[2] <= altura_abertura):
                if(sorteia_pontos(ponto, altura_abertura, raio_abertura)):
                    pts_no_angulo += 1
            elif(ponto[2] > altura_abertura):
                if(not sorteia_pontos_acima_da_abertura(ponto, altura_abertura, raio_abertura)):
                    pts_no_angulo += 1
                    
        salvar_arquivo(arquivo, (topo_fonte - (altura_cilindro/2)), pts_no_angulo)
    

def fonte_pontual(altura_abertura, raio_abertura, sorteios, alturas):
    for altura_ponto in alturas:
        pts_no_angulo = 0
        # print(f'{altura_ponto}')
        for i in range(sorteios):
            #x, y, z
            ponto = np.array([0,0, altura_ponto])
            if(altura_ponto < altura_abertura):
                if(sorteia_pontos(ponto, altura_abertura, raio_abertura)):
                    pts_no_angulo += 1   
            elif(altura_ponto > altura_abertura):
                if(not sorteia_pontos_acima_da_abertura(ponto, altura_abertura, raio_abertura)):
                    pts_no_angulo += 1
            
        arquivo_pontual = f'src/main/fonte_volumetrica/arquivos_gerados/pontual/inicio:{alturas[0]}.txt'
        salvar_arquivo(arquivo_pontual, altura_ponto, pts_no_angulo)   
