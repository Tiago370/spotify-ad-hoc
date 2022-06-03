import logging
import threading
import os


def leIdArtistas(arquivo):
    listaIdArtista = list()
    with open(arquivo) as file_in:
        for line in file_in:
            listaIdArtista.append(line.strip())
    return listaIdArtista

if __name__ == "__main__":

    listaIdArtista = leIdArtistas("teste.txt")
    listaIdInputados = leIdArtistas("inputados.txt")
    listaDiferentes = list()
    for artista in listaIdArtista:
        if artista not in listaIdInputados:
            listaDiferentes.append(artista)

    print('Tam listaIdArtista = ',len(listaIdArtista))
    print('Tam listaIdInputados = ',len(listaIdInputados))
    print('Tam listaDiferentes = ',len(listaDiferentes))

    with open('inserir.txt', 'w') as f:
        for item in listaDiferentes:
            f.write(item+'\n')

