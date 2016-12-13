import requests
from fake_useragent import UserAgent
from lxml import html, etree
import re

# nUrl is a wrapper for manipulating a single page
# focus on extracting content, links, and finding pages
class nUrl:
    def __init__(self, *args):
        self.ua = UserAgent()
        self.proxies = {}
        self.headers = {'User-Agent': self.ua.chrome}
        self.url = args[0]
        self.count = 0
        self.r = requests.get(self.url, headers=self.headers)
        self.tree = html.fromstring(self.r.text)
        self.currentEle = None
        self.elements = None

# returns html Element of page request
# accepts a requests object after .get method success
    def treeString(self):
        return self.r.text

    def setUrl(self, url):
        self.url = url
        return self.loadUrl()

    def loadUrl(self):
        try:
            self.r = requests.get(self.url)
            if int(self.r.status_code) == 200:
                return True
            else:
                return False
        except UrlNotLoadedError('The request has timed out or failed and the url cannot be loaded'):
            return False

# returns child Element of ele matching tag
    def select(self, tag):
        self.currentEle = tag
        self.elements = self.tree.cssselect(tag)
        return self.elements

# returns list Element objects that match the given tag
    def findAll(self, tag):
        search = './/%s' % tag
        return self.tree.findall(search)

    def getHref(self, ele):
        self.currentEle = ele
        return ele.get('href')



#TODO
# needs to store all next page matches to a list
# and determine which page needs to be loaded next
# first page first and save the rest to a list
    def nextPage(self):
        regex = re.compile('count=')
        self.select('a')
        for a in self.elements:
            try:
                href = str(a.get('href'))
                if regex.search(href):
                    self.setUrl(a.get('href'))
            except:
                pass
        
    def getInternalLinks( self ):
        url = self.url
        internalLinks = [] 
        links = self.findAll( 'a' )
        r_internalLinks = re.compile("^(((http:\/\/)*(www\.)*"+url+"\/)|#\w(.+)*|\/|(?!http)?\w)")
        for link in links:
            attr = link.items()
            for a in attr:
                if 'href' in a:
                    if r_internalLinks.search(a[1]):
                        internalLinks.append( a[1] )
                    else:
                        pass
                else:
                    pass
        return internalLinks

    def getOutboundLinks( self ):
        url = self.url
        outboundLinks = [] 
        links = self.findAll( 'a' )
        r_outboundLinks = re.compile("^(?!((http:\/\/)*(www\.)*"+url+"\/)|#|\/|(?!http)\w)")
        for link in links:
            attr = link.items()
            for a in attr:
                if 'href' in a:
                    if r_outboundLinks.search(a[1]):
                        outboundLinks.append( a[1] )
                    else:
                        pass
                else:
                    pass
        return outboundLinks
