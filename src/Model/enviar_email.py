import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from src.Model.estilo import estilo
from src.Model.tokenJson import *
import logging
import pandas as pd
import os

def Enviar_Email():
    
    with open('C:\\RPA\\credenciais\\credenciais_gmail.txt','r') as file:
        chaves = file.readlines()

    empresas = GetBancoEmpresa()
    sender = chaves[0][:-1]
    password = chaves[1]
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    # receiver = ("alexsander@carmais.com.br, alan.estevao@carmais.com.br")
    # receiver = ("alexsander@carmais.com.br, daniel@carmais.com.br, alan.estevao@carmais.com.br")
    receiver = ("francisco.clecio@carmais.com.br")

    conteiner = MIMEMultipart("related")
    conteiner["From"] = sender
    conteiner["To"] = receiver
    conteiner["Subject"] = f"RPA - DIVERGÊNCIAS DE CUPONS FISCAIS - {data_em_texto}"
    mgsAlternativa = MIMEMultipart("alternative")
    conteiner.attach(mgsAlternativa)

    mgsText = MIMEText("RPA - DIVERGÊNCIAS CUPONS FISCAIS")
    mgsAlternativa.attach(mgsText)
    
    corpo = ""

    for empresa in empresas:
        df = pd.read_excel(f"C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS\\informacoes_{empresa}.xlsx")
        tabela = df.to_html(index=False)
        corpo = corpo + f"<h3>{empresa}</h3>{estilo(tabela)}"


    mgsTabela = MIMEText(corpo, "html")
    mgsAlternativa.attach(mgsTabela)
    try:
        servidor =  smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(sender,password)
    except Exception as erro:
        print("ERRO AO TENTA ESTABELECER CONEXAO SMTP " + erro)
        logging.info("ERRO AO TENTA ESTABELECER CONEXAO SMTP " + erro)

    text = conteiner.as_string()
    print('enviando email\naguarde....... ')
    logging.info('enviando email\naguarde....... ')

    servidor.sendmail(sender, receiver.split(","), text)
    print('email enviado com sucesso')
    logging.info('email enviado com sucesso')

    


if __name__ == "__main__":
    Enviar_Email("kabum")
