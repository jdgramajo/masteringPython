import unittest

from notes.note import Note

class TestNote(unittest.TestCase):
    
    note = None

    @classmethod
    def setUpClass(cls):
        TestNote.note = Note("Sample memo", "Sample tag")

    @classmethod
    def tearDownClass(cls):
        del TestNote.note

    def test_find_note_by_memo_or_tag(self):
        self.assertTrue(TestNote.note.match("Sample"))

    def test_find_note_by_memo(self):
        self.assertTrue(TestNote.note.match("memo"))

    def test_find_note_by_tag(self):
        self.assertTrue(TestNote.note.match("tag"))
