import unittest
from cipher_project import cipher


class TestCipher(unittest.TestCase):
    def test_cipher_rejects_invalid_date(self):
        invalid_shift = 13
        self.assertRaises(
            Exception,
            cipher, "test", invalid_shift,
        )

    def test_cipher_rejects_invalid_world(self):
        invalid_word = "34387sdfasdad7"
        self.assertRaises(
            Exception,
            cipher, invalid_word, 3,
        )

    def test_cipher_shift(self):
        actual_output = cipher("Holly", 11)
        expected_output = "Szwwj"
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
