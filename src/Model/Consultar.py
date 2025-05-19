from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import timedelta, date
import datetime
from selenium.webdriver.common.keys import Keys as k
from src.Model.tokenJson import setJson
import pyautogui as p
import logging
import calendar


def webscraping(navegador, empresa, data):
    print(f"PESQUISANDO CF-E {empresa}")
    logging.info(f"PESQUISANDO CF-E {empresa}")
    data_atual = date.today()
    semena = date.weekday(date.today())
    mes, ano = data.split("/")

    # Primeira metade do mês
    inicio_parte1 = datetime.date(int(ano), int(mes), 1)
    fim_parte1 = datetime.date(int(ano), int(mes), 15)

    # Segunda metade do mês
    inicio_parte2 = datetime.date(int(ano), int(mes), 16)
    ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
    fim_parte2 = datetime.date(int(ano), int(mes), ultimo_dia)


    data_pesquisa = [
        {"inicio" : inicio_parte1.strftime("%d/%m/%Y"), 'fim' : fim_parte1.strftime("%d/%m/%Y")},
        {"inicio" : inicio_parte2.strftime("%d/%m/%Y"), 'fim' : fim_parte2.strftime("%d/%m/%Y")}
    ]
    #ESPERA DO LINK CONSULTA F-E APARECER NA TELA
    WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div/ul/li[4]/a")))
    #CLICANDO NO LINK DE CONSULTA F-E
    navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/ul/li[4]/a").click()
    p.sleep(1.5)
    #ESPERA NOME Consulta a Cupons Fiscais FICAR VISIVEL NA TELA
    WebDriverWait(navegador, 20).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div/div/h3")))
    for x in data_pesquisa:
        dt_inicial = x["inicio"]
        dt_final = x["fim"]
        p.sleep(1.5)
        #CAMPO DA DATA INICIAL 
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div[1]/div/div/div[1]/div/input").clear()
        p.sleep(1.5)
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div[1]/div/div/div[1]/div/input").send_keys(dt_inicial, k.RETURN)
        p.sleep(1.5)
        #CAMPO DA DATA FINAL
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div/div[1]/div/input").clear()
        p.sleep(1.5)
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div/div[1]/div/input").send_keys(dt_final, k.RETURN)
        p.sleep(1.5)
        #BTN CONSULTAR
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/form/div[6]/div/div/button[1]").click()
        #ESPERANDO CARREGAR INFORMAÇOES
        WebDriverWait(navegador, 25).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/h4")))
        p.sleep(1)
        try:
            WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[1]")))
            print("NOTAS NAO ENCONTRADAS --")
            logging.info("NOTAS NAO ENCONTRADAS --")
            
            continue
        
        except:
            pass
        #CLICANDO EM 100 OPÇOES
        try: 
            WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/button[4]")))
        except:
            pass

        p.sleep(1)
        navegador.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/button[4]").click()
        p.sleep(2)
        lista_items = navegador.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/ul/li")

        if len(lista_items) > 0:
            for x in range(1,len(lista_items)):
                if x != 1 :
                    p.sleep(6)
            
                    tbody_listas = navegador.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/table/tbody/tr")
                    for item in tbody_listas:
                        print(item.text)
                        Serie_mfe = item.find_element(By.XPATH, ".//td[@data-title-text='Série MFE']").text
                        Data_emissao = item.find_element(By.XPATH, ".//td[@data-title-text='Data emissão']").text
                        Chave_cfo = item.find_element(By.XPATH, ".//td[@data-title-text='Chave CFe']").text
                        setJson({"serie" : Serie_mfe, "data emissao" : Data_emissao, "chaves" : Chave_cfo})
        
                
                    if x != (len(lista_items) - 1):
                        navegador.find_element(By.XPATH, f"/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/ul/li[{x+1}]/a/span").click()
    
        else:
            tbody_listas = navegador.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div[2]/table/tbody/tr")
            for item in tbody_listas:
                Serie_mfe = item.find_element(By.XPATH, ".//td[@data-title-text='Série MFE']").text
                Data_emissao = item.find_element(By.XPATH, ".//td[@data-title-text='Data emissão']").text
                Chave_cfo = item.find_element(By.XPATH, ".//td[@data-title-text='Chave CFe']").text
                print(item.text)
                setJson({"serie" : Serie_mfe, "data emissao" : Data_emissao, "chaves" : Chave_cfo})

    return True