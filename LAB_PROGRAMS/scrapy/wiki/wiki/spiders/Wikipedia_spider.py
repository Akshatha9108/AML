import scrapy
class WikipediaSpider(scrapy.Spider):
      name='program1'
      start_urls=['https://nmamit.nitte.edu.in/']
      
      #set the user agent
      custom_setings={
          'USER_AGENT':'Mozilla/5.0(Windows NT 10.0;Win64; x64)AppleWebkit/537.36(KHTML,like Gecko)  Chrome/88.0.4324.150 Safari/537.36'
      }
      
      def parse(self, response):
          #Extract Images
          images=response.css('img::attr(src)').getall()
          
           #Extract paragraphs
          paragraphs=response.css('p::text').getall()
           
          #save images to a file
          with open('images.txt','w')as file:
               for image in images:
                file.write(image + '\n')
           #save paragraphs to a file
           
          with open('paragraphs.txt','w')as file:
               for paragraph in paragraphs:
                file.write(paragraphs + '\n')
        
