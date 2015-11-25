"""User interfaces for Pipeline."""

import cmd
import sys
import pickle
from pathlib import Path

from pipeline import step

class TextInterface(cmd.Cmd):
    """Text-based interface for Pipeline"""

    def __init__(self, keep_going, filename):
        super().__init__(completekey = 'tab')
        self.keep_going = keep_going
        self.path = Path(filename)
        self.prompt = 'Pipeline> '

        try:
            with self.path.open('rb') as f:
                self.steps = pickle.load(f)
        except FileNotFoundError:
            self.steps = []

    def do_exec(self, arg):
        """Append a program invocation to the pipeline"""
        args = arg.split()
        self.steps.append(step.ExecStep(args))

    def do_args(self, arg):
        """Use the last output as arguments instead of input"""
        sep = arg if arg else None
        self.steps.append(step.ArgsStep(sep))

    def do_store(self, arg):
        """Store the last output in a file"""
        self.steps.append(step.StoreStep(arg.strip()))

    def do_inject(self, arg):
        """Read a file into the next input"""
        self.steps.append(step.InjectStep(arg.strip()))

    def do_run(self, arg):
        """Execute the pipeline"""

        data, args = '', []

        for step in self.steps:
            data, args = step.run(data, args)

        print(data)

    def do_save(self, arg):
        """Save the pipeline"""
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents = True)

        with self.path.open('wb') as f:
            pickle.dump(self.steps, f)

    def do_quit(self, arg):
        """Exit Pipeline"""
        sys.exit(0)
