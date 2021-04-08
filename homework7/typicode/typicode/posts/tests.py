from django.test import TestCase


# Create your tests here.
class TestCount(TestCase):
    
    def test_count_empty(self):
        self.assertEqual(1, 0)
    
    def test_count(self):
        self.assertEqual(2, 2)
        
