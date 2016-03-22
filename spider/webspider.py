from crawler import webcrawler
from time import  time
from threading import Thread


class FatherSpider():

    @staticmethod
    def spider(url, word, maxPages):

        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False

        while numberVisited < maxPages and pagesToVisit != [] or not foundWord:

            numberVisited = numberVisited +1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]

            try:
                tm1 = time()

                # Without thread
                #links = webcrawler.LinkParser().getLinks(url)
                # With Thread
                lst = webcrawler.LinkParser().processing(url)
                linklst = set(lst)
                legthlink = len(linklst)
                tm2 = time()
                timeup = tm2 - tm1
                return (linklst,legthlink,timeup)

            except Exception as e:
                print(" **Failed!**")

        if foundWord:
            print("The word", word, "was found at", url)
        else:
            print("Word never found")



