import scrapy 
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
#calling the module contanining available URL's and domains.
from ..url import url_list, domain_list
from ..items import HtmlscraperItem

class ArticleSpider(scrapy.Spider):
    name = 'articlespider'
    allowed_domains = domain_list
    start_urls = url_list
    max_page = max_depth_count = 5
    

    def __init__(self, max_pages = 5, max_depth = 5, **kwargs):
        super().__init__(**kwargs)
        self.max_page = int(max_pages)  # Convert to int
        self.max_depth_count = int(max_depth)  # Convert to int


    def parse(self,response):
        domain = urlparse(response.url).netloc
        print(f"Processing domain: {domain}")
        if 'arxiv.org' in domain:
            print("Calling arxiv function")
            return self.arxiv(response)
        elif 'proceedings.neurips.cc' in domain:
            print("Calling neurips function")
            return self.neurips(response)
        elif 'papers.neurips.cc' in domain:
            print("Calling neurips function")
            return self.neurips(response)
        elif 'coursera.org' in domain:
            print("Calling coursera function")
            return self.coursera(response)
        elif 'ruder.io' in domain:
            print("Calling ruder function")
            return self.ruder(response)
        elif 'therobotreport.com' in domain:
            print("Calling robotreport function")
            return self.robotreport(response)
        # code unable to pass through scraper and produces no result
        # to be improved in the future
        # # Extract article URLs from the current page and pass them to the parsing function
        #     article_links = response.css('article h2 a::attr(href)').getall()
        #     if self.max_page > len(article_links):
        #         for link in article_links[:]:
        #             yield response.follow(link, callback = self.robotreport)
            
        #     else:
        #         for link in article_links[:self.max_page]:
        #             yield response.follow(link, callback = self.robotreport)

        #      # Get the next page URL and pass it to the parse function if it's within the max_pages limit
        #     current_page_number = response.url.split('page=')[-1]
        #     if current_page_number.isdigit() and int(current_page_number) < self.max_depth_count:
        #         next_page_number = int(current_page_number) + 1
        #         next_page_url = f'https://www.therobotreport.com/?s=robotics&page={next_page_number}'
        #         yield scrapy.Request(next_page_url, callback = self.parse)
        else:
            print(f"No parsing function for domain: {domain}")
        

    def arxiv(self, response):
        items = HtmlscraperItem()
        url = response.url
        new_title = response.css('h1.title.mathjax::text').get()
    # Ensure new_title is a string, even if it's None
        new_title = new_title.strip() if new_title else ""
    
        abstract_paragraph = response.css('blockquote.abstract.mathjax ::text').getall()
    # Join the parts to form the full abstract text
        paragraph = ''.join(abstract_paragraph).strip()
    
    # Safely concatenate new_title and paragraph
        main_text = new_title + " " + paragraph if new_title and paragraph else new_title + paragraph
        items['url'] = url
        items['text'] = main_text
        items['title'] = new_title

        yield items

    def neurips(self, response):
        items = HtmlscraperItem()
        url = response.url
        title = response.css('h4::text').get()

    # # Extract the authors from the <i> tag
        authors = response.css('i::text').get()

    # # Extract the text following the 'Abstract' header
    # # This assumes that there is a single abstract and that it follows an <h4> with the text 'Abstract'
        text = response.css('div.col > p::text').getall()
        abstract_text = ' '.join([part.strip() for part in text])
             # Clean up the text by stripping whitespace:
        title = title.strip()if title else None
        authors = authors.strip()if authors else None
        content = ' '.join(abstract_text.split())
        main_text = title + authors + content

    # Yield the extracted information
        items['url'] = url
        items['text'] = main_text
        items['title'] = title
        yield items
        
    def coursera(self, response):
        items = HtmlscraperItem()
        url = response.url
    # Correct the title selector for Coursera's structure
        title = response.css('h1[data-e2e="article-page-title"]::text').get().strip()
        if title:
            title = title.strip()
        else:
            self.logger.error('Title not found on the page.')
            return
    # Find all the relevant <p> tags within the specific <div>
        paragraphs =  response.css('div.css-do4pef p, div.css-11jeka p, div.rc-Richtext p').getall() 
        combined_text = []
    
        for paragraph in paragraphs:
        # Extract the text nodes, which gets the text content and excludes HTML tags
            paragraph_selector = scrapy.Selector(text=paragraph)

        # Now you can use .xpath() on this Selector object
            text_nodes = paragraph_selector.xpath('.//text()').getall()

        # Clean the text nodes and join them into a single string
            clean_text = ' '.join([text.strip() for text in text_nodes if text.strip()])

        # Add the clean text to the all_text list
            combined_text.append(clean_text)

        main_text = title + ' ' + ' '.join(combined_text) if combined_text else title

        items['url'] = url
        items['text'] = main_text
        items['title'] = title
        yield items
        
    def ruder(self, response):
        items = HtmlscraperItem()
        url = response.url
    # Correct the title selector for Coursera's structure
        title = response.css('h1.article-title::text').get()

        if title:
            title = title.strip()
        else:
            self.logger.error('Title not found on the page.')
            return

    # Find all the relevant <p> tags within the specific <div>
        paragraphs_html = response.css('section.gh-content.gh-canvas p::text').getall()
        text  = ' '.join(paragraphs_html)

        items['url'] = url
        items['text'] = text
        items['title'] = title
        yield items
        
    def robotreport(self, response):
        items = HtmlscraperItem()
        url = response.url
    # Correct the title selector for Coursera's structure
        title = response.css('h1.entry-title::text').get()
        if title:
            title = title.strip()
        else:
            self.logger.error('Title not found on the page.')
            return

    # Find all the relevant <p> tags within the specific <div>
        paragraphs_html = response.css('div.entry-content p::text').getall() 
        paragraph = ' '.join(paragraphs_html)
        subtitle = response.css('div.entry-content h2::text').getall() 
        add_title = ' '.join(subtitle)

        text = title + add_title + paragraph 

        items['url'] = url
        items['text'] = text
        items['title'] =title
        yield items   
        