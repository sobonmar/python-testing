# Ładowanie doctestów
import unittest
import doctest
from _doctest import example_01, account


# Z modułu
# doctest_suit = doctest.DocTestSuite(example_01)
#
# runner = unittest.TextTestRunner()
# runner.run(doctest_suit)

# Z pliku tekstowego
suite = doctest.DocTestSuite(
    'test_account',
    package='_doctest',
    globs=vars(account),
)