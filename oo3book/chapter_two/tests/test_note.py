import unittest

from notes.note import Note

class TestNote(unittest.TestCase):
    
    def setUp(self):
        self.note = Note("Sample memo", "Sample tag")

    def tearDown(self):
        del self.note

    def test_find_note(self):
        self.assertTrue(self.note.match("Sample"))
