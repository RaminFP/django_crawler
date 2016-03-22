from django.shortcuts import render
from spider.webspider import FatherSpider
import socket


class Index():

    def index(self,request):

        if request.POST:
            domain = request.POST.get("domain")
            try:
                url = "www.%s.com" % domain
                socket.gethostbyname(url)
                urls = "http://%s/" % (url)
            except socket.gaierror:
                return render(request,'search.html',{'badadd':'did not match any documents.'})
            links = FatherSpider().spider(urls)
            context_1 = {'linkss':links[0],'len':links[1],'time':links[2]}
            return render(request,'search.html',context_1)

        return render(request,'index.html')

