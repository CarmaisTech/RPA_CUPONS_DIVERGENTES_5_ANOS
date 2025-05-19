from conexao_banco import Conexao_Banco
from Utilitarios import empresas

def ExclusaoDados(empresa):
    print("EXCLUINDO DADOS DA EMPRESA")
    try:
        conn, curso = Conexao_Banco(empresa)
        curso.execute("SELECT * FROM MS_CtrlXml")
        dados = curso.fetchall()
        print(f"TABELA {empresa}--\n{dados}")

        curso.execute("TRUNCATE TABLE MS_CtrlXml")
        conn.commit()

        curso.execute("SELECT * FROM MS_CtrlXml")
        dados = curso.fetchall()
        print(f"{dados}")
        print("DADOS EXCLUIDOS COM SUCESSO!!!")
    except Exception as erro:
        print("DEU RUIM NESSA M....")
        print(erro)

if __name__ == "__main__":
    for empresa in empresas:
        ExclusaoDados(empresa)