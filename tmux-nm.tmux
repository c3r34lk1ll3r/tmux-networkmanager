#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATH="/usr/local/bin:$PATH:/usr/sbin"

main() {
    $(tmux bind-key -T prefix N run -b "python $CURRENT_DIR/scripts/nmcli.py")
}

main
