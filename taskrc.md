## taskrc.md for py-readline.explore


[Python readline help](https://pymotw.com/3/readline/)

```bash

py=`which python3.7`
#scr=readline_completer.py
scr=readline_buffer.py

function get_xtty {
    local xtty=$(cat .diagloop-tty)
    if [[ ! -c $xtty ]]; then
        xtty=/dev/null
    fi
    echo $xtty
}

function run_one {
#Help
    #$py ./readline_parse_and_bind.py 9>$xtty
    $py $scr 9>$(get_xtty)
}

function debug_one {
    #Help debug the checkerz app inside dev-loop.sh
    cd $taskrc_dir
    clear
    echo "debug() waiting in $PWD for debugger attach on 0.0.0.0:5678..."

    $py -m ptvsd --host 0.0.0.0 --port 5678 --wait $scr "$@" 9>$(get_xtty)
    stty sane
}

function vscode_sh_init {
    #Help (this runs when vscode starts a terminal)
    dev-loop 2>/dev/null
}
```
