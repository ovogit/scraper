from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import requests
from fake_useragent import UserAgent
from nfile import nFile

# phantom js chrom useragent setup
ua = UserAgent()
webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = ua.chrome

driver = webdriver.PhantomJS()
driver.get('https://www.google.com/#q=lose+weight+fast')
treeString = driver.page_source
tree = html.fromstring(driver.page_source)

f = nFile('output.txt','w')
f.write(treeString)

#print headers
#r = requests.get('https://www.google.com/#q=lose+weight+fast', headers=headers)

#with open('test.txt','wb') as f:
    #f.write(r.text)

#l = []
#tree = html.fromstring(r.text)

#links = tree.xpath('//h3[contains(@class, "r")]')

#for link in links:
    #print link.xpath('//a::text()')
