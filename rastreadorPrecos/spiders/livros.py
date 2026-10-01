import scrapy
i = 1

class LivrosSpider(scrapy.Spider):
    name = "livros"
    allowed_domains = ["books.toscrape.com"]

    for i in range(1, 51):
        if i == 1:
            start_urls = ["https://books.toscrape.com/"]
        else:
            start_urls.append(f"https://books.toscrape.com/catalogue/page-{i}.html")

    def parse(self, response):
        bloco_de_livros = response.css('article.product_pod')

        for livro in bloco_de_livros:
            titulo = livro.css('h3 a::attr(title)').get()
            preco = livro.css('p.price_color::text').get()
            yield {
                'nome_do_livro': titulo,
                'valor': preco
            }