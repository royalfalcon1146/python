
#! USING XPATH TO GET CONTENT FROM A WEBSITE, USING BS4 AND LXML AND REQUESTS
#? MAKE SURE TO DOWNLOAD THE MODULES
import requests
from bs4 import BeautifulSoup
from lxml import etree

URL = "URL HERE"

#? IGNORE THE HEADERS THING
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS) #? IGNORE
soup = BeautifulSoup(webpage.content, "html.parser") #?I GNORE
dom = etree.HTML(str(soup)) #? IGNORE
print(dom.xpath('XPATH HERE')[0].text)
