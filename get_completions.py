import sys
import os
import subprocess

completion_arg = '--auto-complete-for-eytans-complete'
completion_tag = "THIS_IS_A_SPECIAL_TAG_FOR_PYTHON_AUTOCOMPLETE_COMPLETION"
if __name__ == '__main__':
    cur_word = sys.argv[1]
    all_words = sys.argv[2:]
    exe = all_words[0]
    i = 1
    if exe == 'python':
        while i < len(all_words):
            if not all_words[i].startswith('-'):
                exe = all_words[i]
                break
            i += 1

    if exe == 'python':
        exit()

    # verify exe has necessary rag
    if not os.path.exists(exe):
        exit()

    with open(exe) as txt:
        data = txt.read(4096)
        if completion_tag not in data:
            exit(0)

    sub_exe = all_words[0:i+1]
    e = os.environ.copy()
    subprocess.call(sub_exe + [completion_arg, str(cur_word)] + all_words)
