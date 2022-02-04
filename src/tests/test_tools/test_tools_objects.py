from unittest import TestCase

from main.tools.tools_objects.transform import transform
from main.tools.tools_objects.get_next import get_next

class TestToolsObjects(TestCase):

    def test_transform(self):
        column = [0,1,0,0,1,1]
        expected = set([1,4,5])
        self.assertEqual(transform(column),expected)

    def test_get_next(self):
        current = set([0,3])
        expected = set([0,2,3])
        self.assertEqual(get_next(current),expected)
