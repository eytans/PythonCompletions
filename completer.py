from sys import argv
from get_completions import completion_arg

# This is here to make it look like i wrote completers even though im lazy
from argcomplete.completers import *


class OptionCompleter(object):
    def __init__(self, actions):
        """
        For each option in parser, try to complete it.
        :param parser: argparse argument parser fully initialized
        """
        self.actions = actions

    def __call__(self, prefix, **kwargs):
        all_options = [o for a in self.actions for o in a.option_strings]
        prefixes = (o for o in all_options if o.startswith(prefix))
        return prefixes


class ArgCompleter(object):
    def __init__(self, parser):
        """
        We use init to print the autocomplete and exit. If complete arg isn't in argv we do nothing.
        :param parser: argparse argument parser fully initialized
        """
        if completion_arg not in argv:
            return
        i = argv.index(completion_arg)
        cur_word = int(argv[i+1])
        all_words = argv[i + 2:]
        if cur_word == len(all_words):
            all_words.append('')
        while len(argv) > i:
            argv.pop()

        # start completion by parser
        actions = parser._actions
        options = OptionCompleter(actions)
        prefix = all_words[cur_word]

        if all_words[cur_word] == '' or all_words[cur_word].startswith('-'):
            results = options(prefix)
        else:
            if cur_word == 0:
                exit(0)
            o = all_words[cur_word]
            action = None
            for a in actions:
                if o in a.option_strings:
                    action = a
                    break
            if action is None or not hasattr(action, 'completer'):
                exit(0)

            completer = action.completer
            results = completer(prefix)

        for res in results:
            print(res)
        exit(0)

