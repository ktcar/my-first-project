import requests
from bs4 import BeautifulSoup
import os
from price.models import Items


# from price.models import BlogData
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "priceindector.settings")
# django.setup()
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_item():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select(
        'h3 > a'
    )

    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')

    print("data type = %s" % type(data))
    print(data)

    return data


data_dict = parse_item()

print("data type = %s" % type(Items))



# if __name__=='__main__':
#    item_data_dict = parse_item()
#    for t, l in item_data_dict.items():
#        BlogData(title=t, link=l).save()
