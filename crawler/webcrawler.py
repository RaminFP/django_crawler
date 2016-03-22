from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from threading import Thread
import queue


class LinkParser(HTMLParser):


    def handle_starttag(self, tag, attrs):

        if tag  == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    def getLinks(self, url):

        global weblink
        self.links = []
        self.baseUrl = url
        response = LinkParser().getopen(url)
        if response.getheader('Content-Type') == 'text/html; charset=utf-8' or response.getheader('Content-Type') == 'text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.links
        else:
            return "",[]


    def getopen(self,url):
        return urlopen(url)

    def processing(self,weburl):

            from multiprocessing.pool import ThreadPool
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(LinkParser().getLinks,(weburl,))
            return_val = async_result.get()
            return return_val



class TextParser(HTMLParser):


    def handle_starttag(self, tag, attrs):

        if tag  == 'a':
            for (key, value) in attrs:
                if key == 'title':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    def getLinks(self, url):

        self.links = []
        self.baseUrl = url
        response = LinkParser().getopen(url)
        if response.getheader('Content-Type') == 'text/html; charset=utf-8' or response.getheader('Content-Type') == 'text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]



    def getopen(self,url):

        return urlopen(url)


