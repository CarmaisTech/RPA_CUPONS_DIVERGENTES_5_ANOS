import json
import os



def getJson():
    with open(f"C:/RPA/RPA_CUPONS_DIVERGENTES_5_ANOS/json_dados.json", "r") as file:
        ler = json.load(file)
        return ler["DADOS"]

    

def setJson(empresa):
    with open(f"C:/RPA/RPA_CUPONS_DIVERGENTES_5_ANOS/json_dados.json", "r") as file:
        dados = json.load(file)
        
    with open(f"C:/RPA/RPA_CUPONS_DIVERGENTES_5_ANOS/json_dados.json", "w") as file:
        dados["DADOS"].append(empresa)
        json.dump(dados, file, indent=4)


def zeraJson():
    with open(f"C:/RPA/RPA_CUPONS_DIVERGENTES_5_ANOS/json_dados.json", "r") as file:
        dados = json.load(file)
        
    with open(f"C:/RPA/RPA_CUPONS_DIVERGENTES_5_ANOS/json_dados.json", "w") as file:
        dados["DADOS"] = []
        json.dump(dados, file, indent=4)





        
