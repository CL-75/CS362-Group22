import unittest
import task


class TestValidInteger(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_integer(num), False)


if __name__ == '__main__':
    unittest.main()
