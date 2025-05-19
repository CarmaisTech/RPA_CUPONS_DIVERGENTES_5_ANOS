import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import date
import logging
import os
def EmailImage(empresa, qtd_imgs):
    print("ENVIANDO EMAIL COM MENSAGEM DE AVISO")
    logging.info("ENVIANDO EMAIL COM MENSAGEM DE AVISO")

    with open('C:\\RPA\\credenciais\\credenciais_gmail.txt','r') as file:
        chaves = file.readlines()


    sender = chaves[0][:-1]
    password = chaves[1]
    print(sender)
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    receiver = ("alexsander@carmais.com.br,alan.estevao@carmais.com.br")
    # receiver = ("francisco.clecio@carmais.com.br")


    conteiner = MIMEMultipart("related")
    conteiner["From"] = sender
    conteiner["To"] = receiver
    conteiner["Subject"] = f"RPA - DIVERGENCIAS CUPONS FISCAIS MENSAGEM DE AVISO  {data_em_texto}"

    mgsAlternativa = MIMEMultipart("alternative")
    conteiner.attach(mgsAlternativa)

    mgsText = MIMEText("RPA - DIVERGENCIAS CUPONS FISCAIS AVISO MENSAGEM DE AVISO ")
    mgsAlternativa.attach(mgsText)
    imgs = ""

    for x in range(qtd_imgs):
        imgs = imgs + f"<img src=cid:{x+1}><br>" 

    mgsText = MIMEText(f"<b><h1>Mensagem de Aviso</h1> <h2>{empresa}</h2></b><br>{imgs}", "html")
    mgsAlternativa.attach(mgsText)

    for b in range(qtd_imgs):
        fp = open(f"C:\\RPA\\RPA_DIVERGENCIAS_CUPONS_FISCAIS\\mensagem_aviso_{empresa}{b+1}.png", "rb")
        mgsImage = MIMEImage(fp.read())
        fp.close()

        mgsImage.add_header('Content-ID', f"<{b+1}>")
        conteiner.attach(mgsImage)

    try: 
        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls()
        session.login(sender, password)
    except Exception as error:
        print(f"Erro ao tentar conectar gmail {error}")
        logging.info(f"Erro ao tentar conectar gmail {error}")



    text = conteiner.as_string()
    try: 
        session.sendmail(sender, receiver.split(","), text)
        print("EMAIL ENVIADO COM SUCESSO!!")
        logging.info("EMAIL ENVIADO COM SUCESSO!!")
    except Exception as erro: 
        print(f"Erro ao enviar email {erro}")

if __name__ == "__main__":
    EmailImage("NISSAN FILIAL")
