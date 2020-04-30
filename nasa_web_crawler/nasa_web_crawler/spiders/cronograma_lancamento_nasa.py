# -*- coding: utf-8 -*-
import scrapy


class CronogramaLancamentoNasaSpider(scrapy.Spider):

    name = 'cronograma_lancamento_nasa'
    
    start_urls = ['http://www.nasa.gov/launchschedule/']

    def parse(self, response):
        pagina = response.url.split("/")[-2]
        nome_arquivo = 'lançamento-%s.html' % pagina
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)
        
        
        # for evento_lancamento in response.css('div.launch-event'):
        #    url_imagem: evento_lancamento.css('div.launch-image a::href').get()
        #    print(dict=url_imagem)
            
           