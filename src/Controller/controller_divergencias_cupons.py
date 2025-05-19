import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as p
from selenium.webdriver.common.by import By
from src.Model.muda_empresa import muda_empresa
from src.Model.Login import Login
from src.Model.Utilitarios import dict_cgf
from src.Model.verificar_aviso import  VerifarAviso
from src.Model.Consultar import webscraping
from src.Model.tokenJson import *
from src.Model.DDL import Inserir_Dados
from src.Model.enviar_email import Enviar_Email
from src.Model.EnviaImagens import EmailImage
import traceback
import pandas as pd

with open(f"C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS\\rpa_divergencias_cupons_fiscais.txt", "w"):
    pass


logging.basicConfig(level=logging.INFO, filename=f"C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS\\rpa_divergencias_cupons_fiscais.txt", format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', datefmt='%d/%m/%Y')
print("INCIANDO BOT RPA DIVERGENCIAS CUPONS FISCAIS")
logging.info("INCIANDO BOT RPA DIVERGENCIAS CUPONS FISCAIS")

with open ("C:\\RPA\\Credenciais\\ambiente_seguro_sefaz.txt", "r") as file:
    chaves =  file.readlines()
login = chaves[0][:-1]
senha = chaves[1]

chrome_optins = Options()
chrome_optins.add_argument(f"--user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\Profile teste")
# chrome_optins.add_argument("--profile-directory=Default")  # Use "Default" ou o nome do perfil

navegador = webdriver.Chrome(chrome_optins)
navegador.get("https://servicos.sefaz.ce.gov.br/internet/acessoseguro/servicosenha/logarusuario/login.asp")
navegador.maximize_window()
Login(navegador)
empresa_processadas = getJson()
ler_planilha = pd.read_excel(r"C:\RPA\arquivos\Divergencias_CGF_63002361_(1).xlsx")
try: 
    for index in range(len(ler_planilha.index)):
            g1, g2 = muda_empresa(navegador,dict_cgf[str(ler_planilha["CGF"][index])])

            if g1:
                navegador.switch_to.window(g2)
                resposta, qtd_imgs = VerifarAviso(navegador, dict_cgf[str(ler_planilha["CGF"][index])])
                if resposta:
                        EmailImage(dict_cgf[str(ler_planilha["CGF"][index])], qtd_imgs)

                flag =  webscraping(navegador,dict_cgf[str(ler_planilha["CGF"][index])],str(ler_planilha["MÊS ANO REFERÊNCIA"][index]))
                if flag:
                    # df = pd.DataFrame(dicionario)
                    # df.to_excel(f"C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS\\informacoes_{dict_cgf[str(ler_planilha["CGF"][index])]}.xlsx", index=False)

                    navegador.close()  
                    navegador.switch_to.window(g1)


                else: #PULA PRA PROXIMO EMPRESA QUANDO EMPRESA ANTERIO ESVIVER VAZIA
                    navegador.close()  
                    navegador.switch_to.window(g1)


            

######################### INICIANDO PROCESSO DE INSERIR DADOS ##################################
   
    # zeraJson()
    print("REMOVENDO ARQUIVOS")
    # logging.info("REMOVENDO ARQUIVOS")
    # for file_path in os.listdir("C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS"):
    #     if file_path.endswith(".png"):
    #         os.remove("C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS" + "\\" + file_path)
    #     if file_path.endswith(".xlsx"):
    #         os.remove("C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS" + "\\" + file_path)
            
    print("ARQUIVOS EXCLUIDOS")
    logging.info("ARQUIVOS EXCLUIDOS")
    
            




    
except Exception as erro:
    p.alert("EITA MENINO, DEU ERRO NESSA")
    print(erro)
    logging.info(erro)
    
    print(traceback.format_exc())    
    logging.info(traceback.format_exc())



    




        
            

    






