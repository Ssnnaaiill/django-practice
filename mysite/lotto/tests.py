from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name="kinew", text="VlVlDPEARL")
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lotto) > 20)
