import numpy as np
# from metodos import *

def sorteia_pontos(centro, altura, raio_abertura):
    theta = np.random.uniform(0,np.pi)
    phi = np.random.uniform(0, 2*np.pi)

    x = centro[0] 
    y = centro[1]
    z = centro[2]

    if(theta != (np.pi / 2)):
        # t = altura - z * np.cos(theta_sorteado)
        eixo_x = x + (altura - z) * np.tan(theta) * np.cos(phi)
        eixo_y = y + (altura - z) * np.tan(theta) * np.sin(phi)

    else: return

    '''
    ///////SE OS VALORES DE x E y ESTIVEREM DENTRO DO RAIO DA ABERTURA//////
    //////////////////ENTÃO O PONTO ESTÁ NO ANGULO SÓLIDO//////////////////
    ''' 
    if(eixo_x >= -raio_abertura and eixo_x <= raio_abertura):
        if(eixo_y >= -raio_abertura and eixo_y <= raio_abertura):
            # pts_no_angulo += 1
            return True

def sorteia_pontos_acima_da_abertura(centro, altura, raio_abertura):
    theta = np.random.uniform(0,np.pi)
    phi = np.random.uniform(0, 2*np.pi)
    
    x = centro[0] 
    y = centro[1]
    z = centro[2]

    if (theta != np.pi / 2 and theta < np.pi / 2):
        eixo_x = x + (altura - z) * np.tan(theta) * np.cos(phi)
        eixo_y = y + (altura - z) * np.tan(theta) * np.sin(phi)
        
    else: return

    if(eixo_x >= -raio_abertura and eixo_x <= raio_abertura):
        if(eixo_y >= -raio_abertura and eixo_y <= raio_abertura):
            # pts_no_angulo += 1
            # Caiu dentro da câmara
            return False
    return True
        
def sorteia_novo_centro(raio_cilindro, altura_cilindro, base_cilindro):
    x = np.random.uniform(-raio_cilindro, raio_cilindro)
    y = np.random.uniform(-raio_cilindro, raio_cilindro)
    z = np.random.uniform(base_cilindro, altura_cilindro)

    return np.array([x,y,z])