import cmd
import subprocess as sp

class NotebookIface(cmd.Cmd):
    intro = 'Interface for the notebook program.'
    prompt = 'notebook> '
    file = None

    def do_hello(self, args):
        'Greet user.'
        print('Hi user!')

    def do_reset(self, args):
        'Clear screen.'
        capture = sp.call('clear', shell = True)

    def do_bye(self, args):
        'Says goodbye and exits.'
        print('Goodbye!')
        return True

if __name__ == '__main__':
    NotebookIface().cmdloop()
