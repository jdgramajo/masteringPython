"""Encapsulates single steps of the pipeline

Each step type is represented by a subclass of Step, which is
instantiated by the interface.

"""

from subprocess import Popen, PIPE
from datetime import datetime

now = datetime.now()

class Step:
    """An abstract representation of a single pipeline step"""

    def run(self, data, args):
        """Execute the step

        The parameters are string data to feed into the program, and
        additional arguments to pass to the program.

        The return value is a 2-tuple containing string data to feed
        to the next program, and a list of command line arguments to
        pass to the next program.

        For steps that do not represent execution of a program, the
        meanings are analogous.

        """
        return '', []

class ExecStep(Step):
    """Represents the execution of a program as a pipeline step"""

    def __init__(self, args):
        """Collect the command line for the executed program"""
        self.args = args

    def run(self, data, args):
        """Run the program with the given input and arguments"""
        p = Popen(self.args + args,
                  stdin=PIPE,
                  stdout=PIPE,
                  bufsize=0,
                  universal_newlines=True)
        out, err = p.communicate(data)
        return out, []

class ArgsStep(Step):
    """Split the output of the prior step into arguments for the next"""

    def __init__(self, separator = None):
        """Collect the separator pattern to use for splitting"""
        self.separator = separator

    def run(self, data, args):
        """Perform the split and return the results as args"""
        return '', args + data.split(self.separator)

class StoreStep(Step):
    """Redirect the output of the prior step into a file"""

    def __init__(self, filename):
        """Set the file name to be stored into"""
        self.filename = filename

    def run(self, data, args):
        """Redirect the data, and return empty data"""
        with open(now.strftime(self.filename), 'w') as f:
            f.write(data)
        return '', args

class InjectStep(Step):
    """Redirect input of the next step from a file"""

    def __init__(self, filename):
        """Self the file name to be read from"""
        self.filename = filename

    def run(self, data, args):
        """load the data, and return them"""
        with open(now.strftime(self.filename), 'r') as f:
            return f.read(), args
