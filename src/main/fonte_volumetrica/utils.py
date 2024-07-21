

def salvar_arquivo(arquivo, topo_cilindro, pts_no_angulo):
    with open(arquivo, 'a') as f:
        f.write(f'{pts_no_angulo} {topo_cilindro}\n')