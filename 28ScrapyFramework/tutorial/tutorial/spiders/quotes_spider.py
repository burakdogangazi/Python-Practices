from typing import NewType
import scrapy
from protego import Protego
# https://docs.scrapy.org/en/latest/intro/tutorial.html
class QuotesSpider(scrapy.Spider):
    name = "quotes" # bu isme göre commandlineden işlem yapıcaz
    #aynı isimli spider olamaz
    
    quote_count = 1 # link takibi
    
    file =  open("quotes1.txt","a",encoding="utf-8")

    start_urls = [ # ismi bu olmak zorunda
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/' link takibi için kapattık
    ]

    #default
    """def start_requests(self): 
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            #bellekte saklamıyoruz sadece üretiyoruz 
            #ilk urlye gidiyor sonra parse çalıştırıyor sonra ikinci"""

    def parse(self, response):
        
        #Default
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')


        #Tek Veri Çekerken
        # quote = response.css("div.quote")[0]
        # title = quote.css("span.text::text").extract_first()
        # author = quote.css("div.tags a.tag::text").extract_first()
        # tags = quote.css("div.tags a.tag::text").extract()


        #Tek Veri çekerken
        #     yield {
        #     "title" : title,
        #     "author" : author,
        #     "tags" : tags#json dosyasysına yazar.
        #     # text
        #     # (base) C:\Users\Burak\source\repos\Python\28ScrapyFramework\tutorial>scrapy crawl quotes -o quotes.json
        # }


        #Çoklu veri alımı
        # with open("quotes.txt","w",encoding="utf-8") as file:
        #     for quote in response.css("div.quote"):
        #         title = quote.css("span.text::text").extract_first()
        #         author = quote.css("div.tags a.tag::text").extract_first()
        #         tags = quote.css("div.tags a.tag::text").extract()
        #         file.write("*******************************************\n")
        #         file.write("Alıntı : " +title +"\n")
        #         file.write("Alıntı sahibi :" + author + "\n")
        #         file.write("Etiketler :" + str(tags) + "\n")
        #         #scrapy crawl quotes
        #         file.write("*******************************************\n")

            #Çoklu veri alımı json dosyası oluşturmak
            # yield {
            # "title" : title,
            # "author" : author,
            # "tags" : tags#json dosyasysına yazar. yield
            # # text
            # # (base) C:\Users\Burak\source\repos\Python\28ScrapyFramework\tutorial>scrapy crawl quotes -o quotes.json
            # }   


       
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").extract_first()
            author = quote.css("div.tags a.tag::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            self.file.write(str(self.quote_count) +"*******************************************\n")
            self.file.write("Alıntı : " +title +"\n")
            self.file.write("Alıntı sahibi :" + author + "\n")
            self.file.write("Etiketler :" + str(tags) + "\n")
            #scrapy crawl quotes
            self.file.write("*******************************************\n")
            self.quote_count +=1

#response.css("li.next a::attr(href)").extract_first() link takibi

        next_url = response.css("li.next a::attr(href)").extract_first()
  
        if next_url is not None:
            next_url =  "http://quotes.toscrape.com"+ next_url
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.file.close()
# In [2]: response
# Out[2]: <200 http://quotes.toscrape.com/page/1/>

# In [3]: response.css("title")
# Out[3]: [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]


# In [4]: response.css("title").extract()
# Out[4]: ['<title>Quotes to Scrape</title>']


# In [5]: response.css("title::text").extract()
# Out[5]: ['Quotes to Scrape']

# In [6]: response.css("title::text").extract()[0]
# Out[6]: 'Quotes to Scrape'


# In [9]: response.css("title::text").extract_first()
# Out[9]: 'Quotes to Scrape'


# In [11]: response.xpath('//title')
# Out[11]: [<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]

# In [12]: response.xpath('//title').extract_first()
# Out[12]: '<title>Quotes to Scrape</title>'

# In [14]: response.xpath('//title/text()').extract_first()
# Out[14]: 'Quotes to Scrape'


# In [16]: content = response.css("div.quote")

# In [17]: content


# In [18]: quote = response.css("div.quote")[0]

# In [19]: quote
# Out[19]: <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>



# In [23]: title = quote.css("span.text::text").extract_first()

# In [24]: title
# Out[24]: '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'


# In [25]: author = quote.css("small.author::text").extract_first()

# In [26]: author
# Out[26]: 'Albert Einstein'


# In [28]: tags = quote.css("div.tags a.tag::text").extract()

# In [29]: tags
# Out[29]: ['change', 'deep-thoughts', 'thinking', 'world']