
# unit test case
import unittest

class SimpleTest(unittest.TestCase):

    def test_split(self):
        s = 'yes YES'
        self.assertEqual(s.split(), ['yes', 'YES'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_split_2(self):
        s = 'no NO'
        self.assertEqual(s.split(), ['no', 'NO'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
