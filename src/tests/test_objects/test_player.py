from unittest import TestCase

from main.objects.player import Player

class TestToolsObjects(TestCase):

    def test_win(self):
        player = Player(5)
        player.play((0,0))
        column = [0,1,0,0,1,1]
        expected = set([1,4,5])
        self.assertEqual(transform(column),expected)