import numpy as np
import time
# from metodos import *

np.random.seed(int(time.time()))

def sorteia_pontos(centro, altura, raio_abertura):
    theta = np.random.uniform(0,np.pi)
    phi = np.random.uniform(0, 2*np.pi)

    x = centro[0] 
    y = centro[1]
    z = centro[2]

    #theta < pi/2 (Direção acima do eixo x)
    if(theta_maior_pi_sobre_2(theta)): return False
    
    # t = altura - z * np.cos(theta_sorteado)
    eixo_x = x + abs((altura - z)) * np.tan(theta) * np.cos(phi)
    eixo_y = y + abs((altura - z)) * np.tan(theta) * np.sin(phi)

    '''
    ///////SE OS VALORES DE x E y ESTIVEREM DENTRO DO RAIO DA ABERTURA//////
    //////////////////ENTÃO O PONTO ESTÁ NO ANGULO SÓLIDO//////////////////
    ''' 
    if(eixo_x >= -raio_abertura and eixo_x <= raio_abertura):
        if(eixo_y >= -raio_abertura and eixo_y <= raio_abertura):
            # pts_no_angulo += 1
            return True

def sorteia_pontos_acima_da_abertura(centro, altura, raio_abertura):
    x = centro[0] 
    y = centro[1]
    z = centro[2]
    
    theta = np.random.uniform(0,np.pi)
    
    if (not theta_maior_pi_sobre_2(theta)): return False
    
    phi = np.random.uniform(0, 2*np.pi)
    
    eixo_x = x + abs((z - altura)) * np.tan(theta) * np.cos(phi)
    eixo_y = y + abs((z - altura)) * np.tan(theta) * np.sin(phi)
        

    if(eixo_x >= -raio_abertura and eixo_x <= raio_abertura):
        if(eixo_y >= -raio_abertura and eixo_y <= raio_abertura):
            return True
    return False
        
def sorteia_novo_centro(raio_cilindro, altura_cilindro, base_cilindro):
    x = np.random.uniform(-raio_cilindro, raio_cilindro)
    y = np.random.uniform(-raio_cilindro, raio_cilindro)
    z = np.random.uniform(base_cilindro, altura_cilindro)

    return np.array([x,y,z])


# Se theta > pi/2 retorna True
def theta_maior_pi_sobre_2(theta):  
    return theta > (np.pi / 2)
