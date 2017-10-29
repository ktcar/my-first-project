from django.shortcuts import render
from price.models import Items
from django.views.generic.base import TemplateView
import urllib.request
import json
from django.shortcuts import get_object_or_404

client_id = "ryITVMNdCgeAPkbfn8tx"
client_secret = "KH4GaFl1MJ"
encText = urllib.parse.quote("9791160500844")
url = "https://openapi.naver.com/v1/search/book?display=1&query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()


# Create your views here.
class HomeView(TemplateView):

    template_name = "price/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def list_(request):

    if (rescode == 200):
        #response_body = response.read()
        #data = response_body.decode('utf-8')
        #dictdata = json.loads(data)
        #print("data type = %s" % type(dictdata))
        #datasub1 = dictdata["items"]
        #print("data type = %s" % type(datasub1))

        #dicDataSub = datasub1[0]
        #print("data type = %s" % type(dicDataSub))
        #print(dicDataSub)

        #bookItem = Items(**dicDataSub)
        #bookItem.isbn_id = 9791160500844
        #bookItem.save()
        #print(bookItem)

        print("==========")

        #Items.objects.create(**dicDataSub)
    else:
        print("Error Code:" + rescode)

    item_list = Items.objects.all().order_by('-isbn')[::]
    print(item_list)
    context = {'item_list': item_list}
    return render(request, 'price/list.html', context)


def details(request, isbn_id):
    item = get_object_or_404(Items, pk=isbn_id)
    context = {'item': item}
    return render(request, 'price/details.html', context)



