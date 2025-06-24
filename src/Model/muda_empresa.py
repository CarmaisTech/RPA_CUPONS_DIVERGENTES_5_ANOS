from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.Model.Utilitarios import dict_cgf,empresas_ignoradas
from src.Model.click_api import click2 as c
import threading
import time
import logging 
import pyautogui as p

def manage_os_popup():
    time.sleep(2)
    c(797, 353)
def muda_empresa(navegador, empresa):
    print("TROCANDO DE EMPRESA" + empresa)
    logging.info("TROCANDO DE EMPRESA" + empresa)
    handle  = ""

    if navegador.title == "Erro de privacidade":

        navegador.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/h1")
        p.sleep(1)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/button[3]").click()
        try:
                WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/p[2]/a"))) #ELEMENTO DE ESPERA INPUT

        except:
                p.alert("n deu bom")
                navegador.find_element(By.XPATH, "/html/body/div/div[3]/p[2]/a").click()
    qtde_empresas = len(navegador.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr'))

    for i in range(1, qtde_empresas+1):

    # Ignorando cabeçalho da tabela de empresas
        if i != 1:

            # Capturando CGF
            cgf_empresa = navegador.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[{i}]/td[1]/a').text

            nome_empresa = dict_cgf[cgf_empresa]
            
            # Filtrando só pelas empresas ativas
            if nome_empresa not in empresas_ignoradas:
    
                # Selecionando certificado digital, apenas na primeira empresa acessada

                if empresa == nome_empresa: # TODO Mudar para enumerate
                        print(f'Acessando da empresa {empresa}\n')
                        logging.info(f'Acessando da empresa {empresa}')
           

                        my_thread = threading.Thread(target = manage_os_popup)
                        my_thread.start()

                        # Clicando na empresa 
                        navegador.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[{i}]/td[1]/a').click()
                        p.sleep(2)
                        print(navegador.title)
                        handle = navegador.window_handles
                        break
    if handle != "":
        return handle
    else:
       
        return "",""



