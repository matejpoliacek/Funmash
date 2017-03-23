from django.test import TestCase
from funmash_app.models import Image
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funmash.settings')
# Create your tests here.
from django.core.urlresolvers import reverse
def add_img(name, source, ranking, ownerName):
    img = Image.objects.get_or_create(name=name)[0]
    img.source = source
    img.ranking = ranking
    img.owner = ownerName
    img.save()
    return img
class IndexViewTests(TestCase):
	#Test if the page loads
    def test_index_view(self):

        images = {}
        # change if you want to add all pictures
        for x in range(1, 15):
            id = str(x) + ".jpg"
            # The one line below is these three lines combined:
            # images["name"]= "1 ("+x+").jpg",
            # images["source"] = settings.MEDIA_URL+"/"+id
            # images["ranking"] = x+1
            add_img(str(x), settings.MEDIA_URL + id, x + 1, "Nobilitie")

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
	
	#Test if the pictures does not have the same source
    def test_index_view2(self):
        images = {}
        # change if you want to add all pictures
        for x in range(1, 15):
            id = str(x) + ".jpg"
            # The one line below is these three lines combined:
            # images["name"]= "1 ("+x+").jpg",
            # images["source"] = settings.MEDIA_URL+"/"+id
            # images["ranking"] = x+1
            add_img(str(x), settings.MEDIA_URL + id, x + 1, "Nobilitie")
        response = self.client.get(reverse('index'))
        self.assertNotEqual(response.context['firstImage'].source, response.context['secondImage'].source)

	#Check that it doesnot allow to view top 5 images unless signed in
	#And we are redirected to other page
    def test_top_5_302(self):
        response = self.client.get(reverse('top5'))
        self.assertEqual(response.status_code, 302)


    #Not signed in users are redirected sign in page when attempting
    #to access profile page

    def test_profile_302(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

	#Test if see the content of unlogged user
    def test_index_logged_in_content(self):
        images = {}
        # change if you want to add all pictures
        for x in range(1, 15):
            id = str(x) + ".jpg"
            # The one line below is these three lines combined:
            # images["name"]= "1 ("+x+").jpg",
            # images["source"] = settings.MEDIA_URL+"/"+id
            # images["ranking"] = x+1
            add_img(str(x), settings.MEDIA_URL + id, x + 1, "Nobilitie")
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Log in to see image owner")





