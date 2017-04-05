import unittest
import game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.human = game.HUMAN
        self.opposition = game.OPPOSITION
        self.avail = game.AVAIL

    def test_player_difference(self):
        self.assertNotEqual(self.human, self.opposition)
        self.assertGreater(self.human, self.opposition)
        self.assertEqual(self.avail, 0)


if __name__ == '__main__()':
    unittest.main()


