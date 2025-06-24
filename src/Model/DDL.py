from conexao_banco import Conexao_Banco
from tokenJson import getJson
import pandas as pd
import os
import logging
import pyautogui as p
import traceback


def Inserir_Dados(empresa,data_l):
    print(f"INSERIR DADOS NA EMPRESA {empresa}")
    f"INSERIR DADOS NA EMPRESA {empresa}"
    conn, cursor = Conexao_Banco(empresa)
    df = pd.DataFrame(getJson())
    serie = [str(x) for x in df["serie"]]
    data = [str(x[:10]) for x in df["data emissao"]]
    chave = [str(x) for x in df["chaves"]]
    dados = []

    for index in range(len(serie)):
        dados.append((serie[index], data[index], chave[index]))

    sql_insert = "INSERT INTO MS_CtrlXml VALUES (%s, %s, %s)"



    try:
        cursor.executemany(sql_insert, dados)
        conn.commit()

        # print("DADOS INSERIDO COM SUCESSO!!!")
        # logging.info("DADOS INSERIDO COM SUCESSO!!!")

        # print("EXECUTANDO PROCEDURE")
        # logging.info("EXECUTANDO PROCEDURE")
        
        # cursor.execute("UP_Cupons_Divergentes_Xml")
        cursor.execute("SELECT * FROM MS_CtrlXml ")
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
            # df.to_excel(f"C:\\RPA\\RPA_CUPONS_DIVERGENTES_5_ANOS\\divergencias_cupons_banco\\{empresa}_divergencias_cupons_5anos_bancodedaos_{data_l}.xlsx", index=False)
            df.to_excel(f"C:\\RPA\\RPA_CUPONS_DIVERGENTES_5_ANOS\\divergencias_cupons_banco\\PROCEDURE.xlsx", index=False)
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
    flag, dados = Inserir_Dados("NOSSAMOTOMATRIZ","21_05_2025")




    
    