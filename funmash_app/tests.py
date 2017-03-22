from django.test import TestCase
from funmash_app.models import Images
		
class ImageMethodTests(TestCase):
	def test_ensure_rankings_are_postive(self):
	
		rank = Image(name="test",ranking=-1,owner="Nobilitie")
		rank.save()
		self.assertEqual((rank.ranking>=0,True)

