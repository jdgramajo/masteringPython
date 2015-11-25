"""Run a sequence of programs.

Each program (except the first receives the standard output of the
previous program on its standard input, by default. There are several
alternate ways of passing data between the programs.

"""


def _launch():
    print("Pipeline launched!")


if __name__ == "__main__":
    _launch()
