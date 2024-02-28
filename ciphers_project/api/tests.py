from django.test import TestCase
from .ciphers import caesar_cipher
# Create your tests here.
class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        self.assertEqual(caesar_cipher(plain_text, shift), expected)
    def test_caesar_encoding_2(self):
        plain_text="winter"
        shift=3
        expected="zlqwhu"
        self.assertEqual(caesar_cipher(plain_text, shift), expected)
    # find flaw in the caesar_cipher function
    def test_caesar_encoding_3(self):
        plain_text = "hello"
        shift = 1
        expected = "hello"
        self.assertNotEqual(caesar_cipher(plain_text, shift), expected)
    def test_caesar_encoding_4(self):
        plain_text="winter"
        shift=3
        expected="winter"
        self.assertNotEqual(caesar_cipher(plain_text, shift), expected)