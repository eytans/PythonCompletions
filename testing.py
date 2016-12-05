# THIS_IS_A_SPECIAL_TAG_FOR_PYTHON_AUTOCOMPLETE_COMPLETION
import argparse
from completer import ArgCompleter


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--hello')
ArgCompleter(parser)
print("hello world")