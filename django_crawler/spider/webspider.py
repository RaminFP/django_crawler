from crawler import webcrawler


class FatherSpider():

    def spider(self,url, word, maxPages):

        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False
        while numberVisited < maxPages and pagesToVisit != [] and not foundWord:

            numberVisited = numberVisited +1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numberVisited, "Visiting:", url)

                data, links = webcrawler.LinkParser().getLinks(url)
                if data.find(word)> -1:
                    foundWord = True
                    pagesToVisit = pagesToVisit + links
                    linklst = set(pagesToVisit)
                    #i = 1
                    print("Length This Domains:" , len(linklst))
                    print(" **Success!**")
                    return linklst

                    # for item in linklst:
                    #     print("Spider Find This links of this site: %s"  % i , item)
                    #
                    #     i = i + 1

            except Exception as e:
                print(" **Failed!**")
        if foundWord:
            print("The word", word, "was found at", url)
        else:
            print("Word never found")