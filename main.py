import csv

usarSistema = "sim"
get_close_matches = []
opcoes_validas = [
   "1", "um", "preço", "preco", "precos", "preços",
   "2", "dois", "titulo", "titulos", "título", "títulos",
   "3", "tres", "três", "exportar", "exportação", "exportacâo", "exportaçao", "catalogo", "catálogo", "catalogos", "catálogos"
]

nome = input("\nOlá, qual o seu nome? ")

while usarSistema == "sim":
    print(f"\nOlá {nome}! Esse é um sistema de consulta do site Books to Scrape")
    print("\n1 - Procurar preço \n2 - Procurar titulos \n3 - Exportar Catálogo \n4 - Encerrar")
    opcao = input("Qual das opções acima você deseja executar? ").strip() .lower()

    if opcao not in opcoes_validas:
            parecido = get_close_matches(opcao, opcoes_validas, n=1, cutoff=0.6)
            if parecido:
                resposta = input(f"Você quis dizer {parecido[0]}? ")
                if resposta in ("sim", "s", "ss"):
                    opcao = parecido[0]
    