import scrapy


class LivrosSpider(scrapy.Spider):
    name = "livros"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"]

    def parse(self, response):
        titulo = response.css('h1::text').get()
        preco = response.css('p.price_color::text').get()
        yield {
            'nome_do_livro': titulo,
            'valor': preco
        }