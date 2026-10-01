import csv

def procurar_preco():
    repeticao = "sim"
    while repeticao == "sim":
        precoMin = float(input("Qual o preço mínimo para filtrar? "))
        precoMax = float(input("Qual o preço máximo para filtrar? "))

        if precoMin < precoMax:
            with open ('catalogoCompleto.csv', mode='r', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    preco_sem_simbolo = linha['valor'].replace('£', '')
                    precoLimpo = float(preco_sem_simbolo)

                    if precoMin <= precoLimpo <= precoMax:
                        print(f"| {linha['nome_do_livro']} | {linha['valor']} |")
            repeticao = "não"
        else:
            print("Erro: O valor máximo tem que ser maior que o valor mínimo!")
            repeticao = "sim"
