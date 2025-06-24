import pyautogui
import logging
import pymssql
from Utilitarios import dict_empresas_banco
import traceback
def Conexao_Banco(empresa):
    print("CONECTANDO  BANCO DA DADOS")
    logging.info("CONECTANDO  BANCO DA DADOS")
    credenciais = open('C:/RPA/Credenciais/credenciais_ssms.txt', 'r')
    chaves = credenciais.readlines()
    credenciais.close()
    BD_HOST = chaves[0].strip()
    BD_USER = chaves[1].strip()
    BD_PASSWORD = chaves[2].strip()
    try:
        conn = pymssql.connect(BD_HOST, BD_USER, BD_PASSWORD, dict_empresas_banco[empresa])
        cursor = conn.cursor()
        print("Conexão realizada com sucesso.")
        logging.info("Conexão realizada com sucesso.")
        return conn, cursor
    except Exception as erro:
        print(f"ERRO AO TENTAR SE CONECTAR AO BANCO DE DADOS: {erro}")
        logging.info(f"ERRO AO TENTAR SE CONECTAR AO BANCO DE DADOS: {erro}")
        print(traceback.format_exc())
        exit()

if __name__ == "__main__":
    print("banco de dados")

    

