# Doctest internals
import doctest


test_string = """
>>> 2 + 2
3
"""


# doctest.run_docstring_examples(test_string, globals())

import context

with open("tests") as f:
    tests = f.read()


doctest.run_docstring_examples(tests, vars(context))
