from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui as p


def Login(navegador):
        credenciais = open(r"C:\RPA\Credenciais\ambiente_seguro_sefaz.txt", "r")
        chaves = credenciais.readlines()
        usuario = chaves[0][:-1]
        senha = chaves[1]
        if navegador.title == "Erro de privacidade":
        
                navegador.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/h1")
                p.sleep(1)
                navegador.find_element(By.XPATH, "/html/body/div/div[2]/button[3]").click()
                try:
                        WebDriverWait(navegador, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/p[2]/a"))) #ELEMENTO DE ESPERA INPUT
 
                except:
                        p.alert("n deu bom")
                navegador.find_element(By.XPATH, "/html/body/div/div[3]/p[2]/a").click()


        WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[2]/td[1]/input"))) #ELEMENTO DE ESPERA INPUT
        p.sleep(0.5)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(usuario) #INPUT DE USUARIO
        p.sleep(2)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(senha) #INPUT DE SENHA
        p.sleep(2)
        selecionar = navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[3]/td/select") #INPUT DE USUARIO
        Vinculoa = Select(selecionar)
        Vinculoa.select_by_value("3")
        p.sleep(4)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[1]/input").click()
        p.sleep(0.5)
        WebDriverWait(navegador, 10).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/ul[2]/li[11]/a")))
        p.sleep(0.5)    
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/ul[2]/li[11]/a").click() #MFE MODULO FISCAL ELETRONICA
        p.sleep(0.5)
        navegador.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/ul/li/a").click()
        p.sleep(0.5)

        # https://zimbra.centre.com.ng/a