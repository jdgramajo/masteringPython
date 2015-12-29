import cmd
import subprocess as sp

from chapter_two.notes.notebook import Notebook

class NotebookIface(cmd.Cmd):
    intro = 'Interface for the notebook program.'
    prompt = 'notebook> '
    file = None
    notebook = None

    def do_hello(self, args):
        'Greet user.'
        print('Hi user!')

    def do_notebook(self, args):
        'Create new notebook if none exists, indicate otherwise'
        if self.notebook == None:
            self.notebook = Notebook()
        else:
            print('A notebook already is in use.')

    def do_add(self, args):
        """\
        Adds a note to the notebook with first param as memo
        and second param as tag.
        If there is no notebook in use, it warns and exits.
        Usage: add all words in memo tag:tag"""
        if self.notebook == None:
            print('No notebook created yet, create one first.')
        else:
            # These next three lines really really are bad, but I'm just
            # learning so I'll leave them as they are 'cause they work.
            all_args = ''.join(args)
            self.notebook.new_note(' '.join(all_args.split()[0:-1]), 
                all_args.split()[-1::][0].split(':')[1])

    def do_show_all(self, args):
        'Shows all memos and tags'
        for note in self.notebook.notes:
            print('id: {}\nMemo: {}\ntag: {}\n'.format(note.id,
                note.memo, note.tags))

    def do_mod_memo(self, args):
        """\
        Modifies note's memo.
        Usage: 'mod_memo id new memo content'
        NOTE: There is no validation, enter a valid id!
        """
        all_args = ''.join(args)
        self.notebook.modify_memo(int(all_args[0]), ''.join(all_args[1::]))

    def do_mod_tag(self, args):
        """\
        Modifies note's tag.
        Usage: 'mod_memo id new tag'
        NOTE: There is no validation, enter a valid id!
        """
        all_args = ''.join(args)
        self.notebook.modify_tags(int(all_args[0]), ''.join(all_args[1::]))

    def do_reset(self, args):
        'Clear screen.'
        capture = sp.call('clear', shell = True)

    def do_bye(self, args):
        'Says goodbye and exits.'
        print('Goodbye!')
        return True

if __name__ == '__main__':
    NotebookIface().cmdloop()
