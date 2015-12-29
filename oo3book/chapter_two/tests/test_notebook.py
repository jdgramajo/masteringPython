import unittest

from chapter_two.notes.notebook import Notebook

class TestNotebook(unittest.TestCase):

    notebook = None

    @classmethod
    def setUpClass(cls):
        TestNotebook.notebook = Notebook()

    @classmethod
    def tearDownClass(cls):
        del TestNotebook.notebook

    def test_01_new_note(self):
        TestNotebook.notebook.new_note("Sample note", "Sample tag")
        self.assertEqual(len(TestNotebook.notebook.notes), 1)

    def test_02_search(self):
        self.assertNotEqual(len(TestNotebook.notebook.search("Sample note")), 0)
        self.assertEqual(len(TestNotebook.notebook.search("Non existent note")), 0)

    # Turns out that the first note created in notebook receives an id of 2,
    # very likely because when the Note class is loaded, it is run and the first
    # inc of last_id happens, so the first instatiation receives a no. 2.
    def test_03_modify_memo(self):
        TestNotebook.notebook.modify_memo(2, "Modified memo")
        self.assertEqual(TestNotebook.notebook.notes[0].memo, "Modified memo")
        
    def test_04_modify_tag(self):
        TestNotebook.notebook.modify_tags(2, "Modified tag")
        self.assertEqual(TestNotebook.notebook.notes[0].tags, "Modified tag")
