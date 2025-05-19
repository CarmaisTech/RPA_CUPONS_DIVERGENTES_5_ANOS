import pandas as pd
from src.Model.Utilitarios import dict_cgf

# ler_planilha =  pd.read_excel(r'C:\RPA\arquivos\Divergencias_CGF_63002361_(1).xlsx')
# for index in range(len(ler_planilha.index)):
#     print(dict_cgf[str(ler_planilha["CGF"][index])])

# print(dict_cgf["63002361"])
# data_pesquisa = [
#         {"inicio" : "ola", 'fim' : "oi"},
#         {"inicio" : "tese", 'fim' : "conde"}
#     ]
# for x in data_pesquisa:
#     print(x["inicio"])

texto = "8/2025"

mes, ano = texto.split("/")
print(mes)