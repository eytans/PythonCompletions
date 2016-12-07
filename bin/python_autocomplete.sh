#!/usr/bin/env bash

if [[ $1 == "--install" ]]; then
    echo source python_autocomplete.sh >> ~/.bashrc
fi

function _python-autocomplete {
    COMPREPLY=(`get_python_completions $COMP_CWORD ${COMP_WORDS[@]}`)
}

complete -o bashdefault -o nospace -F _python-autocomplete python