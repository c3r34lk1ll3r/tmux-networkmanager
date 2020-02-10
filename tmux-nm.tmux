#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATH="/usr/local/bin:$PATH:/usr/sbin"
main() {
    if [ -z "$TMCLI_PYTHON" ]
    then
        NMCLI_PYTHON=$(which python)
    fi
    $(tmux bind-key -T prefix N run -b "$TMCLI_PYTHON $CURRENT_DIR/scripts/nmcli.py")
}

main
