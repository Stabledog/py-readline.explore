## taskrc.md for py-readline.explore


[Python readline help](https://pymotw.com/3/readline/)

```bash

py=`which python3.7`

function run_one {
#Help
    xtty=$(cat .diagloop-tty)
    echo "xtty=${xtty}"
    echo "hello" >${xtty}
    #$py ./readline_parse_and_bind.py 9>$xtty
    $py ./readline_completer.py 9>${xtty}
}

function debug_one {
#Help
    echo "This is debug_one()"
}

function vscode_sh_init {
    #Help (this runs when vscode starts a terminal)
    dev-loop 2>/dev/null
}
```
