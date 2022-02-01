from CardValidator import checkLuhn
import unittest

class TestCardValidator(unittest.TestCase):

    def testCases(self):
        self.assertTrue(checkLuhn("79927398713"))
        self.assertFalse(checkLuhn("79927398715"))

        with self.assertRaises(TypeError):
            checkLuhn(79927398713)

if __name__ == '__main__':
    unittest.main()
