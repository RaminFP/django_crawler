from crawler import webcrawler
from time import  time
from threading import Thread
class FatherSpider():

    @staticmethod
    def spider(url, word, maxPages):

        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False
        tm1 = time()

        while numberVisited < maxPages and pagesToVisit != [] or not foundWord:

            numberVisited = numberVisited +1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]

            try:

                data, links = webcrawler.LinkParser().getLinks(url)
               # data ,title= webcrawler.TextParser().getLinks(url)
                if data.find(word)> -1:
                    foundWord = True
                    pagesToVisit = pagesToVisit + links
                    linklst = set(pagesToVisit)
                    legthlink = len(linklst)
                    tm2 = time()
                    timeup = tm2 - tm1
                    return (linklst,legthlink,timeup)

            except Exception as e:
                print( " **Failed!**")

        if foundWord:
            print("The word", word, "was found at", url)
        else:
            print("Word never found")



