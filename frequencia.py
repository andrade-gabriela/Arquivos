from cgitb import text
import os
import requests
import matplotlib.pyplot as mat
from collections import Counter

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
        return frequencia

    # def limpar_string(texto):
    #     texto_limpo = ''
    #     for c in texto:
    #         if c.isalpha() or c == ' ':
    #             texto_limpo += c
    #     return texto_limpo
    def gerar_grafico_letras(frequencia_letras):
        rotulos, valores = zip(*frequencia_letras.most_common(15))
        mat.title('Frequência de letras em português')
        mat.pie(valores, labels=rotulos, autopct='%1.0f%%', startangle=90)

    # bloco - Iniciar
    def iniciar():
        nome_arquivo = 'domcasmurro.txt'
        link = "https://www.gutenberg.org/files/55752/55752-8.txt"
        verificar_existe(nome_arquivo, link)
        frequencia_letras = calcular_frequencia(nome_arquivo)
        gerar_grafico_letras(frequencia_letras)

    iniciar()

if __name__ == '__main__':
    main()


