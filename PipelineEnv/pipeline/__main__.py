"""Run a sequence of programs.

Each program (except the first receives the standard output of the
previous program on its standard input, by default. There are several
alternate ways of passing data between the programs.

"""

import argparse

from pipeline.interface import TextInterface


def _launch():
    parser = argparse.ArgumentParser(prog = "python -m pipeline",
                                     description = __doc__)

    parser.add_argument("-k", "--keep-going",
                        action = "store_true",
                        default = False)

    parser.add_argument("filename")

    args = parser.parse_args()

    iface = TextInterface(args.keep_going, args.filename)
    iface.cmdloop()


if __name__ == "__main__":
    _launch()
