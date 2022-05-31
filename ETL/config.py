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

