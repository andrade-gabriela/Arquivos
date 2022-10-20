from cgitb import text
import os
import requests
import matplotlib.pyplot as plt
from collections import Counter

# main
# verifica se existe 
# fazer upload 
# fazer a frequencia 
# construir grafico

def main():
    # bloco - Arquivos
    def verificar_existe(nome_arquivo, link):
        if os.path.exists(nome_arquivo):
            print("Arquivo já existe, e não será baixado.")
        else:
            print("Arquivo não existe, baixando...")
            fazer_upload(nome_arquivo, link)

    def fazer_upload(nome_arquivo, link):
        resposta = requests.get(link, stream=True)
        with open(nome_arquivo, 'wb') as novo_arquivo:
                for linha in resposta.iter_content(chunk_size=256):
                    novo_arquivo.write(linha)

    def calcular_frequencia(nome_arquivo):
        with open(nome_arquivo, encoding='ISO 8859-1') as arquivo:
            texto = arquivo.read().lower()
        letras = [item for item in texto if item.isalpha()]
        frequencia = Counter(letras)
        print(frequencia)
        return frequencia

    # def limpar_string(texto):
    #     texto_limpo = ''
    #     for c in texto:
    #         if c.isalpha() or c == ' ':
    #             texto_limpo += c
    #     return texto_limpo

    # bloco - Iniciar
    def iniciar():

        nome_arquivo = 'domcasmurro.txt'
        link = "https://www.gutenberg.org/files/55752/55752-8.txt"
        verificar_existe(nome_arquivo, link)
        calcular_frequencia(nome_arquivo)

    iniciar()

if __name__ == '__main__':
    main()


