""" from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent
FILE_DIR = Path(BASE_DIR, "back/")

arquivos = [i for i in Path(FILE_DIR).glob("*.html")]

for arquivo in arquivos:
    arquivo_path = arquivo
    arquivo_nome = arquivo_path.stem
    arquivo_extensao = arquivo_path.suffix

    with open(arquivo_path, "r") as file:
        texto = file.readlines()

    # Define o padrão a ser procurado
    padrao = r"assets/[a-z]+/[a-z-0-9]+\...."
    novo_texto = list()

    for linha_atual in texto:
        achou = re.search(padrao, linha_atual)
        if achou:
            # Extrai o texto encontrado de acordo com o
            #   padrão do regex e transforma no parâmetro
            #   filename que será usado na url_for
            filename = achou.group()
            urlfor = "{{ " + f"url_for('site.static',filename='{filename}')" + " }}"
            nova_linha = linha_atual.replace(filename, urlfor)
            nova_linha = nova_linha.replace("./", "")
            nova_linha = nova_linha.replace("assets/", "")
            novo_texto.append(nova_linha)
        else:
            novo_texto.append(linha_atual)

    novo_arquivo_path = Path(BASE_DIR, f"{arquivo_nome}{arquivo_extensao}")
    with open(novo_arquivo_path, "w") as file:
        file.writelines(novo_texto)
 """