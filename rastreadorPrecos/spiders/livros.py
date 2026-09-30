import scrapy


class LivrosSpider(scrapy.Spider):
    name = "livros"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        blocos_de_livros = response.css('article.product_pod')

        for livro in blocos_de_livros:
            titulo = livro.css('a::attr(title)').get()
            preco = livro.css('p.price_color::text').get()
            yield {
                'nome_do_livro': titulo,
                'valor': preco
            }