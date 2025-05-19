from src.Model.conexao_banco import Conexao_Banco
import pandas as pd
import os
import logging
import pyautogui as p
import traceback


def Inserir_Dados(empresa):
    print(f"INSERIR DADOS NA EMPRESA {empresa}")
    f"INSERIR DADOS NA EMPRESA {empresa}"
    conn, cursor = Conexao_Banco(empresa)
    df = pd.read_excel(f"{os.getcwd()}//informacoes_{empresa}.xlsx")
    serie = [str(x) for x in df["Serie"]]
    data = [str(x[:10]) for x in df["data"]]
    chave = [str(x) for x in df["chave_cfo"]]
    dados = []

    for index in range(len(serie)):
        dados.append((serie[index], data[index], chave[index]))

    sql_insert = "INSERT INTO MS_CtrlXml VALUES (%s, %s, %s)"



    try:
        cursor.execute("TRUNCATE TABLE MS_CtrlXml")
        cursor.executemany(sql_insert, dados)
        conn.commit()

        print("DADOS INSERIDO COM SUCESSO!!!")
        logging.info("DADOS INSERIDO COM SUCESSO!!!")

        print("EXECUTANDO PROCEDURE")
        logging.info("EXECUTANDO PROCEDURE")
        
        cursor.execute("UP_Cupons_Divergentes_Xml")  
        resposta = cursor.fetchall()
        if len(resposta) > 0:


            serie = []
            data =  []
            chave = []

            for dado in resposta:
                serie.append(dado[0])
                data.append(dado[1])
                chave.append(dado[2])
            

            Dicionario = {
                "Serie" : serie,
                "Data" : data,
                "Chave" : chave
            }


            df = pd.DataFrame(Dicionario)
            df.to_excel(f"{os.getcwd()}//informacoes_{empresa}.xlsx", index=False)
            serie = []
            data =  []
            chave = []


            return True
        else:
            return False

    except:
        print(f"ERRO AO TENTA INSERIR INFORMACAO")
        logging.info(f"ERRO AO TENTA INSERIR INFORMACAO")
        print(traceback.format_exc())
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    flag, dados = Inserir_Dados("NISSAN MATRIZ")




    
    