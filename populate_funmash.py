import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funmash.settings')

import django

django.setup()

from funmash_app.models import Image
from django.conf import settings

def populate():
    images = {}
    for x in range(1,15):
        id = str(x) + ".jpg"
        #The one line below is these three lines combined:
        #images["name"]= "1 ("+x+").jpg",
        #images["source"] = settings.MEDIA_URL+"/"+id
        #images["ranking"] = x+1
        add_img(str(x), settings.MEDIA_URL+id, x+1, "Nobilitie")
        print("added" + settings.MEDIA_URL + id)



def add_img(name,source,ranking,ownerName):
    img = Image.objects.get_or_create(name=name)[0]
    img.source = source
    img.ranking = ranking
    img.owner = ownerName
    img.save()
    return img




# Start execution here!
if __name__ == '__main__':
    print("Starting Funmash population script...")
    populate()