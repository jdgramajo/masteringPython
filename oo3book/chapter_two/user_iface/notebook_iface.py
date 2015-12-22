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

    def do_add(self, *args):
        'Adds a note to the notebook with first param as memo
        and second param as tag.
        If there is no notebook in use, it warns and exits.
        Usage: add all words in memo tag:tag'
        if self.notebook == None:
            print('No notebook created yet, create one first.')
        else:
            all_params = args.split()
            self.notebook.new_note(all_params[0:-1], 
                all_paramsi[-1:].split(':')[1])

    def do_reset(self, args):
        'Clear screen.'
        capture = sp.call('clear', shell = True)

    def do_bye(self, args):
        'Says goodbye and exits.'
        print('Goodbye!')
        return True

if __name__ == '__main__':
    NotebookIface().cmdloop()
