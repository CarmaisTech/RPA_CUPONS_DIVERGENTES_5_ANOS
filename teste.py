import pandas as pd
from src.Model.Utilitarios import dict_cgf
from src.Model.tokenJson import *
# ler_planilha =  pd.read_excel(r'C:\RPA\arquivos\Divergencias_CGF_63002361_(1).xlsx')
# # ler_planilha = ler_planilha.sort_values(by="MÊS ANO REFERÊNCIA")
# print(ler_planilha["Status"])
# ler_planilha = ler_planilha.fillna("")
# for index in range(len(ler_planilha.index)):

#     if ler_planilha["Status"][index] == "":
#         print(index)
#         print(ler_planilha["MÊS ANO REFERÊNCIA"][index])
#         ler_planilha["Status"][index] = "feito"
#     else:
#         print("merda")

# ler_planilha.to_excel(r'C:\RPA\arquivos\Divergencias_CGF_63002361_(1).xlsx', index=False)

# # print(dict_cgf["63002361"])
# # data_pesquisa = [
# #         {"inicio" : "ola", 'fim' : "oi"},
# #         {"inicio" : "tese", 'fim' : "conde"}
# #     ]
# # for x in data_pesquisa:
# #     print(x["inicio"])

# # texto = "8/2025"

# # mes, ano = texto.split("/")
# # print(mes)

# def teste():
#     return ["ola", "conde"]

# g1, g2 = teste()
# print(g1)
# dados = getJson()

# ler_json = pd.DataFrame(dados)
# print(ler_json)
# import calendar
# import datetime
# ano = 2025 
# mes = 6
# ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
# data_pesquisa = []
# dia_inicio = 1
# while dia_inicio <= ultimo_dia:
#     dia_fim = min(dia_inicio + 4, ultimo_dia)
#     inicio = datetime.date(ano, mes, dia_inicio)
#     fim = datetime.date(ano, mes, dia_fim)
    
#     data_pesquisa.append({
#         "inicio": inicio.strftime("%d/%m/%Y"),
#         "fim": fim.strftime("%d/%m/%Y")
#     })
    
#     dia_inicio += 5
# print(data_pesquisa)
df = pd.DataFrame(getJson())
df.to_excel("cupons_divergentes_5anos.xlsx", index=False)