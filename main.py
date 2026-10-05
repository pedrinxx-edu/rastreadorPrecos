from difflib import get_close_matches
from funcoes import procurar_preco, procurar_titulo, exportar_catalogo_excel, exportar_catalogo_word

usarSistema = "sim"
opcoes_validas = [
   "1", "um", "preço", "preco", "precos", "preços",
   "2", "dois", "titulo", "titulos", "título", "títulos",
   "3", "tres", "três", "exportar", "exportação", "exportacâo", "exportaçao", "catalogo", "catálogo", "catalogos", "catálogos",
   "4", "quatro", "encerrar", "sair", "fechar", "exit", "finalizar", "terminar"
]

nome = input("\nOlá, qual o seu nome? ")

while usarSistema == "sim":
    print(f"\nOlá {nome}! Esse é um sistema de consulta do site Books to Scrape")
    print("\n1 - Filtrar por preço \n2 - Procurar titulos \n3 - Exportar Catálogo \n4 - Encerrar")
    opcao = input("\nQual das opções acima você deseja executar? ").strip() .lower()

    if opcao not in opcoes_validas:
            parecido = get_close_matches(opcao, opcoes_validas, n=1, cutoff=0.6)
            if parecido:
                resposta = input(f"Você quis dizer {parecido[0]}? ")
                if resposta in ("sim", "s", "ss"):
                    opcao = parecido[0]

    if opcao in ("1", "um", "preço", "preco", "precos", "preços"):
        procurar_preco()
    elif opcao in ("2", "dois", "titulo", "titulos", "título", "títulos"):
        procurar_titulo()
    elif opcao in ("3", "tres", "três", "exportar", "exportação", "exportacâo", "exportaçao", "catalogo", "catálogo", "catalogos", "catálogos"):
        escolher_formato_exportacao_excel = input("Deseja exportar o catálogo em formato Excel? (sim/não) ").strip() .lower()
        if escolher_formato_exportacao_excel in ("sim", "s"):
            exportar_catalogo_excel()
        else:
            escolher_formato_exportacao_word = input("Existe uma opção de exportar em formato word, quer tentar? ").strip() .lower()
            if escolher_formato_exportacao_word in ("sim", "s"):
                exportar_catalogo_word()
            else:
                print("Ok, não existe outra opção de exportação, tente novamente mais tarde!")

    elif opcao in ("4", "quatro", "encerrar", "sair", "fechar", "exit", "finalizar", "terminar"):
        print(f"Até logo {nome}! Obrigado por usar nosso sistema!")
        exit()
    else:
        print("Opção Indisponível! Tente novamente ou encerre o sistema")