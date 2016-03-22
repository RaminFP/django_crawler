from crawler import webcrawler
from time import  time
from django.shortcuts import HttpResponse

class FatherSpider():

    @staticmethod
    def spider(url):
        try:
                tm1 = time()
                lst = webcrawler.LinkParser().processing(url)
                if isinstance(lst,list):
                    linklst = set(lst)
                    legthlink = len(linklst)
                    tm2 = time()
                    timeup = tm2 - tm1
                    return (linklst,legthlink,timeup)

        except Exception as e:
                return HttpResponse("Found Error : %s") % e

