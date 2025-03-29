import os
from PIL import Image
import imagehash

def encontrar_imagens_repetidas(pasta, extensao_especifica=None, hashfunc=imagehash.whash):
    extensoes_imagens = tuple(Image.registered_extensions().keys())

    imagens = {}
    repetidas = []

    for nome_arquivo in os.listdir(pasta):
        if extensao_especifica:
            if not nome_arquivo.lower().endswith(extensao_especifica):
                continue
        elif not nome_arquivo.lower().endswith(extensoes_imagens):
            continue

        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        try:
            img = Image.open(caminho_arquivo)
            hash_img = hashfunc(img)

            if hash_img in imagens:
                repetidas.append((imagens[hash_img], nome_arquivo))
            else:
                imagens[hash_img] = nome_arquivo
        except (OSError, ValueError, IOError):
            print(f"Não foi possível processar: {nome_arquivo}")

    return repetidas

def salvar_repetidas(repetidas, pasta):

    if not repetidas:
        return

    pasta_repetidas = os.path.join(pasta, 'repetidas')
    os.makedirs(pasta_repetidas, exist_ok=True)

    caminho_arquivo_repetidas = os.path.join(pasta_repetidas, 'repetidas.txt')
    with open(caminho_arquivo_repetidas, 'w') as arquivo:
        for original, duplicata in repetidas:
            arquivo.write(f"Original: {original}, Duplicata: {duplicata}\n")

if __name__ == "__main__":
    pasta_imagens = input("Digite o caminho da pasta de imagens: ")
    
    escolha = input("Deseja verificar todos os tipos de imagem suportados (digite 'todos') ou uma extensão específica (ex: .jpg)? \n ").strip().lower()
    extensao_especifica = None if escolha == "todos" else escolha

    repetidas = encontrar_imagens_repetidas(pasta_imagens, extensao_especifica, hashfunc=imagehash.whash)
    salvar_repetidas(repetidas, pasta_imagens)

    if repetidas:
        print("Imagens repetidas encontradas. Verifique a pasta 'repetidas'.")
    else:
        print("Nenhuma imagem repetida encontrada.")