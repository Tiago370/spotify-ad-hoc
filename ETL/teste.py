import logging
import threading
import os
from datetime import datetime

def thread_function(num, listaIds):
    logging.info("Thread [%d]: Executando", num)
    print('Thread', num)
    logging.info("Thread [%d]: Finalizando", num)


def separa(lista, parts):
    k, m = divmod(len(lista), parts)
    return (lista[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(parts))


def leIdArtistas(arquivo, partes):
    listaIdArtista = list()
    with open(arquivo) as file_in:
        for line in file_in:
            listaIdArtista.append(line.strip())
    return list(separa(listaIdArtista, partes))

def main():

    # Definicoes logging
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()

    listaIdArtista = leIdArtistas("./ETL/teste.txt", 10)

    for num, parte in enumerate(listaIdArtista):
        logging.info("Main: thread [%d]: Criada e Iniciada", num)
        x = threading.Thread(target=thread_function, args=(num, parte))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread [%d].", index)
        thread.join()
        logging.info("Main: thread [%d] done.", index)


if __name__ == "__main__":
    main()