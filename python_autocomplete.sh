#!/usr/bin/env bash

if [[ $1 == "--install" ]] && [[ `realpath .` ]]; then
    temp_path=$0
    full_path="`realpath ${temp_path}`"
    get_completion_path="`dirname ${full_path}`/get_completions.py"
    echo "function _python-autocomplete {
COMPREPLY=(\`python $get_completion_path \$COMP_CWORD \${COMP_WORDS[@]}\`)
}
complete -F _python-autocomplete python" >> ~/.bashrc
fi