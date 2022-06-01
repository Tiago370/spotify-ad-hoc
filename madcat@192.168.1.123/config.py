import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = 'host={} dbname={} user={} password={}'.format(os.getenv('HOST'), os.getenv('DATABASE'), os.getenv('USER'), os.getenv('PASSWORD'))
        return self
    
    def alteraBD(self, stringSQL, valores):
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            conexao=psycopg2.connect(config.setParametros(self).dadosconexao)
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()
            # Executor o comando em memoria RAM
            sessao.execute(stringSQL, valores)
            # Comitar no hanco
            conexao.commit()
            # Encerror a sessão
            sessao.close()
        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'

    def consultaBD(self, stringSQL, valores):
        # iniciar a conexo vazia
        conn = None
        try:

            # abrir a conexão
            conexao=psycopg2.connect(config.setParametros(self).dadosconexao)
            
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()

            # Executor o comando em memoria RAM
            sessao.execute(stringSQL, valores)

            registros = sessao.fetchall()
            colnames = [desc[0] for desc in sessao.description]

            # Comitar no hanco
            # conexao.commit()

            # Encerror a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return (colnames, registros)

    def insertArtistaGenres(self, string_SQL_artista, string_SQL_generos, dados_artista, listaGeneros, idArtista):
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            conexao=psycopg2.connect(config.setParametros(self).dadosconexao)
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()
            # Executor o comando em memoria RAM
            sessao.execute(string_SQL_artista, dados_artista)
            # Executar a inserção dos produtos na memoria RAM - TABLA ORDERDETAILS
            for genero in listaGeneros:
                sessao.execute(string_SQL_generos, (idArtista, genero))
            # Comitar TODAS as inserções - fechar a transação
            conexao.commit()
            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'

    def insertAlbumsArtists(self, string_SQL_album, string_SQL_artistas, dados_album, listaArtistas, idAlbum):
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            conexao=psycopg2.connect(config.setParametros(self).dadosconexao)
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()
            # Executor o comando em memoria RAM
            sessao.execute(string_SQL_album, dados_album)
            # Executar a inserção dos produtos na memoria RAM - TABLA ORDERDETAILS
            for artista in listaArtistas:
                sessao.execute(string_SQL_artistas, (artista['id'], idAlbum, artista['isOwner']))
            # Comitar TODAS as inserções - fechar a transação
            conexao.commit()
            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'

    def insertTracksArtists(self, string_SQL_track, string_SQL_artistas, dados_track, listaArtistas, idTrack):
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            conexao=psycopg2.connect(config.setParametros(self).dadosconexao)
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()
            # Executor o comando em memoria RAM
            sessao.execute(string_SQL_track, dados_track)
            # Executar a inserção dos produtos na memoria RAM - TABLA ORDERDETAILS
            for artista in listaArtistas:
                sessao.execute(string_SQL_artistas, (artista['id'], idTrack, artista['isOwner']))
            # Comitar TODAS as inserções - fechar a transação
            conexao.commit()
            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'