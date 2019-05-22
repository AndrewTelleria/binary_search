import unittest
import random

from faker import Faker

from search.binary_search import binary_search


fake = Faker()


def get_fake_names():
    names = []
    for _ in range(100):
        names.append(fake.name())
    names.sort()
    item = random.choice(names)
    index = names.index(item)
    return names, item, index


def get_fake_emails():
    emails = []
    for _ in range(500):
        emails.append(fake.ascii_email())
    emails.sort()
    item = random.choice(emails)
    index = emails.index(item)
    return emails, item, index


def get_fake_passwords():
    passwords = []
    for _ in range(1000):
        passwords.append(fake.password(length=16,
                                       special_chars=True,
                                       digits=True,
                                       upper_case=True,
                                       lower_case=True))
    passwords.sort()
    item = random.choice(passwords)
    index = passwords.index(item)
    return passwords, item, index


class TestSearch(unittest.TestCase):
    """Unit tests for the binary search algorithm"""
    def test_output(self):
        """Test that it can search a list of integers"""
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        result = binary_search(data, 4)
        self.assertEqual(result, 3)

    def test_output_none_negative(self):
        """Test that it can return None if element is below the list range"""
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        result = binary_search(data, -1)
        self.assertIsNone(result)

    def test_output_none_positive(self):
        """Test that it can return None if element is above the list range"""
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        result = binary_search(data, 9)
        self.assertIsNone(result)

    def test_output_strings(self):
        """Test that it can return the index of a string element"""
        data = ['bar', 'eggs', 'foo', 'ham', 'python', 'spam']
        result = binary_search(data, "bar")
        self.assertEqual(result, 0)

    def test_100_names(self):
        """Test the return from 100 names for the correct index"""
        names, item, index = get_fake_names()
        result = binary_search(names, item)
        self.assertEqual(result, index)

    def test_500_emails(self):
        """Test the return from 500 emails for the correct index"""
        emails, item, index = get_fake_emails()
        result = binary_search(emails, item)
        self.assertEqual(result, index)

    def test_1000_passwords(self):
        """Test the return from 1000 passwords for the correct index"""
        passwords, item, index = get_fake_emails()
        result = binary_search(passwords, item)
        self.assertEqual(result, index)

    def test_dictionary(self):
        """Make sure the input is a dictionary"""
        data = {'foo': 'bar', 'spam': 'eggs'}
        result = binary_search(data, 1)
        self.assertEqual(result, "Data type needs to be a list")

    def test_tuple(self):
        """Make sure the input is not a tuple"""
        data = ('foo', 'bar', 'spam', 'eggs')
        result = binary_search(data, 1)
        self.assertEqual(result, "Data type needs to be a list")


if __name__ == '__main__':
    unittest.main()
