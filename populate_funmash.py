import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funmash.settings')

import django

django.setup()

from funmash_app.models import Image
from django.conf import settings

def populate():
    images = {}
    for x in range(1,13):
        id = "1 (" + str(x) + ").jpg"
        #images["name"]= "1 ("+x+").jpg",
        #images["source"] = settings.MEDIA_URL+"/"+id
        #images["ranking"] = x+1
        add_img(id, settings.MEDIA_URL+id, x+1)
        print("added" + settings.MEDIA_URL + id)



def add_img(name,source,ranking):
    img = Image.objects.get_or_create(name=name)[0]
    img.source = source
    img.ranking = ranking
    img.save()
    return img




# Start execution here!
if __name__ == '__main__':
    print("Starting Funmash population script...")
    populate()