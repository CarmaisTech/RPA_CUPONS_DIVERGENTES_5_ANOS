from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
import os
import logging
import pyautogui as p

def VerifarAviso(navegador,empresa):
    print("VERIFICANDO SE CONTEM MENSAGEM DE AVISO")
    logging.info("VERIFICANDO SE CONTEM MENSAGEM DE AVISO")
    try:
        if navegador.title == "Erro de privacidade":
        
                navegador.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/h1")
                p.sleep(1)
                navegador.find_element(By.XPATH, "/html/body/div/div[2]/button[3]").click()
                try:
                        WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/p[2]/a"))) #ELEMENTO DE ESPERA INPUT
 
                except:
                        p.alert("n deu bom")
                navegador.find_element(By.XPATH, "/html/body/div/div[3]/p[2]/a").click()
                
        WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[1]/h4")))

        listas = navegador.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr")
        print(len(listas))
        
        if len(listas) > 0 and len(listas) <= 1  :            
            listas[0].click()
            p.sleep(2)
            mensagemAviso =  navegador.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/div/div/div[2]")
            mensagemAviso.screenshot(f"{os.getcwd()}\\mensagem_aviso_{empresa}{len(listas)}.png")
            p.sleep(3)
            WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/div/div/div[3]/button")))
            
            navegador.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/div/div/div[3]/button").click() #BTN DE FECHAR MODAL AVISO
        
        elif len(listas) > 1:
            for x in range(len(listas)):
                navegador.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]").click()
                mensagemAviso =  navegador.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/div/div/div[2]")
                mensagemAviso.screenshot(f"{os.getcwd()}\\mensagem_aviso_{empresa}{x+1}.png")
                navegador.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/div/div/div[3]/button").click() #BTN DE CIENTE DO MODAL DE AVISA
                p.alert("ola")
        
            
        
        
        print("MENSAGEM DE AVISO PRESENTE!!!!")
        logging.info("MENSAGEM DE AVISO PRESENTE!!!!")
        return True, len(listas)
    except exceptions.TimeoutException:
        return False , ""
        