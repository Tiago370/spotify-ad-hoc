
import psycopg2

class Config:

    def __init__(self):
        #self.dadosconexao = dadosconexao
        self.setParametros()

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='spotify' user='postgres' password='postgres'"
        
    def alteraBD(self, stringSQL, valores):
        #print(stringSQL)
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            self.setParametros()
            conexao=psycopg2.connect(self.dadosconexao)

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
            print(psycopg2.Error)
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'

    def consultaBD(self, stringSQL, valores):
        # iniciar a conexo vazia
        conn = None
        try:
            # abrir a conexão
            conexao=psycopg2.connect(self.dadosconexao)
            # abrir a sessão transação começa aqui
            sessao = conexao.cursor()
            # Executor o comando em memoria RAM
            sessao.execute(stringSQL, valores)
            registros = sessao.fetchall()
            colnames = [desc[0] for desc in sessao.description]
            # Encerror a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return (colnames, registros)

