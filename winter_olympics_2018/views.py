import os
from collections import OrderedDict

from django.http.response import HttpResponse

from .models import Country

import matplotlib.pyplot as plt
from PIL import Image


def mapimage(request):
    '''view for displaying graph as a response from the values in database for top 10 countries'''

    #getting data from database
    top_10_country_object_list = Country.objects.filter(rank__in=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).order_by('rank')
    name_list = top_10_country_object_list.values_list('noc', flat=True)
    gold_list = top_10_country_object_list.values_list('gold', flat=True)
    silver_list = top_10_country_object_list.values_list('silver',flat=True)
    bronze_list = top_10_country_object_list.values_list('bronze',flat=True)

    #decracing custom font
    csfont = {'fontname': 'Comic Sans MS'}

    #plotting graph
    plt.plot(name_list, gold_list, label='gold', color='#d6c333', linewidth=3)
    plt.plot(name_list, silver_list, label='silver', color='#dddddd', linewidth=3)
    plt.plot(name_list, bronze_list, label='bronze', color='#89803c', linewidth=3)
    plt.xlabel('\nCountries', **csfont)
    plt.ylabel('\nNo of Medals\n', **csfont)
    plt.title('Winter olymics 2018', **csfont)
    plt.xticks(rotation=45) #rotating x-axis labels 45%
    plt.subplots_adjust(bottom=0.3) #adjusting bottom of map to image

    #to avoid duplication of legends
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    os.remove('foo.png')
    plt.savefig('foo.png') #save image from graph

    #open image from file oobject and return as response
    img = Image.open('foo.png')
    response = HttpResponse(content_type="image/png")
    img.save(response, 'PNG')
    return response
