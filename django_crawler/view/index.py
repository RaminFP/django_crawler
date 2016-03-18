from django.shortcuts import render ,HttpResponse
from spider.webspider import FatherSpider


class Index():

    def index(self,request):

        links = FatherSpider().spider('http://www.saminray.com',"info@Saminray.com",200)
        context = {'linkss':links}
        return render(request,'index.html',context)