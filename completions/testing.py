# THIS_IS_A_SPECIAL_TAG_FOR_PYTHON_AUTOCOMPLETE_COMPLETION
import argparse
from completer import ArgCompleter
from completer import FilesCompleter


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--hello')
parser.add_argument('world').completer = FilesCompleter()
ArgCompleter(parser)
print("hello world")