from django.test import TestCase
from .models import MegaNumbers, Drawing

class ResultsTestCase(TestCase):
    def setUp(self):
        Drawing.objects.create(numbers='01,02,03,04,05',megaBall=6, multiplier=4,drawingDate='2016-07-22')
        Drawing.objects.create(numbers='02,03,04,05,06',megaBall=7, multiplier=3,drawingDate='2016-07-23')

    def test_MegaNumbers_saved(self)
        Drawing.objects.create(numbers='03,04,05,06,07',megaBall=8, multiplier=3,drawingDate='2016-07-24')
        drawing = Drawing.objects.get(drawingDate='2016-07-24')
        self.assertEqual(drawing.multiplier, 3)

    def test_drawing_saved(self):
        drawing = Drawing.objects.get(drawingDate='2016-07-22')
        self.assertEqual(drawing.multiplier, 4)
        drawing = Drawing.objects.get(drawingDate='2016-07-23')
        self.assertEqual(drawing.multiplier, 3)
