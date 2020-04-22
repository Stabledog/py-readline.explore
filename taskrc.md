## taskrc.md for py-readline.explore


[Python readline help](https://pymotw.com/3/readline/)

```bash

py=`which python3.7`

function run_one {
#Help
    xtty=$(cat .diagloop-tty)
    $py ./readline_parse_and_bind.py 9>$xtty
}

function debug_one {
#Help
    echo "This is debug_one()"
}

function vscode_sh_init {
    #Help (this runs when vscode starts a terminal)
    dev-loop
}
```
