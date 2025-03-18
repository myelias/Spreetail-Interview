import unittest
from unittest.mock import patch
from io import StringIO
from multiValueDict import MultiValueDict

class TestMultiValueDict(unittest.TestCase):
    def setUp(self):
        self.db = MultiValueDict()

    def capture_output(self, func, *args):
        """
        Helper function to capture printed output
        patch() acts as a function decorator, class decorator or a context manager. 
        Inside the body of the function or with statement, the target is patched with a new object. 
        When the function/with statement exits the patch is undone.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            func(*args)
            return fake_out.getvalue().strip() # retrieves everything that was printed inside the with block.

    def test_add(self):
        output = self.capture_output(self.db.add, "key1", "value1")
        self.assertEqual(output, ") Added")
        output = self.capture_output(self.db.add, "key1", "value1")
        self.assertEqual(output, ") ERROR, member already exists for key")

    def test_keys(self):
        self.db.add("key1", "value1")
        self.db.add("key2", "value2")
        output = self.capture_output(self.db.keys)
        self.assertIn("1) key1", output)
        self.assertIn("2) key2", output)

    def test_members(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.members, "key1")
        self.assertIn("1) value1", output)

        output = self.capture_output(self.db.members, "key2")
        self.assertEqual(output, ") ERROR, key does not exist.")

    def test_remove(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.remove, "key1", "value1")
        self.assertEqual(output, ") Removed")
        
        output = self.capture_output(self.db.remove, "key1", "value1")
        self.assertEqual(output, ") ERROR, key does not exist")
        
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.remove, "key1", "value2")
        self.assertEqual(output, ") ERROR, member does not exist")

    def test_remove_all(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.remove_all, "key1")
        self.assertEqual(output, ") Removed")

        output = self.capture_output(self.db.remove_all, "key1")
        self.assertEqual(output, ") ERROR, key does not exist")

    def test_clear(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.clear)
        self.assertEqual(output, ") Cleared")

        self.db.add("key1", "value1")
        self.db.add("key2", "value2")
        output = self.capture_output(self.db.clear)
        self.assertEqual(output, ") Cleared")
        
        output = self.capture_output(self.db.keys)
        self.assertEqual(output, "(empty set)")

    def test_key_exists(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.key_exists, "key1")
        self.assertEqual(output, ") true")

        output = self.capture_output(self.db.key_exists, "key2")
        self.assertEqual(output, ") false")

    def test_member_exists(self):
        self.db.add("key1", "value1")
        output = self.capture_output(self.db.member_exists, "key1", "value1")
        self.assertEqual(output, ") true")

        output = self.capture_output(self.db.member_exists, "key1", "value2")
        self.assertEqual(output, ") false")

    def test_all_members(self):
        self.db.add("key1", "value1")
        self.db.add("key2", "value2")
        output = self.capture_output(self.db.all_members)
        self.assertIn("1) value1", output)
        self.assertIn("2) value2", output)

    def test_items(self):
        self.db.add("key1", "value1")
        self.db.add("key1", "value2")
        output = self.capture_output(self.db.items)
        self.assertIn("key1: value1", output)
        self.assertIn("key1: value2", output)

if __name__ == "__main__":
    unittest.main()
