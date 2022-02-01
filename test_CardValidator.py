import unittest

class TestCardValidator(unittest.TestCase):

    def testCases(self):
        self.assertTrue(checkLuhn("79927398713"), True)
        self.assertTrue(checkLuhn("79927398715"), False)

        with self.assertRaises(TypeError):
            checkLuhn(79927398713)

if __name__ == '__main__':
    unittest.main()
